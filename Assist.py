#!/usr/bin/env python
# coding: utf-8



import cv2
import numpy as np
import pandas as pd




def QuadEXS (EXSType) :
            fr=0
            lr=0
            quadList = []
            
            #Intermediate
            if(EXSType == "Dumbbell Reverse Lunge Intermediate") :
                fr = 4685
                lr = 5175
                
            #Advanced   
            if(EXSType=="Prisoner Squat") :
                fr = 2025
                lr = 2715
                
            #Beginner
            if(EXSType=="Split Squat Contralateral Load" ) :
                fr = 2715
                lr = 3105

                
            quadList.append(fr)
            quadList.append(lr)
            return quadList


 


def HamstringEXS (EXSType) :
            fr=0
            lr=0
            hamstringList = []
            
            #Intermediate
            if(EXSType == "Conventional Deadlift Intermediate") :
                fr = 2986
                lr = 3655

                
            #Advanced    
            if(EXSType == "Single Leg Deadlift 1 Dumbbell  Advanced") :
                fr = 5719
                lr = 5990
            
                
            #Beginner
            if(EXSType=="Kettlebell Swing") :
                fr = 629 
                lr = 949
            
            hamstringList.append(fr)
            hamstringList.append(lr)
            return hamstringList


 


def TricepsEXS (EXSType) :
            fr=0
            lr=0
            tricepsList = []
                
            #Advanced  
            if(EXSType=="Standing-Overhead-Dumbbell-Tricep-adv") :
                fr = 646
                lr = 1128
                
            tricepsList.append(fr)
            tricepsList.append(lr)
            return tricepsList


 


def ShoulderEXS (EXSType) :
            fr=0
            lr=0
            shoulderList = []
            
            #Intermediate
            if(EXSType == "Elbow Int") :
                fr = 289
                lr = 578

            
                
            #Advanced   
            if(EXSType=="Elbow Adv") :
                fr = 578
                lr = 870
            
                
            #Beginner    
            
            if(EXSType=="Elbow Beg") :
                fr =  0
                lr = 289
                
            shoulderList.append(fr)
            shoulderList.append(lr)
            return shoulderList


 


def BicepsEXS (EXSType) :
            fr=0
            lr=0
            bicepsList = []
               
            #Beginner    
            
            if(EXSType=="Biceps Beg") :
                fr =  0
                lr = 366
                            
            #Intermediate
            if(EXSType == "Biceps Int") :
                fr = 366
                lr = 665    
            #Advanced   
            if(EXSType=="Biceps Adv") :
                fr = 665
                lr = 1083

            bicepsList.append(fr)
            bicepsList.append(lr)
            return bicepsList


 


def Assist (level,EXS,EXSType) :
    tempData = None
    Row = []
    shoulderData = pd.read_csv(r"D:\yolo\yolov7\Elbow_yolo.csv")
    bicepsData = pd.read_csv(r"D:\yolo\yolov7\Biceps_yolo.csv")
    hamstringData = pd.read_csv(r"D:\yolo\yolov7\Hamstring _yolov7.csv") 
    quadData = pd.read_csv(r"D:\yolo\yolov7\Quad_yolov7.csv")



    if(level == "Intermediate") :
        
        if(EXS == "Shoulder") :
            tempData=shoulderData
            position = ShoulderEXS(EXSType)
            
        if(EXS == "Quad") :
            tempData=quadData
            position = QuadEXS(EXSType)
            
        if(EXS == "Hamstring") :
            tempData = hamstringData
            position = HamstringEXS(EXSType)
        
        if (EXS == "Triceps") :
            tempData = tricepsData
            position = TricepsEXS(EXSType)
            
        if (EXS == "Biceps") :
            tempData = bicepsData
            position = BicepsEXS(EXSType)
            
        dataFrame =tempData.iloc[position[0]:position[1],1:] 

        MaxLP = dataFrame.loc[dataFrame['y10'] == dataFrame.y10.max()]
        MaxLP = MaxLP.head(1)
        MinLP = dataFrame.loc[dataFrame['y10'] == dataFrame.y10.min()]
        MinLP = MinLP.head(1)
        MaxRP = dataFrame.loc[dataFrame['y11'] == dataFrame.y11.max()]
        MaxRP = MaxRP.head(1)
        MinRP = dataFrame.loc[dataFrame['y11'] == dataFrame.y11.min()]
        MinRP = MinRP.head(1)
 
    if(level == "Advanced") :
        
        if(EXS == "Shoulder") :
            tempData=shoulderData
            position = ShoulderEXS(EXSType)
            
        if(EXS == "Quad") :
            tempData=quadData
            position = QuadEXS(EXSType)

        if(EXS == "Hamstring") :
            tempData = hamstringData
            position = HamstringEXS(EXSType)

        if (EXS == "Triceps") :
            tempData = tricepsData
            position = TricepsEXS(EXSType)
       
        if (EXS == "Biceps") :
            tempData = bicepsData
            position = BicepsEXS(EXSType)
            
        dataFrame = tempData.iloc[position[0]:position[1],1:] 
        
        if(EXS ==  "Shoulder" or EXS == "Hamstring") :
            MaxLP = dataFrame.loc[dataFrame['y6'] == dataFrame.y6.max()]
            MaxLP = MaxLP.head(1)
            MinLP = dataFrame.loc[dataFrame['y6'] == dataFrame.y6.min()]
            MinLP = MinLP.head(1)
            MaxRP = dataFrame.loc[dataFrame['y7'] == dataFrame.y7.max()]
            MaxRP = MaxRP.head(1)
            MinRP = dataFrame.loc[dataFrame['y7'] == dataFrame.y7.min()] 
            MinRP = MinRP.head(1)
        
            
        else:
            MaxLP = dataFrame.loc[dataFrame['y10'] == dataFrame.y10.max()]
            MaxLP = MaxLP.head(1)
            MinLP = dataFrame.loc[dataFrame['y10'] == dataFrame.y10.min()]
            MinLP = MinLP.head(1)
            MaxRP = dataFrame.loc[dataFrame['y11'] == dataFrame.y11.max()]
            MaxRP = MaxRP.head(1)
            MinRP = dataFrame.loc[dataFrame['y11'] == dataFrame.y11.min()]
            MinRP = MinRP.head(1)
            
        
        
    if(level == "Beginner") :
        
        if(EXS == "Shoulder") :
            tempData=shoulderData
            position = ShoulderEXS(EXSType)
            
        if(EXS == "Quad") :
            tempData=quadData
            position = QuadEXS(EXSType) 

        if(EXS == "Hamstring") :
            tempData = hamstringData
            position = HamstringEXS(EXSType)
            
            
        if (EXS == "Ticeps") :
            tempData = tricepsData
            position = TicepsEXS(EXSType)
            
        if (EXS == "Biceps") :
            tempData = bicepsData
            position = BicepsEXS(EXSType)
            
        dataFrame =tempData.iloc[position[0]:position[1],1:] 
        
        MaxLP = dataFrame.loc[dataFrame['y10'] == dataFrame.y10.max()]
        MaxLP = MaxLP.head(1)
        MinLP = dataFrame.loc[dataFrame['y10'] == dataFrame.y10.min()]
        MinLP = MinLP.head(1)
        MaxRP = dataFrame.loc[dataFrame['y11'] == dataFrame.y11.max()]
        MaxRP = MaxRP.head(1)
        MinRP = dataFrame.loc[dataFrame['y11'] == dataFrame.y11.min()]
        MinRP = MinRP.head(1)
            
    Row.append(MaxLP)
    Row.append(MinLP)
    Row.append(MaxRP)
    Row.append(MinRP)
        
        
    return Row

