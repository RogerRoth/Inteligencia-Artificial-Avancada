import clr
import sys, os
import pandas as pd 

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

sys.path.append(os.path.join(__location__, 'AdrenaDLL'))
clr.AddReference("ADReNA_API")
clr.AddReference("Newtonsoft.Json")

from Newtonsoft.Json import *
from ADReNA_API.NeuralNetwork import Backpropagation
from ADReNA_API.Data import DataSet, DataSetObject
from ADReNA_API.Util import Import

def importNeuralNet():

    #neuralNet = Import.NeuralNetworkStructure('trainedNeuralNetworkStructure')
    neuralNet = Backpropagation(19, 1)
    Import.KnowledgeBase(neuralNet, 'trainedKnowledgeBase')

    print('Entrada', neuralNet.GetInputLayerSize())
    print('Saida', neuralNet.GetOutputLayerSize())

    return neuralNet

def reconhecimento(neuralNet, data):

    reconhecimento = neuralNet.Recognize(data)

    return reconhecimento



#Pandas(Index=88, age=47.0, hypertension=0, heart_disease=0, ever_married=1, Residence_type=0, avg_glucose_level=86.94, bmi=41.1, stroke=1, gender_Female=0, gender_Male=1, gender_Other=0, work_type_Govt_job=0, work_type_Never_worked=0, work_type_Private=1, work_type_Self_employed=0, work_type_children=0, smoking_status_Unknown=0, smoking_status_formerly_smoked=1, smoking_status_never_smoked=0, smoking_status_smokes=0)  

#Pandas(Index=2394, age=19.0, hypertension=0, heart_disease=0, ever_married=0, Residence_type=0, avg_glucose_level=83.43, bmi=38.4, stroke=0, gender_Female=1, gender_Male=0, gender_Other=0, work_type_Govt_job=0, work_type_Never_worked=0, work_type_Private=1, work_type_Self_employed=0, work_type_children=0, smoking_status_Unknown=1, smoking_status_formerly_smoked=0, smoking_status_never_smoked=0, smoking_status_smokes=0) 
'''
[ float(row.age), float(row.hypertension), float(row.heart_disease), float(row.ever_married), float(row.Residence_type), 
float(row.avg_glucose_level), float(row.bmi), float(row.gender_Female), float(row.gender_Male), float(row.gender_Other), 
float(row.work_type_Govt_job), float(row.work_type_Never_worked), float(row.work_type_Private), float(row.work_type_Self_employed), 
float(row.work_type_children), float(row.smoking_status_Unknown), float(row.smoking_status_formerly_smoked), 
float(row.smoking_status_never_smoked), float(row.smoking_status_smokes)], [float(row.stroke)])
'''

#Stroke True
testData = [47.0, 0, 0, 1, 0, 86.94, 41.1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]


#Stroke False
#testData = [19.0, 0, 0, 0, 0, 83.43, 38.4, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]


neuralNet = importNeuralNet()
rec = reconhecimento(neuralNet, testData)
print(rec[0])