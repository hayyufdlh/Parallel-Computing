from multiprocessing import Pool
import numpy as np

def add_row(args):
    row1, row2 = args
    return row1 + row2

if __name__ == "__main__":
    A = np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])

    B = np.array([
        [9,8,7],
        [6,5,4],
        [3,2,1]
    ])

    with Pool() as pool:
        result = pool.map(add_row, zip(A,B))

    C = np.array(result)

    print("Matrix A:")
    print(A)

    print("\nMatrix B:")
    print(B)

    print("\nResult A+B:")
    print(C)
