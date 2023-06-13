#!/usr/bin/env python
# coding: utf-8

 


import Assist as AS
import Angles as ag
import cv2


 


def detection (frame,angles,idx,EXS, level, EXSType,EXSType_show,tts_g,rec1,rec2): 
    EXS_name = []
    x=ag.dataset_angles(AS.Assist (level,EXS,EXSType))
    
    if level == "Beginner" :

        if EXS == "Biceps" :
            if EXSType == "Biceps Beg" : 
                if(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) :
                    EXSType_show[idx] = EXSType
                
                if(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)):                     
                    EXSType_show[idx] = EXSType 
                    
                    
        if EXS == "Shoulder" :
            if EXSType == "Elbow Beg" :
                if(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) :
                    EXSType_show[idx] = EXSType
                
                if(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)):                     
                    EXSType_show[idx] = EXSType
                        
                    
        if EXS == "Quad" :            
            if EXSType == "Split Squat Contralateral Load":
                if (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)) and (angles[2] >= int(x[4]-20) and angles[2] <= int(x[4]+20)) and (angles[3] >= int(x[6]-20) and angles[3] <= int(x[6]+20)) and (angles[4] >= int(x[8]-20) and angles[4] <= int(x[8]+20)) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) and (angles[6] >= int(x[12]-20) and angles[6] <= int(x[12]+20)) and (angles[7] >= int(x[14]-20) and angles[7] <= int(x[14]+20)):   
                    EXSType_show[idx] = EXSType
                if (angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20) ) and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)) and (angles[2] <= int(x[5]+20) and angles[2] >= int(x[5]-20)) and (angles[3] <= int(x[7]+20) and angles[3] >= int(x[7]-20)) and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20)) and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20) )and (angles[6] <= int(x[13]+20) and angles[6] >= int(x[13]-20)) and (angles[7] <= int(x[15]+20) and angles[7] >= int(x[15]-20)):   
                    EXSType_show[idx] = EXSType
                    
                    
        if EXS == "Hamstring" :
            
             if EXSType == "Kettlebell Swing":
                    if (angles[0] <= int(x[0]+10) and angles[0] >= int(x[0]-10)) and (angles[1] >= int(x[2]-10) and angles[1] <= int(x[2]+10)) and (angles[2] >= int(x[4]-10) and angles[2] <= int(x[4]+10)) and (angles[3] >= int(x[6]-10) and angles[3] <= int(x[6]+10)) and (angles[4] >= int(x[8]-10) and angles[4] <= int(x[8]+10)) and (angles[5] >= int(x[10]-10) and angles[5] <= int(x[10]+10)) and (angles[6] >= int(x[12]-10) and angles[6] <= int(x[12]+10)) and (angles[7] >= int(x[14]-10) and angles[7] <= int(x[14]+10)):
                        EXSType_show[idx] = EXSType
            

                    elif (angles[0] <= int(x[1]+10) and angles[0] >= int(x[1]-10) ) and (angles[1] <= int(x[3]+10) and angles[1] >= int(x[3]-10)) and (angles[2] <= int(x[5]+10) and angles[2] >= int(x[5]-10)) and (angles[3] <= int(x[7]+10) and angles[3] >= int(x[7]-10)) and (angles[4] <= int(x[9]+10) and angles[4] >= int(x[9]-10)) and (angles[5] <= int(x[11]+10) and angles[5] >= int(x[11]-10) )and (angles[6] <= int(x[13]+10) and angles[6] >= int(x[13]-10)) and (angles[7] <= int(x[15]+10) and angles[7] >= int(x[15]-10)):
                        EXSType_show[idx] = EXSType

                           
                            

                    
    if level == "Intermediate" :
        if EXSType == "Biceps Int" :            
            if(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) :
                    EXSType_show[idx] = EXSType
                
            elif(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)):              
                    EXSType_show[idx] = EXSType
                    
                    
        if EXSType == "Elbow Int" :
            if(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20)) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) :
                    EXSType_show[idx] = EXSType
                
            if(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)):            
                    EXSType_show[idx] = EXSType
                    
                    
                
        if EXSType == "Dumbbell Reverse Lunge Intermediate":
            if (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)) and (angles[2] >= int(x[4]-20) and angles[2] <= int(x[4]+20)) and (angles[3] >= int(x[6]-20) and angles[3] <= int(x[6]+20)) and (angles[4] >= int(x[8]-20) and angles[4] <= int(x[8]+20)) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) and (angles[6] >= int(x[12]-20) and angles[6] <= int(x[12]+20)) and (angles[7] >= int(x[14]-20) and angles[7] <= int(x[14]+20)):    
                    EXSType_show[idx] = EXSType
                    
            if (angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20) ) and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)) and (angles[2] <= int(x[5]+20) and angles[2] >= int(x[5]-20)) and (angles[3] <= int(x[7]+20) and angles[3] >= int(x[7]-20)) and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20)) and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20) )and (angles[6] <= int(x[13]+20) and angles[6] >= int(x[13]-20)) and (angles[7] <= int(x[15]+20) and angles[7] >= int(x[15]-20)):    
                    EXSType_show[idx] = EXSType
                            
                                         
                                   
            

    if level == "Advanced" :
        if EXSType == "Biceps Adv" :
            if(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) : 
                    EXSType_show[idx] = EXSType
                
            if(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)):   
                    EXSType_show[idx] = EXSType  
                    
        if EXSType == "Prisoner Squat":
                if angles[0] <= int(x[0]+40) and angles[1] <= int(x[2]+40) and angles[1] >=100 and angles[2] <= int(x[4]+40) and angles[3] <= int(x[6]+40) and angles[4] <= int(x[8]+40) and angles[5] <= int(x[10]+40) and angles[5] >=100 and angles[6] <= int(x[12]+40) and angles[7] <= int(x[14]+40) :
                    EXSType_show[idx] = EXSType

                elif angles[0] >= int(x[1]-40) and angles[1] >= int(x[3]-40) and angles[1] >=100 and  angles[2] >= int(x[5]-40) and angles[3] >= int(x[7]-40) and angles[4] >= int(x[9]-40) and angles[5] >= int(x[11]-40) and angles[5] >=100 and angles[6] >= int(x[13]-40) and angles[7] >= int(x[15]-40) :
                     EXSType_show[idx] = EXSType
                        
                        
    
    
    if EXSType_show[idx] == None :
        rect = cv2.rectangle(frame, (int(rec1[0]-60),int(rec1[1]-200)), (int(rec2[0]+20),int(rec1[1]-150)),(255,255,255),-1)
        rect2 = cv2.rectangle(rect,(int(rec1[0]-60),int(rec1[1]-150)), (int(rec2[0]+110),int(rec2[1]-150)),(105,105,105))
        cv2.putText(rect2,'Not Detected !',(int(rec1[0]-50),int(rec1[1]-160)), cv2.LINE_AA , .7, (105,105,105), 1,cv2.LINE_AA )
        
    else :
        if tts_g ==2:
            rect = cv2.rectangle(frame, (int(rec1[0]-60),int(rec1[1]-200)), (int(rec2[0]+20),int(rec1[1]-150)),(255,255,255),-1)
            rect2 = cv2.rectangle(rect,(int(rec1[0]-60),int(rec1[1]-150)), (int(rec2[0]+110),int(rec2[1]-150)),(105,105,105))
            cv2.putText(rect2,EXSType_show[idx],(int(rec1[0]-40),int(rec1[1]-170)), cv2.LINE_AA , .7, (105,105,105), 1,cv2.LINE_AA ) 
        else:
            rect = cv2.rectangle(frame, (int(rec1[0]-60),int(rec1[1]-200)), (int(rec2[0]+20),int(rec1[1]-150)),(255,255,255),-1)
            rect2 = cv2.rectangle(rect,(int(rec1[0]-60),int(rec1[1]-150)), (int(rec2[0]+40),int(rec2[1]-150)),(105,105,105))
            cv2.putText(rect2,EXSType_show[idx],(int(rec1[0]-40),int(rec1[1]-170)), cv2.LINE_AA , .7, (105,105,105), 1,cv2.LINE_AA ) 
        

