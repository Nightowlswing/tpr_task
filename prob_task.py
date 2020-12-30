import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)

prob_task = {'func': {
    'coefs': [1180.0, 1270.0, 1150.0, 1200.0, 100.0, 80.0, 110.0, 50, 60, 50, 100, 644.0, 664.0, 574.0, 604.0, 70.0,
              100.0, 90.0, 50, 40, 60, 100], 'target': 'min', 'const': 1382400},
    'restrictions': [
        {'coefs': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 'sign': '>=', 'value': 1000},
        {'coefs': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 'sign': '>=', 'value': 1200},
        {'coefs': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 'sign': '>=', 'value': 1500},
        {'coefs': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 'sign': '>=', 'value': 2000},
        {'coefs': [-10, -10, -10, -10, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'sign': '=', 'value': 0},
        {'coefs': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8, -8, -8, -8, 0, 0, 0, 1, 1, 1, 1], 'sign': '=', 'value': 0},
        {'coefs': [1, 1, 1, 1, -4, -4, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'sign': '=', 'value': 0},
        {'coefs': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, -5, -5, -5, 0, 0, 0, 0], 'sign': '=', 'value': 0}],
    "betha": [10, 8]
    }

coef_names = {
    'x_0_0': 0,
    'x_1_0': 1,
    'x_2_0': 2,
    'x_3_0': 3,
    'y_0_0': 4,
    'y_1_0': 5,
    'y_2_0': 6,
    'theta_0_0': 7,
    'theta_0_1': 8,
    'theta_0_2': 9,
    'theta_0_3': 10,
    'x_0_1': 11,
    'x_1_1': 12,
    'x_2_1': 13,
    'x_3_1': 14,
    'y_0_1': 15,
    'y_1_1': 16,
    'y_2_1': 17,
    'theta_1_0': 18,
    'theta_1_1': 19,
    'theta_1_2': 20,
    'theta_1_3': 21
}

def show_prob_task():
    res = pd.DataFrame(
        data=[prob_task['func']['coefs']]+[rest['coefs'] for rest in prob_task['restrictions']],
        index=["function"]+[f"restriction {i}" for i in range(len([rest['coefs'] for rest in prob_task['restrictions']]))],
        columns=list(coef_names.keys())
    )
    print(res)