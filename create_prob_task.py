E = [1000, 1200, 1500, 2000]
A = [200, 240, 140, 200]
B = [50, 60, 70]
C = [96, 48]
CONST = 1382400

def M(a, b):
    return (a + b) / 2


material_to_factory_a = [
    [M(10, 30), M(50, 90), M(40, 60), M(30, 50)],
    [M(40, 80), M(20, 60), M(40, 60), M(10, 30)]
]

material_to_factory_b = [
    [M(40, 60), M(15, 25), M(20, 60)],
    [M(10, 30), M(35, 45), M(10, 30)]
]

base_factory = [
    [50, 60, 50, 100],
    [50, 40, 60, 100]
]
alpha = [4, 5]
betha = [10, 8]


prob_task = {
    "func": {
        "coefs": [],
        "target": "min"
    },
    "restrictions": []
}

coefs_names = {}
m = 0

for k in range(2):
    for i in range(4):
        prob_task["func"]["coefs"].append(A[i] + material_to_factory_a[k][i] + C[k] * betha[k])
        coefs_names[f"x_{i}_{k}"] = m
        m += 1
    for j in range(3):
        prob_task["func"]["coefs"].append(B[j] + material_to_factory_b[k][j])
        coefs_names[f"y_{j}_{k}"] = m
        m += 1

    for n in range(4):
        prob_task["func"]["coefs"].append(base_factory[k][n])
        coefs_names[f"gamma_{k}_{n}"] = m
        m += 1

for n in range(4):
    restriction = {
        "coefs": [0] * len(prob_task["func"]["coefs"]),
        "sign": ">=",
        "value": E[n]
    }
    for k in range(2):
        restriction["coefs"][coefs_names[f"gamma_{k}_{n}"]] = 1

    prob_task["restrictions"].append(restriction)

for k in range(2):
    restriction = {
        "coefs": [0] * len(prob_task["func"]["coefs"]),
        "sign": "=",
        "value": 0
    }
    for n in range(4):
        restriction["coefs"][coefs_names[f"gamma_{k}_{n}"]] = 1
    for i in range(4):
        restriction["coefs"][coefs_names[f"x_{i}_{k}"]] = - betha[k]

    prob_task["restrictions"].append(restriction)

for k in range(2):
    restriction = {
        "coefs": [0] * len(prob_task["func"]["coefs"]),
        "sign": "=",
        "value": 0
    }
    for i in range(4):
        restriction["coefs"][coefs_names[f"x_{i}_{k}"]] = 1
    for j in range(3):
        restriction["coefs"][coefs_names[f"y_{j}_{k}"]] = - alpha[k]
    prob_task["restrictions"].append(restriction)
prob_task['func']['const'] = CONST

print()
