import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    # dictionary to be created
    calculations = {}

    # Creating the array
    matrix = np.array([(list[0], list[1], list[2]), (list[3],
                      list[4], list[5]), (list[6], list[7], list[8])], dtype=float)
    # columns
    col = [matrix[0, 0:3], matrix[1, 0:3], matrix[2, 0:3]]
    # rows
    row = [matrix[0:3, 0], matrix[0:3, 1], matrix[0:3, 2]]
    # flattened array
    flat = matrix.ravel()
    # target
    target = [row[0], row[1], row[2], col[0], col[1], col[2], flat]

    # mean calculations
    calculations["mean"] = [[np.mean(target[i]) for i in range(0, 3)], [
        np.mean(target[i]) for i in range(3, 6)], np.mean(target[6])]
    # variance calculations
    calculations["variance"] = [[np.var(target[i]) for i in range(0, 3)], [
        np.var(target[i]) for i in range(3, 6)], np.var(target[6])]
    # standard deviation calculations
    calculations["standard deviation"] = [[np.std(target[i]) for i in range(
        0, 3)], [np.std(target[i]) for i in range(3, 6)], np.std(target[6])]
    # max
    calculations["max"] = [[np.max(target[i]) for i in range(0, 3)], [
        np.max(target[i]) for i in range(3, 6)], np.max(target[6])]
    # min
    calculations["min"] = [[np.min(target[i]) for i in range(0, 3)], [
        np.min(target[i]) for i in range(3, 6)], np.min(target[6])]
    # sum
    calculations["sum"] = [[np.sum(target[i]) for i in range(0, 3)], [
        np.sum(target[i]) for i in range(3, 6)], np.sum(target[6])]

    return calculations
