import concurrent.futures
import time

import numpy as np
import SALib
from SALib.analyze import sobol
from SALib.sample import saltelli
from SALib.test_functions import Ishigami

# Define the model inputs
problem = {
    "num_vars": 3,
    "names": ["x1", "x2", "x3"],
    "bounds": [
        [-3.14159265359, 3.14159265359],
        [-3.14159265359, 3.14159265359],
        [-3.14159265359, 3.14159265359],
    ],
}


def evaluate_model(X):
    answer = X[0] * 12

    return answer


# Generate samples
param_values = saltelli.sample(problem, 2048)

# Run model (example)
Y = Ishigami.evaluate(param_values)


np.savetxt("param_values.txt", param_values)

# Y = np.zeros([param_values.shape[0]])
t1 = time.perf_counter()


def analysis(values):
    # print("started")
    Y = np.zeros([param_values.shape[0]])
    for i, row in enumerate(values):
        Y[i] = evaluate_model(row)

    print("ended")
    return Y


# Si = sobol.analyze(problem, Y)


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(analysis, param_values)


if __name__ == "__main__":
    main()
    t2 = time.perf_counter()
    print(f"Finished in {round(t2-t1,2)} seconds")
