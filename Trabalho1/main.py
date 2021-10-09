import ctypes
from inspect import getmembers, isclass, isfunction
from typing import NewType
import clr
import sys


sys.path.append(r"F:\Roger\Faculdade\Inteligencia Artificial Avançada\Trabalho1\AdrenaDLL")
clr.AddReference("ADReNA_API")

from ADReNA_API.NeuralNetwork import Backpropagation
from ADReNA_API.Data import DataSet, DataSetObject

neural = Backpropagation(2, 1)

trainingSet = DataSet(2,1)

# Ajustar treinamento, são dois parametros de arrays de double
trainingSet.Add(DataSetObject( {0,0}, {0} ))
trainingSet.Add(DataSetObject( {0,1}, {1} ))
trainingSet.Add(DataSetObject( {1,0}, {1} ))
trainingSet.Add(DataSetObject( {1,1}, {0} ))

neural.learn(trainingSet)


#Para verificar as funções da classe
#print(getmembers(neural))