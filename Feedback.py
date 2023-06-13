#!/usr/bin/env python
# coding: utf-8

 


import Assist as AS
import detection as de
import Angles as ag
import cv2


 


def feedback(frame,angles,idx, level,EXS,EXSType_show,EXS_feedback,state_fed,tts_g,rec1,rec2):
    cntr=[]
    x=ag.dataset_angles(AS.Assist (level,EXS,EXSType_show[idx]))
    global s_g
    
    if EXS == "Biceps" :
        
        if(EXSType_show[idx]== "Biceps Beg"):        
            if(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) : 
                EXS_feedback[idx]=" Now Bring your,hands up!"

            elif(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)):   
                EXS_feedback[idx]=" Very Good ,Bring your ,hands down!"

            elif(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (not(angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) : 
                if angles[1] > int(x[2]+20) :
                    EXS_feedback[idx]="Bring your right, elbow close to ,your body"
                elif angles[1] < int(x[2]-20):
                    EXS_feedback[idx]="Keep your right, elbow away from ,your body a ,little"

            elif(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (not(angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20))) : 
                if angles[5] > int(x[10]+20) :
                    EXS_feedback[idx]="Bring your left, elbow close to, your body"
                elif angles[5] < int(x[10]-20):
                    EXS_feedback[idx]="Keep your left, elbow away from, your body a, little"

            elif(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (not(angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (not(angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20))) : 
                if angles[1] > int(x[2]+20) and angles[5] > int(x[10]+20) :
                    EXS_feedback[idx]="Bring your elbows, close to your, body"

                elif angles[1] < int(x[2]-20) and angles[5] < int(x[10]-20):
                    EXS_feedback[idx]="Keep your elbows, away from your, body a little"

            elif(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (not(angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)):   
                if angles[1] > int(x[3]+20) :
                    EXS_feedback[idx]="Bring your right, elbow close to, your body"
                elif angles[1] < int(x[3]-20):
                    EXS_feedback[idx]="Keep your right, elbow away from ,your body a little"

            elif(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (not(angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20))):   
                if angles[5] > int(x[11]+20) :
                    EXS_feedback[idx]="Bring your left, elbow close to, your body"
                elif angles[5] < int(x[11]-20):
                    EXS_feedback[idx]="Keep your left ,elbow away from ,your body a little"

            elif(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (not(angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (not(angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20))):   
                if angles[1] > int(x[3]+20) and angles[5] > int(x[11]+20):
                    EXS_feedback[idx]="Bring your elbows, close to your ,body"
                elif angles[1] < int(x[3]-20)and angles[5] < int(x[11]-20):
                    EXS_feedback[idx]="Keep your elbows ,away from your ,body a little"
                    
                    
        if (EXSType_show[idx] == "Biceps Int"):
            if (angles[1] > x[2]+20 ):
                EXS_feedback[idx]="Bring your right elbow close to your body"
            elif (angles[1] < x[2]-20 ):
                EXS_feedback[idx]="move your right elbow slightly away from your body"
                
            elif(angles[0] <= int(x[0]+10) and angles[0] >= int(x[0]-10))and (angles[1] >= int(x[2]-10) and angles[1] <= int(x[2]+10))  and (angles[4] <= int(x[8]+10) and angles[4] >= int(x[8]-10))  and (angles[5] >= int(x[10]-10) and angles[5] <= int(x[10]+10)) :   
                EXS_feedback[idx]=" Very Good , go Up !"
                
            elif(angles[0] <= int(x[1]+10) and angles[0] >= int(x[1]-10))and (angles[1] <= int(x[3]+10) and angles[1] >= int(x[3]-10))  and (angles[4] <= int(x[9]+10) and angles[4] >= int(x[9]-10))and (angles[5] <= int(x[11]+10) and angles[5] >= int(x[11]-10)):   
                 EXS_feedback[idx]=" Go Down !" 
        
                        
        
        if EXSType_show[idx] == "Biceps Adv" :

            if(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) : 
                EXS_feedback[idx]=" Now Bring your hands up!"

            elif(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)):   

                EXS_feedback[idx]=" Very Good ,Bring your hands down!"

            elif(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (not(angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) : 

                if angles[1] > int(x[2]+20) :
                    EXS_feedback[idx]="Bring your right elbow close to your body"
                elif angles[1] < int(x[2]-20):
                    EXS_feedback[idx]="Keep your right elbow away from your body a little"

            elif(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (not(angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20))) : 

                if angles[5] > int(x[10]+20) :
                    EXS_feedback[idx]="Bring your left elbow close to your body"
                elif angles[5] < int(x[10]-20):
                    EXS_feedback[idx]="Keep your left elbow away from your body a little"

            elif(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (not(angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (not(angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20))) : 

                if angles[1] > int(x[2]+20) and angles[5] > int(x[10]+20) :
                    EXS_feedback[idx]="Bring your elbows close to your body"

                elif angles[1] < int(x[2]-20) and angles[5] < int(x[10]-20):
                    EXS_feedback[idx]="Keep your elbows away from your body a little"

            elif(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (not(angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)):   
                if angles[1] > int(x[3]+20) :
                    EXS_feedback[idx]="Bring your right elbow close to your body"
                elif angles[1] < int(x[3]-20):
                    EXS_feedback[idx]="Keep your right elbow away from your body a little"

            elif(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (not(angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20))):   
                if angles[5] > int(x[11]+20) :
                    EXS_feedback[idx]="Bring your left elbow close to your body"
                elif angles[5] < int(x[11]-20):
                    EXS_feedback[idx]="Keep your left elbow away from your body a little"

            elif(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (not(angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (not(angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20))):   
                if angles[1] > int(x[3]+20) and angles[5] > int(x[11]+20):
                    EXS_feedback[idx]="Bring your elbows close to your body"
                elif angles[1] < int(x[3]-20)and angles[5] < int(x[11]-20):
                    EXS_feedback[idx]="Keep your elbows away from your body a little"
                    
        
        
                    
                    
    if EXS == "Shoulder" :
        if(EXSType_show[idx]== "Elbow Beg"):
                
            if(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) :
                EXS_feedback[idx]="very good ! ,try to Make ,your arms straight"
                state_fed[idx] = "Down"

            elif(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)) :                     
                EXS_feedback[idx]="now!Go down, and make your,both hand at,the same line"
                state_fed[idx] = "UP"

            elif (angles[0] > int(x[0]+20)) and (not(angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20))  :
                EXS_feedback[idx]="bring your right,elbow up"

            elif angles[4] > int(x[8]+20) and (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (not(angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20))):
                EXS_feedback[idx]="bring your left,elbow up"

            elif (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (not(angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) :

                if angles[1] > int(x[2]+20) :
                    EXS_feedback[idx]="Bring your right,elbow close to,your body"
                elif angles[1] < int(x[2]-20):
                    EXS_feedback[idx]="Keep your right,elbow away from,your body a,little"

            elif (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (not(angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20))) :

                if angles[5] > int(x[10]+20) :
                    EXS_feedback[idx]="Bring your left,elbow close to,your body"
                elif angles[5] < int(x[10]-20):
                    EXS_feedback[idx]="Keep your left,elbow away from,your body a little"

            elif (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (not(angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (not(angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20))) :

                if angles[1] > int(x[2]+20) and angles[5] > int(x[10]+20) :
                    EXS_feedback[idx]="bring your elbows,close to your,body"

                elif angles[1] < int(x[2]-20) and angles[5] < int(x[10]-20):
                    EXS_feedback[idx]="Keep your elbows,away from your, bodya little"    

            elif(not(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20)))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)) :                     
                if angles[0] > int(x[1]+20):
                    EXS_feedback[idx]="Bend your right,arm slightly"
                elif angles[0] < int(x[1]-20):
                    EXS_feedback[idx]="make your right,arm straight,slightly"

            elif(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (not(angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20)))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)) :                     
                if angles[4] > int(x[9]+20):
                    EXS_feedback[idx]="Bend your left,arm slightly"
                elif angles[4] < int(x[9]-20):
                    EXS_feedback[idx]="make your left,arm straight,slightly"

            elif(not(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20)))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (not(angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20)))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)) :                     
                if angles[4] > int(x[9]+20) and  angles[0] > int(x[1]+20):
                    EXS_feedback[idx]="Bend your two ,arms slightly"
                if angles[4] < int(x[9]-20) and  angles[0] < int(x[1]-20):
                    EXS_feedback[idx]="Make your two ,arms straight,slightly"    
                        
    
        
        if(EXSType_show[idx]== "Elbow Int"):

            if(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20)) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) :
                    EXS_feedback[idx]=" Very Good , go Up !"

            elif(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)):            
                    EXS_feedback[idx]=" Now , go Down !"

            elif(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (not(angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20)) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) :
                    if angles[1] > int(x[2]+20) :
                        EXS_feedback[idx]="Bring your right elbow close to your body"
                    elif angles[1] < int(x[2]-20):
                         EXS_feedback[idx]="Keep your right elbow away from your body a little"

            elif(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20)) and (not(angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20))) :
                    if angles[5] > int(x[10]+20) :
                        EXS_feedback[idx]="Bring your left elbow close to your body"
                    elif angles[5] < int(x[10]-20):
                         EXS_feedback[idx]="Keep your left elbow away from your body a little"

            elif(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (not(angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20)) and (not(angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20))) :
                    if angles[1] > int(x[2]+20) and angles[5] > int(x[10]+20) :
                        EXS_feedback[idx]="Bring your elbows close to your body"
                    elif angles[1] < int(x[2]-20) and angles[5] < int(x[10]-20):
                         EXS_feedback[idx]="Keep your elbows away from your body a little"

            elif(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (not(angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (not(angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20))):            
                    if angles[1] > int(x[3]+20) and angles[5] > int(x[11]+20) :
                        EXS_feedback[idx]="Keep your two elbows apart "
                    elif angles[1] < int(x[3]-20) and angles[5] < int(x[11]-20):
                         EXS_feedback[idx]="try to Make your arms straight "

            elif(not(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20)))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (not(angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20)))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)):            
                    if angles[0] < int(x[1]-20) and angles[4] < int(x[9]-20):
                         EXS_feedback[idx]="try to make your arms straight " 
                                
     
    
    
    
                    
    if EXS == "Quad" :
        if(EXSType_show[idx]== "Split Squat Contralateral Load"):
            if (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)) and (angles[2] >= int(x[4]-20) and angles[2] <= int(x[4]+20)) and (angles[3] >= int(x[6]-20) and angles[3] <= int(x[6]+20)) and (angles[4] >= int(x[8]-20) and angles[4] <= int(x[8]+20)) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) and (angles[6] >= int(x[12]-20) and angles[6] <= int(x[12]+20)) and (angles[7] >= int(x[14]-20) and angles[7] <= int(x[14]+20)):   
                EXS_feedback[idx]=" Now , go Up !"

            elif (angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20) ) and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)) and (angles[2] <= int(x[5]+20) and angles[2] >= int(x[5]-20)) and (angles[3] <= int(x[7]+20) and angles[3] >= int(x[7]-20)) and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20)) and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20) )and (angles[6] <= int(x[13]+20) and angles[6] >= int(x[13]-20)) and (angles[7] <= int(x[15]+20) and angles[7] >= int(x[15]-20)):   
                EXS_feedback[idx]="Right, Go Down !"   

            elif (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)) and (angles[2] >= int(x[4]-20) and angles[2] <= int(x[4]+20)) and (not(angles[3] >= int(x[6]-20) and angles[3] <= int(x[6]+20))) and (angles[4] >= int(x[8]-20) and angles[4] <= int(x[8]+20)) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) and (angles[6] >= int(x[12]-20) and angles[6] <= int(x[12]+20)) and (angles[7] >= int(x[14]-20) and angles[7] <= int(x[14]+20)):    
                if angles[3] > int(x[6]+20):
                    EXS_feedback[idx]=" try to bend your right knee slightly!"
                elif angles[3] < int(x[6]-20):
                    EXS_feedback[idx]=" try to make your right knee at a90-degree angle!" 

            elif (angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20) ) and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)) and (angles[2] <= int(x[5]+20) and angles[2] >= int(x[5]-20)) and (angles[3] <= int(x[7]+20) and angles[3] >= int(x[7]-20)) and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20)) and (not(angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)))and (angles[6] <= int(x[13]+20) and angles[6] >= int(x[13]-20)) and (angles[7] <= int(x[15]+20) and angles[7] >= int(x[15]-20)):   
                if angles[5] > int(x[11]+20):
                    EXS_feedback[idx]=" Bring your left elbow close to your body!"
                if angles[5] < int(x[11]-20):
                    EXS_feedback[idx]=" Keep your left elbow away from your body a little"

            elif (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)) and (angles[2] >= int(x[4]-20) and angles[2] <= int(x[4]+20)) and (angles[3] >= int(x[6]-20) and angles[3] <= int(x[6]+20)) and (angles[4] >= int(x[8]-20) and angles[4] <= int(x[8]+20)) and (not(angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20))) and (angles[6] >= int(x[12]-20) and angles[6] <= int(x[12]+20)) and (angles[7] >= int(x[14]-20) and angles[7] <= int(x[14]+20)):    
                if angles[5] > int(x[10]+20):
                    EXS_feedback[idx]=" Bring your left elbow close to your body!"
                if angles[5] < int(x[10]-20):
                    EXS_feedback[idx]=" Keep your left elbow away from your body a little"
        
        
        if EXSType_show[idx] == "Dumbbell Reverse Lunge Intermediate":
            if (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)) and (angles[2] >= int(x[4]-20) and angles[2] <= int(x[4]+20)) and (angles[3] >= int(x[6]-20) and angles[3] <= int(x[6]+20)) and (angles[4] >= int(x[8]-20) and angles[4] <= int(x[8]+20)) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) and (angles[6] >= int(x[12]-20) and angles[6] <= int(x[12]+20)) and (angles[7] >= int(x[14]-20) and angles[7] <= int(x[14]+20)):    
                EXS_feedback[idx]=" Very Good , go Up !"
            elif (angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20) ) and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)) and (angles[2] <= int(x[5]+20) and angles[2] >= int(x[5]-20)) and (angles[3] <= int(x[7]+20) and angles[3] >= int(x[7]-20)) and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20)) and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20) )and (angles[6] <= int(x[13]+20) and angles[6] >= int(x[13]-20)) and (angles[7] <= int(x[15]+20) and angles[7] >= int(x[15]-20)):    
                EXS_feedback[idx]=" Go Down , Try to make your arms straight!" 
            elif (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)) and (angles[2] >= int(x[4]-20) and angles[2] <= int(x[4]+20)) and (angles[3] >= int(x[6]-20) and angles[3] <= int(x[6]+20)) and (angles[4] >= int(x[8]-20) and angles[4] <= int(x[8]+20)) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) and (angles[6] >= int(x[12]-20) and angles[6] <= int(x[12]+20)) and (not(angles[7] >= int(x[14]-20) and angles[7] <= int(x[14]+20))):    

                if angles[7] > int(x[14]+20):
                    EXS_feedback[idx]=" try to bend your left knee slightly!"
                elif angles[7] < int(x[14]-20):
                    EXS_feedback[idx]=" try to make your left knee at a90-degree angle!" 

            elif (not(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))) and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)) and (angles[2] >= int(x[4]-20) and angles[2] <= int(x[4]+20)) and (angles[3] >= int(x[6]-20) and angles[3] <= int(x[6]+20)) and (angles[4] >= int(x[8]-20) and angles[4] <= int(x[8]+20)) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) and (angles[6] >= int(x[12]-20) and angles[6] <= int(x[12]+20)) and (angles[7] >= int(x[14]-20) and angles[7] <= int(x[14]+20)):    
                if angles[0] < int(x[0]-20):
                    EXS_feedback[idx]=" Try to make your right arm straight!"

            elif (not(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))) and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)) and (angles[2] <= int(x[5]+20) and angles[2] >= int(x[5]-20)) and (angles[3] <= int(x[7]+20) and angles[3] >= int(x[7]-20)) and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20)) and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20) )and (angles[6] <= int(x[13]+20) and angles[6] >= int(x[13]-20)) and (angles[7] <= int(x[15]+20) and angles[7] >= int(x[15]-20)):    
                 if angles[0] < int(x[1]-20):
                    EXS_feedback[idx]=" Try to make your right arm straight!"

            elif (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)) and (angles[2] >= int(x[4]-20) and angles[2] <= int(x[4]+20)) and (angles[3] >= int(x[6]-20) and angles[3] <= int(x[6]+20)) and (not(angles[4] >= int(x[8]-20) and angles[4] <= int(x[8]+20))) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) and (angles[6] >= int(x[12]-20) and angles[6] <= int(x[12]+20)) and (angles[7] >= int(x[14]-20) and angles[7] <= int(x[14]+20)):    
                if angles[4] < int(x[8]-20):
                    EXS_feedback[idx]=" Try to make your left arm straight!"

            elif (angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20) ) and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)) and (angles[2] <= int(x[5]+20) and angles[2] >= int(x[5]-20)) and (angles[3] <= int(x[7]+20) and angles[3] >= int(x[7]-20)) and (not(angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))) and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20) )and (angles[6] <= int(x[13]+20) and angles[6] >= int(x[13]-20)) and (angles[7] <= int(x[15]+20) and angles[7] >= int(x[15]-20)):    
                if angles[4] < int(x[9]-20):
                    EXS_feedback[idx]=" Try to make your left arm straight!"

            elif (angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20) ) and (not(angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))) and (angles[2] <= int(x[5]+20) and angles[2] >= int(x[5]-20)) and (angles[3] <= int(x[7]+20) and angles[3] >= int(x[7]-20)) and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20)) and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20) )and (angles[6] <= int(x[13]+20) and angles[6] >= int(x[13]-20)) and (angles[7] <= int(x[15]+20) and angles[7] >= int(x[15]-20)):    
                if angles[1] > int(x[3]+20):
                    EXS_feedback[idx]=" Bring your right elbow close to your body!"

            elif (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (not(angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))) and (angles[2] >= int(x[4]-20) and angles[2] <= int(x[4]+20)) and (angles[3] >= int(x[6]-20) and angles[3] <= int(x[6]+20)) and (angles[4] >= int(x[8]-20) and angles[4] <= int(x[8]+20)) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) and (angles[6] >= int(x[12]-20) and angles[6] <= int(x[12]+20)) and (angles[7] >= int(x[14]-20) and angles[7] <= int(x[14]+20)):    
                if angles[1] > int(x[2]+20):
                    EXS_feedback[idx]=" Bring your right elbow close to your body!"
                    
                    
        if(EXSType_show[idx]== "Prisoner Squat"):
            if angles[0] <= int(x[0]+40) and angles[1] <= int(x[2]+40) and angles[1] >=100 and angles[2] <= int(x[4]+40) and angles[3] <= int(x[6]+40) and angles[4] <= int(x[8]+40) and angles[5] <= int(x[10]+40) and angles[5] >=100 and angles[6] <= int(x[12]+40) and angles[7] <= int(x[14]+40) :
                EXS_feedback[idx]=" Very Good , go Up !"

            if angles[0] >= int(x[1]-40) and angles[1] >= int(x[3]-40) and angles[1] >=100 and  angles[2] >= int(x[5]-40) and angles[3] >= int(x[7]-40) and angles[4] >= int(x[9]-40) and angles[5] >= int(x[11]-40) and angles[5] >=100 and angles[6] >= int(x[13]-40) and angles[7] >= int(x[15]-40) :
                EXS_feedback[idx]=" Go Down !"
                    
     
    
                    
                    
    
    if(EXS=="Hamstring"):
        if(EXSType_show[idx]== "Kettlebell Swing"):
            if angles[0] <= int(x[0]+10):
                EXS_feedback[idx]="straight your right arm"  
                        
            elif angles[4] <= int(x[8]+10):
                EXS_feedback[idx]="straight your right arm"         

            elif (angles[1] >= int(x[2]-30) and angles[1] <= int(x[2]+30)) and (angles[2] < int(x[4]-30) or angles[6] < int(x[12]-30)) and (angles[3] >= int(x[6]-30) and angles[3] <= int(x[6]+30)) and (angles[5] >= int(x[10]-30) and angles[5] <= int(x[10]+30)) and (angles[6] >= int(x[12]-30) and angles[6] <= int(x[12]+30)) and (angles[7] >= int(x[14]-30) and angles[7] <= int(x[14]+30)):
                  EXS_feedback[idx]="straight your back"       

            elif (angles[1] >= int(x[2]-30) and angles[1] <= int(x[2]+30)) and angles[3] < int(x[6]-30) and (angles[5] >= int(x[10]-30) and angles[5] <= int(x[10]+30)) and (angles[7] >= int(x[14]-30) and angles[7] <= int(x[14]+30)):
                EXS_feedback[idx]="straight your right leg"         

            elif (angles[1] >= int(x[2]-30) and angles[1] <= int(x[2]+30)) and (angles[5] >= int(x[10]-30) and angles[5] <= int(x[10]+30)) and angles[7] < int(x[14]-30):
                EXS_feedback[idx]="straight your left leg" 
                    
                
                    
        
   #Determine the type of feedback(audio / text)               
    if EXS_feedback[idx] != None :     
        if(tts_g !=2):
            tts_g.SetVolume(50)
            s=str(idx)+" "+str(EXS_feedback[idx])
            try:
                if s_g != s:
                    tts_g.Speak(s,1)
                    s_g = s
            except NameError:s_g=""
            
        else:
            if len(rec1) !=0:
                rect = cv2.rectangle(frame,(int(rec1[0]-60),int(rec1[1]-150)), (int(rec2[0]+110),int(rec2[1]-150)),(105,105,105),-1)
                text =str(EXS_feedback[idx])
                for i, line in enumerate(text.split(',')):
                    cv2.putText(rect,line,  (int(rec1[0]-50),int(rec1[1]-135+i*17)), cv2.LINE_AA , .7, (255,255,255), 1,cv2.LINE_AA ) 

