from prob_task import prob_task, show_prob_task, coef_names
from task import task, show_task
from simplex_solver import SimplexSolver
from pprint import pprint
from pandas import DataFrame as df

# print("Коєфіцієнти чіткої задачі")
# show_task()
# print("Коєфіцієнти нечіткої задачі")
# show_prob_task()
solver = SimplexSolver(task, coef_names)
solver.show_result()
print("\n")
solver_prob = SimplexSolver(prob_task, coef_names)

solver.show_intermediate_results()
# pprint([(i, j) for i, j in zip(coef_names, solver.result['x'])])
# pprint(solver.result)