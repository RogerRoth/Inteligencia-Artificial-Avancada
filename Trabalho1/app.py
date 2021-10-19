import clr
import sys, os
import pandas as pd 
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

sys.path.append(os.path.join(__location__, 'AdrenaDLL'))
clr.AddReference("ADReNA_API")
clr.AddReference("Newtonsoft.Json")

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "app.ui")

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

class AppApp:
    def __init__(self, master=None):
        # build ui
        self.tp_Main = tk.Tk() if master is None else tk.Toplevel(master)
        self.label6 = tk.Label(self.tp_Main)
        self.label6.configure(text='Gender:')
        self.label6.grid(column='0', row='0', sticky='w')
        self.label7 = tk.Label(self.tp_Main)
        self.label7.configure(text='Age:')
        self.label7.grid(column='0', row='1', sticky='w')
        self.label9 = tk.Label(self.tp_Main)
        self.label9.configure(text='Heart Disease:')
        self.label9.grid(column='0', row='3', sticky='w')
        self.label10 = tk.Label(self.tp_Main)
        self.label10.configure(text='Ever Married:')
        self.label10.grid(column='0', row='4', sticky='w')
        self.label11 = tk.Label(self.tp_Main)
        self.label11.configure(text='Work Type:')
        self.label11.grid(column='0', row='5', sticky='w')
        self.label12 = tk.Label(self.tp_Main)
        self.label12.configure(text='Residence Type:')
        self.label12.grid(column='0', row='6', sticky='w')
        self.label13 = tk.Label(self.tp_Main)
        self.label13.configure(text='AVG Glucose Level:')
        self.label13.grid(column='0', row='7', sticky='w')
        self.label14 = tk.Label(self.tp_Main)
        self.label14.configure(text='Body Mass Index:')
        self.label14.grid(column='0', row='8', sticky='w')
        self.label15 = tk.Label(self.tp_Main)
        self.label15.configure(text='Smoke Status:')
        self.label15.grid(column='0', row='9', sticky='w')
        self.label8 = tk.Label(self.tp_Main)
        self.label8.configure(text='Hypertension:')
        self.label8.grid(column='0', row='2', sticky='w')
        self.label22 = tk.Label(self.tp_Main)
        self.label22.configure(text='Results:')
        self.label22.grid(column='0', row='14', sticky='w')

        self.cbx_Gender = ttk.Combobox(self.tp_Main)
        self.cbx_Gender.configure(values=('Male','Female','Others'))
        self.cbx_Gender.grid(column='1', row='0', sticky='e')
        self.cbx_Gender.configure(width='19')
        
        self.cbx_Hypertension = ttk.Combobox(self.tp_Main)
        self.cbx_Hypertension.configure(values=('True','False'))
        self.cbx_Hypertension.grid(column='1', row='2', sticky='e')
        self.cbx_Hypertension.configure(width='19')
        
        self.cbx_HeartDisease = ttk.Combobox(self.tp_Main)
        self.cbx_HeartDisease.configure(values=('True','False'))
        self.cbx_HeartDisease.grid(column='1', row='3', sticky='e')
        self.cbx_HeartDisease.configure(width='19')

        self.cbx_EverMarried = ttk.Combobox(self.tp_Main)
        self.cbx_EverMarried.configure(values=('Yes','No'))
        self.cbx_EverMarried.grid(column='1', row='4', sticky='e')
        self.cbx_EverMarried.configure(width='19')

        self.cbx_WorkType = ttk.Combobox(self.tp_Main)
        self.cbx_WorkType.configure(values=('Private','Never_worked','Govt_job','Self_employed','children'))
        self.cbx_WorkType.grid(column='1', row='5', sticky='e')
        self.cbx_WorkType.configure(width='19')

        self.cbx_ResidenceType = ttk.Combobox(self.tp_Main)
        self.cbx_ResidenceType.configure(values=('Urban','Rural'))
        self.cbx_ResidenceType.grid(column='1', row='6', sticky='e')
        self.cbx_ResidenceType.configure(width='19')

        self.cbx_SmokeStatus = ttk.Combobox(self.tp_Main)
        self.cbx_SmokeStatus.configure(values=('Smokes','Never_smoked','formerly_smoked','Unknown'))
        self.cbx_SmokeStatus.grid(column='1', row='9', sticky='e')
        self.cbx_SmokeStatus.configure(width='19')

        self.fld_GlucoseLevel = ttk.Entry(self.tp_Main)
        self.fld_GlucoseLevel.configure(width='22')
        self.fld_GlucoseLevel.grid(column='1', row='7', sticky='e')

        self.fld_BMI = ttk.Entry(self.tp_Main)
        self.fld_BMI.configure(width='22')
        self.fld_BMI.grid(column='1', row='8', sticky='e')

        self.fld_Age = ttk.Entry(self.tp_Main)
        self.fld_Age.configure(width='22')
        self.fld_Age.grid(column='1', row='1', sticky='e')

        self.btn_Submit = ttk.Button(self.tp_Main,command=self.buttonClick)
        self.btn_Submit.configure(text='Submit', width='39')
        self.btn_Submit.grid(column='0', columnspan='2', row='12')

        self.tp_Main.rowconfigure('14', pad='0')
        self.log_Results = tk.Text(self.tp_Main)
        self.log_Results.configure(height='10', width='34')
        _text_ = ""
        self.log_Results.insert('0.0', _text_)
        self.log_Results.grid(column='0', columnspan='2', row='15')
        self.label23 = tk.Label(self.tp_Main)
        self.label23.configure(font='TkTextFont', text='Developed by Lucas Schwengber and Roger Rothmund')
        self.label23.grid(column='0', columnspan='2', row='16')
        self.tp_Main.configure(height='500', width='800')

        # Main widget
        self.mainwindow = self.tp_Main
    

    def buttonClick(self):
        
        print('test',self.fld_Age.get())
        self.log_Results.delete('1.0',tk.END)
        self.log_Results.insert('0.0', "test")


    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = AppApp()
    app.run()


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