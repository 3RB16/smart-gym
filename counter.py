#!/usr/bin/env python
# coding: utf-8

 


import Assist as AS
import Angles as ag
import cv2


 


def counter(frame,angles,idx,level,EXS,EXSType_show,cnt,state,tts_g,rec1,rec2):
    cntr=[]
    x=ag.dataset_angles(AS.Assist (level,EXS,EXSType_show[idx]))
    
    if(EXSType_show[idx]== "Biceps Beg"):                
        if(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) : 
            state[idx] = "down" 
    
        if(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20))and state[idx]=="down":   
            cnt[idx] = cnt[idx]+1
            state[idx] = "up" 
       
            
    if(EXSType_show[idx]== "Biceps Int"):        
        if(angles[0] <= int(x[0]+10) and angles[0] >= int(x[0]-10))and (angles[1] >= int(x[2]-10) and angles[1] <= int(x[2]+10))  and (angles[4] <= int(x[8]+10) and angles[4] >= int(x[8]-10))  and (angles[5] >= int(x[10]-10) and angles[5] <= int(x[10]+10)) :
            state[idx] = "down" 
                   
        elif(angles[0] <= int(x[1]+10) and angles[0] >= int(x[1]-10))and (angles[1] <= int(x[3]+10) and angles[1] >= int(x[3]-10))  and (angles[4] <= int(x[9]+10) and angles[4] >= int(x[9]-10))and (angles[5] <= int(x[11]+10) and angles[5] >= int(x[11]-10))and state[idx]=="down":
            cnt[idx] = cnt[idx]+1
            state[idx] = "up" 
            
            
    if(EXSType_show[idx]== "Biceps Adv"):        
        if(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) : 
            state[idx] = "down" 
                   
        if(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)) and state[idx] == "down" :   
            cnt[idx] = cnt[idx]+1
            state[idx] = "up" 
            
            
                        
    if(EXSType_show[idx]== "Elbow Beg"):
        if(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) :
            state[idx] = "down"         
            
        if(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)) and state[idx] == "down"   :                         
            cnt[idx] = cnt[idx]+1
            state[idx] = "up" 
            
            
    if(EXSType_show[idx]== "Elbow Int"):
        if(angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20))and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20))  and (angles[4] <= int(x[8]+20) and angles[4] >= int(x[8]-20))  and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) :
            state[idx] = "down"         
            
        if(angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20))and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20))  and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20))and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20)) and state[idx]=="down":
            cnt[idx] = cnt[idx]+1
            state[idx] = "up"
         
        
    if(EXSType_show[idx]== "Prisoner Squat"):
        if (angles[0] <= int(x[1]+40) and angles[0] >= int(x[1]-40) ) and (angles[1] <= int(x[3]+40) and angles[1] >= int(x[3]-40)) and (angles[2] <= int(x[5]+60) and angles[2] >= int(x[5]-60)) and (angles[3] <= int(x[7]+60) and angles[3] >= int(x[7]-60)) and (angles[4] <= int(x[9]+40) and angles[4] >= int(x[9]-40)) and (angles[5] <= int(x[11]+40) and angles[5] >= int(x[11]-40) )and (angles[6] <= int(x[13]+40) and angles[6] >= int(x[13]-40)) and (angles[7] <= int(x[15]+40) and angles[7] >= int(x[15]-40)):  
            state[idx] = "up" 
        
        elif (angles[0] <= int(x[0]+40) and angles[0] >= int(x[0]-40)) and (angles[1] >= int(x[2]-40) and angles[1] <= int(x[2]+40)) and (angles[2] >= int(x[4]-40) and angles[2] <= int(x[4]+40)) and (angles[3] >= int(x[6]-40) and angles[3] <= int(x[6]+40)) and (angles[4] >= int(x[8]-40) and angles[4] <= int(x[8]+40)) and (angles[5] >= int(x[10]-40) and angles[5] <= int(x[10]+40)) and (angles[6] >= int(x[12]-40) and angles[6] <= int(x[12]+40)) and (angles[7] >= int(x[14]-40) and angles[7] <= int(x[14]+40)) and state[idx] == "up": 
            cnt[idx] = cnt[idx]+1
            state[idx] = "down"         
        
        
    if(EXSType_show[idx]== "Split Squat Contralateral Load"):
        if (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)) and (angles[2] >= int(x[4]-20) and angles[2] <= int(x[4]+20)) and (angles[3] >= int(x[6]-20) and angles[3] <= int(x[6]+20)) and (angles[4] >= int(x[8]-20) and angles[4] <= int(x[8]+20)) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) and (angles[6] >= int(x[12]-20) and angles[6] <= int(x[12]+20)) and (angles[7] >= int(x[14]-20) and angles[7] <= int(x[14]+20)) and state[idx] == "up":   
            cnt[idx] = cnt[idx]+1
            state[idx] = "down" 

        if (angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20) ) and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)) and (angles[2] <= int(x[5]+20) and angles[2] >= int(x[5]-20)) and (angles[3] <= int(x[7]+20) and angles[3] >= int(x[7]-20)) and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20)) and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20) )and (angles[6] <= int(x[13]+20) and angles[6] >= int(x[13]-20)) and (angles[7] <= int(x[15]+20) and angles[7] >= int(x[15]-20)):   
              state[idx] = "up"    
          

    if (EXSType_show[idx]== "Dumbbell Reverse Lunge Intermediate"):
        if (angles[0] <= int(x[1]+20) and angles[0] >= int(x[1]-20) ) and (angles[1] <= int(x[3]+20) and angles[1] >= int(x[3]-20)) and (angles[2] <= int(x[5]+20) and angles[2] >= int(x[5]-20)) and (angles[3] <= int(x[7]+20) and angles[3] >= int(x[7]-20)) and (angles[4] <= int(x[9]+20) and angles[4] >= int(x[9]-20)) and (angles[5] <= int(x[11]+20) and angles[5] >= int(x[11]-20) )and (angles[6] <= int(x[13]+20) and angles[6] >= int(x[13]-20)) and (angles[7] <= int(x[15]+20) and angles[7] >= int(x[15]-20)):    
            state[idx] = "up" 
        
        if (angles[0] <= int(x[0]+20) and angles[0] >= int(x[0]-20)) and (angles[1] >= int(x[2]-20) and angles[1] <= int(x[2]+20)) and (angles[2] >= int(x[4]-20) and angles[2] <= int(x[4]+20)) and (angles[3] >= int(x[6]-20) and angles[3] <= int(x[6]+20)) and (angles[4] >= int(x[8]-20) and angles[4] <= int(x[8]+20)) and (angles[5] >= int(x[10]-20) and angles[5] <= int(x[10]+20)) and (angles[6] >= int(x[12]-20) and angles[6] <= int(x[12]+20)) and (angles[7] >= int(x[14]-20) and angles[7] <= int(x[14]+20))and state[idx] == "up" :    
            cnt[idx] = cnt[idx]+1
            state[idx] = "down" 
                


    if(EXSType_show[idx]== "Kettlebell Swing"):
        if (angles[0] <= int(x[0]+10) and angles[0] >= int(x[0]-10)) and (angles[1] >= int(x[2]-10) and angles[1] <= int(x[2]+10)) and (angles[2] >= int(x[4]-10) and angles[2] <= int(x[4]+10)) and (angles[3] >= int(x[6]-10) and angles[3] <= int(x[6]+10)) and (angles[4] >= int(x[8]-10) and angles[4] <= int(x[8]+10)) and (angles[5] >= int(x[10]-10) and angles[5] <= int(x[10]+10)) and (angles[6] >= int(x[12]-10) and angles[6] <= int(x[12]+10)) and (angles[7] >= int(x[14]-10) and angles[7] <= int(x[14]+10)):
            state[idx] = "down"
                 

        elif (angles[0] <= int(x[1]+10) and angles[0] >= int(x[1]-10) ) and (angles[1] <= int(x[3]+10) and angles[1] >= int(x[3]-10)) and (angles[2] <= int(x[5]+10) and angles[2] >= int(x[5]-10)) and (angles[3] <= int(x[7]+10) and angles[3] >= int(x[7]-10)) and (angles[4] <= int(x[9]+10) and angles[4] >= int(x[9]-10)) and (angles[5] <= int(x[11]+10) and angles[5] >= int(x[11]-10) )and (angles[6] <= int(x[13]+10) and angles[6] >= int(x[13]-10)) and (angles[7] <= int(x[15]+10) and angles[7] >= int(x[15]-10)) and state[idx] == "down":
            cnt[idx] = cnt[idx]+1
            state[idx] = "up"
            
            
            
    if cnt[idx] :
        if tts_g==2:       
            rect = cv2.rectangle(frame, (int(rec2[0]+120),int(rec2[1]-210)), (int(rec2[0]+190),int(rec2[1]-150)),(105,105,105) ,-1)
            pixelx = (int(rec2[0]+120)+int(rec2[0]+190))/2
            text=str(cnt[idx])+"\n"+str(state[idx])
            for i, line in enumerate(text.split('\n')):
                cv2.putText(rect,line, (int(pixelx)-i*20,int(rec2[1]-180)+i*20), cv2.LINE_AA , .7, (255,255,255), 1,cv2.LINE_AA )
        else:
            rect = cv2.rectangle(frame,(int(rec1[0]-60),int(rec1[1]-150)), (int(rec2[0]+40),int(rec2[1]-150)),(105,105,105),-1)
            text="Counter: "+str(cnt[idx])+"!"+"\n"+"State: "+str(state[idx])
            for i, line in enumerate(text.split('\n')):
                cv2.putText(rect,line, (int(rec1[0]-40),int(rec1[1]-110+i*30)), cv2.LINE_AA , .7, (255,255,255), 1,cv2.LINE_AA ) 

