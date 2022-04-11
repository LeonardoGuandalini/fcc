import numpy as np

def calculate(array):
  if len(array) == 9:
    converted_array = np.array(array)
    converted_array = converted_array.reshape(3,3)
    mean = [converted_array.mean(axis=0).tolist(), converted_array.mean(axis=1).tolist(), converted_array.mean().tolist()]
    variance = [converted_array.var(axis=0).tolist(), converted_array.var(axis=1).tolist(), converted_array.var().tolist()]
    std = [converted_array.std(axis=0).tolist(), converted_array.std(axis=1).tolist(), converted_array.std().tolist()]
    max = [converted_array.max(axis=0).tolist(), converted_array.max(axis=1).tolist(), converted_array.max().tolist()]
    min = [converted_array.min(axis=0).tolist(), converted_array.min(axis=1).tolist(), converted_array.min().tolist()]
    sum = [converted_array.sum(axis=0).tolist(), converted_array.sum(axis=1).tolist(), converted_array.sum().tolist()]
    calculations = {'mean': mean, 'variance': variance, 'standard deviation': std, 'max': max, 'min': min, 'sum': sum }
    return calculations
  else:
    raise ValueError("List must contain nine numbers.")
