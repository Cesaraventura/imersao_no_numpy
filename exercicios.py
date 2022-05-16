import numpy as np

# ex 1 : Extraia todos os números ímpares de ‘arr’
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr1 = arr[arr % 2 == 1]
print(arr1)

# ex 2 : substitua todos os números ímpares em arr com -1 sem alterar arr
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
print(out)

# ex 3 : Empilhe matrizes verticalmente:
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
array = np.concatenate([a, b], axis=0)
print(array)

# ex 4 : Calcule a pontuação softmax de ‘sepal length’:
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
sepallength = np.array([float(row[0]) for row in iris])

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)
print(softmax(sepallength))

# ex 5 : Calcule as contagens de valores únicos na linha.
np.random.seed(100)
arrx = np.random.randint(1,11,size=(6, 10))
print(arrx)
def counts_of_all_values_rowwise(arr2d):
    num_counts_array = [np.unique(row, return_counts=True) for row in arr2d]
    return([[int(b[a==i]) if i in a else 0 for i in np.unique(arr2d)] for a, b in num_counts_array])

print(np.arange(1,11))
matrix = counts_of_all_values_rowwise(arrx)
print(matrix)