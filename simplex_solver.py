import pandas as pd
from scipy.optimize import linprog

import custom_exceptions


class SimplexSolver:
    def __init__(self, task, coef_names=None):
        self.betha = task['betha']
        self.coef_names = coef_names
        self._intermediate_results = []
        if 'const' in task['func']:
            self.const = task['func']['const']
        else:
            self.const = 0
        self._target = task["func"]["target"]
        if self._target == "min":
            self.func_coefs = task["func"]["coefs"]
        elif self._target == "max":
            self.func_coefs = [-c for c in task["func"]["coefs"]]
        else:
            raise custom_exceptions.UnknownTargetError(
                f"Got unknown target in 'func' dictionary - {task['func']['target']}")

        equality_restrictions_coefs = []
        less_restrictions_coefs = []
        equality_restrictions_values = []
        less_restrictions_values = []
        for i, restriction in enumerate(task['restrictions']):
            if restriction["sign"] in ("==", "="):
                equality_restrictions_coefs.append(restriction["coefs"])
                equality_restrictions_values.append(restriction["value"])
            elif restriction["sign"] in ("<=", "<"):
                less_restrictions_coefs.append(restriction["coefs"])
                less_restrictions_values.append(restriction["value"])
            elif restriction["sign"] in (">=", ">"):
                less_restrictions_coefs.append([-c for c in restriction["coefs"]])
                less_restrictions_values.append(-restriction["value"])
            else:
                raise custom_exceptions.UnknownSignError(f"Unknown sign in restriction {i} - {restriction['sign']}")
        self.equality_restrictions_coefs = equality_restrictions_coefs
        self.less_restrictions_coefs = less_restrictions_coefs
        self.equality_restrictions_values = equality_restrictions_values
        self.less_restrictions_values = less_restrictions_values
        self.bounds = [(0, float("inf"))] * len(self.func_coefs)
        self.result = None
        self._opt = None
        self._solve()

    def _solve(self):
        intemeiate_results = self._intermediate_results

        def intermediate_callback(x):
            size = max(x.con.shape[0] + x.slack.shape[0], x.x.shape[0])
            simplex_table = {
                "delta": list(x.con) + list(x.slack) + ["-"] * (size - x.con.shape[0] - x.slack.shape[0]),
                "current_x": list(x.x) + ["-"] * (size - x.x.shape[0]),
                "value": [x.fun] + ["-"] * (size - 1)
            }
            intemeiate_results.append(pd.DataFrame(simplex_table))

        self._opt = linprog(c=self.func_coefs, A_ub=self.less_restrictions_coefs, b_ub=self.less_restrictions_values,
                            A_eq=self.equality_restrictions_coefs,
                            b_eq=self.equality_restrictions_values, bounds=self.bounds, method="simplex",
                            callback=intermediate_callback)
        self.result = {}
        if self._target == "min":
            self.result[self._target] = self._opt.fun + self.const
        elif self._target == "max":
            self.result[self._target] = -self._opt.fun + self.const
        else:
            raise custom_exceptions.UnknownTargetError(
                f"Got unknown target in 'func' dictionary - {task['func']['target']}")
        self.result["x"] = []
        for xi in self._opt.x:
            self.result["x"].append(xi)
        self.result["iterations"] = self._opt.nit

    def show_result(self):
        res = pd.DataFrame(self.result['x'], index=self.coef_names)
        if self.betha:
            for k in range(2):
                print(
                    f'Number of T on factory {k}: {sum([self.betha[k] * v for v in self.result["x"][k * 11:k * 11 + 4]])}')
        print(f'{self._target} value: {self.result[self._target]}')
        print(f'Iterations: {self.result["iterations"]}')
        print(res)

    def show_intermediate_results(self):
        for i in self._intermediate_results:
            print(i)
