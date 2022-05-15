import numpy as np

#array a partir de uma lista
new_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(new_matrix)

custo = [100,200,300,400]
venda = [125,225,350,475]

arr1 = np.array(custo)
arr2 = np.array(venda)

lucro = arr2-arr1
print(lucro)

#array a partir do numpy
#arange()
range = np.arange(10,20,2,dtype=float)
print(range)

#linspace()
lin = np.linspace(0,1,10)
print(lin)

#random  rand, randn, randint
rand1 = np.random.rand(10)
print(rand1)

rand2 = np.random.randn(15)
print(rand2)

rand3 = np.random.randint(10,100,30)
print(rand3)

#zeros e uns e eyes(identidade)
matriz1 = np.zeros((5,4))
print(matriz1)

matriz2 = np.ones((5,5))
print(matriz2)

matriz3 = np.eye((6))
print(matriz3)

# indexação de arrays
arr = np.arange(1,11,dtype=int)
print(arr)

#index unidimensionais
arr1 = arr[4]
print(arr1)

#index bidimensionais
arr2 = np.random.randint(10,50,size=(3,3))
print(arr2)

arr3 = arr2[2][2]
print(arr3)

arr4 = arr2[1][0:2]
print(arr4)

#selecao de arrays
cadastro = np.random.randint(15,51,size=(50,10))
print(cadastro)

cadastro_maior18 = cadastro > 18
print(cadastro_maior18)

cadastro1 = cadastro[cadastro_maior18]
print(cadastro1)

quantidade = len(cadastro1)
print(quantidade)

#ou cadastro_maior18.sum()

condicao = (cadastro>20)
extraido = np.extract(condicao,cadastro)
print(extraido)
