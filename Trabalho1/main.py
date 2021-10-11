
import clr
import sys, os
from numpy import float64
import pandas as pd 
from decimal import Decimal

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

sys.path.append(os.path.join(__location__, 'AdrenaDLL'))
clr.AddReference("ADReNA_API")

from ADReNA_API.NeuralNetwork import Backpropagation
from ADReNA_API.Data import DataSet, DataSetObject


def exampleBackpropagation():
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


def openTrainingSet(fileName) :
    trainingSet = pd.read_csv(os.path.join(__location__, 'Dataset', fileName))

    return trainingSet

def datasetTreatment():
    strokeData = openTrainingSet('healthcare-dataset-stroke-data.csv')

    #Tratamento dos dados, convertendo dados para binarios

    residence_mapping = {'Urban': 0, 'Rural': 1}
    strokeData['Residence_type'] = strokeData['Residence_type'].map(residence_mapping)

    marriage_mapping = {'No': 0, 'Yes': 1}
    strokeData['ever_married'] = strokeData['ever_married'].map(marriage_mapping)

    strokeData['gender'] = pd.Categorical(strokeData['gender'])
    strokeDataAux_gender = pd.get_dummies(strokeData['gender'], prefix = 'gender')

    strokeData['smoking_status'] = pd.Categorical(strokeData['smoking_status'])
    strokeDataAux_smoking_status = pd.get_dummies(strokeData['smoking_status'], prefix = 'smoking_status')

    strokeData['work_type'] = pd.Categorical(strokeData['work_type'])
    strokeDataAux_work_type = pd.get_dummies(strokeData['work_type'], prefix = 'work_type')

    strokeData.drop(['id'], axis = 1, inplace=True)
    strokeData.drop("gender", axis=1, inplace=True)
    strokeData.drop("work_type", axis=1, inplace=True)
    strokeData.drop("smoking_status", axis=1, inplace=True)

    strokeData = pd.concat([strokeData, strokeDataAux_gender], axis=1)
    strokeData = pd.concat([strokeData, strokeDataAux_work_type], axis=1)
    strokeData = pd.concat([strokeData, strokeDataAux_smoking_status], axis=1)
    
    return(strokeData)

def trainingSet(neuronIn, neuronOut):
    dataSet = datasetTreatment()

    neuralNet = Backpropagation(neuronIn, neuronOut)

    trainingSet = DataSet(neuronIn, neuronOut)

    # Treinamento do Set
    for row in dataSet.itertuples(index=True, name='Pandas'):
        
        trainingSet.Add(DataSetObject( [ float(row.age), float(row.hypertension), float(row.heart_disease), float(row.ever_married), float(row.Residence_type), float(row.avg_glucose_level), float(row.bmi), float(row.gender_Female), float(row.gender_Male), float(row.gender_Other), float(row.work_type_Govt_job), float(row.work_type_Never_worked), float(row.work_type_Private), float(row.work_type_Self_employed), float(row.work_type_children), float(row.smoking_status_Unknown), float(row.smoking_status_formerly_smoked), float(row.smoking_status_never_smoked), float(row.smoking_status_smokes)], [float(row.stroke)]))
        break

    print(trainingSet)

    #neuralNet.Learn(trainingSet)

    # Exemplo de reconhecimento
    #res = neuralNet.Recognize([0,1])



#res = datasetTreatment()

trainingSet(19, 1)
