
import clr
import sys


sys.path.append(r"F:\Roger\Faculdade\Inteligencia Artificial Avançada\Trabalho1\AdrenaDLL")
clr.AddReference("ADReNA_API")

from ADReNA_API.NeuralNetwork import Backpropagation
from ADReNA_API.Data import DataSet, DataSetObject

neural = Backpropagation(2, 1)

trainingSet = DataSet(2,1)

# Treinamento do Set
trainingSet.Add(DataSetObject( [0,0], [0] ))
trainingSet.Add(DataSetObject( [0,1], [1] ))
trainingSet.Add(DataSetObject( [1,0], [1] ))
trainingSet.Add(DataSetObject( [1,1], [0] ))

neural.Learn(trainingSet)

# Exemplo de reconhecimento
res = neural.Recognize([0,1])

print("%.0f" % res[0])