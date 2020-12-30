E = [1000, 1200, 1500, 2000]
A = [200, 240, 140, 200]
B = [50, 60, 70]
C = [96, 48]
CONST = 1382400

material_to_factory_a = [
    [20, 70, 50, 40],
    [60, 40, 50, 20]
]

material_to_factory_b = [
    [50, 20, 40],
    [20, 40, 20]
]

base_factory = [
    [5, 4, 5, 10],
    [5, 3, 6, 10]
]
alpha = [4, 5]
betha = [10, 8]


task = {
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
        task["func"]["coefs"].append(A[i] + material_to_factory_a[k][i] + C[k] * betha[k])
        coefs_names[f"x_{i}_{k}"] = m
        m += 1
    for j in range(3):
        task["func"]["coefs"].append(B[j] + material_to_factory_b[k][j])
        coefs_names[f"y_{j}_{k}"] = m
        m += 1

    for n in range(4):
        task["func"]["coefs"].append(base_factory[k][n])
        coefs_names[f"gamma_{k}_{n}"] = m
        m += 1

for n in range(4):
    restriction = {
        "coefs": [0] * len(task["func"]["coefs"]),
        "sign": ">=",
        "value": E[n]
    }
    for k in range(2):
        restriction["coefs"][coefs_names[f"gamma_{k}_{n}"]] = 1

    task["restrictions"].append(restriction)

for k in range(2):
    restriction = {
        "coefs": [0] * len(task["func"]["coefs"]),
        "sign": "=",
        "value": 0
    }
    for n in range(4):
        restriction["coefs"][coefs_names[f"gamma_{k}_{n}"]] = 1
    for i in range(4):
        restriction["coefs"][coefs_names[f"x_{i}_{k}"]] = - betha[k]

    task["restrictions"].append(restriction)

for k in range(2):
    restriction = {
        "coefs": [0] * len(task["func"]["coefs"]),
        "sign": "=",
        "value": 0
    }
    for i in range(4):
        restriction["coefs"][coefs_names[f"x_{i}_{k}"]] = 1
    for j in range(3):
        restriction["coefs"][coefs_names[f"y_{j}_{k}"]] = - alpha[k]
    task["restrictions"].append(restriction)

task['func']['const'] = CONST
print()