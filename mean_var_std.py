import numpy as np

def calculate(l):
    if len(l) !=9:
        raise ValueError("List must contain nine numbers.")
    m = np.array(l).reshape(3,3)
    # print(m)
    calculations = {
            'mean': [np.mean(m, axis = 0).tolist(), np.mean(m, axis = 1).tolist(), np.mean(l)],
            'variance': [np.var(m, axis = 0).tolist(), np.var(m, axis = 1).tolist(), np.var(l)],
            'standard deviation': [np.std(m, axis = 0).tolist(), np.std(m, axis = 1).tolist(), np.std(l)],
            'max': [np.max(m, axis = 0).tolist(), np.max(m, axis = 1).tolist(), np.max(l)],
            'min': [np.min(m, axis = 0).tolist(), np.min(m, axis = 1).tolist(), np.min(l)],
            'sum': [np.sum(m, axis = 0).tolist(), np.sum(m, axis = 1).tolist(), np.sum(l)]
    }


    return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))