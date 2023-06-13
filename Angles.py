#!/usr/bin/env python
# coding: utf-8



import numpy as np
import cv2




def findAngle(frame,kpts,b):
    #angles points
    angle_points={'angle_1R':[6,8,10],'angle_2R':[8,6,12],'angle_3R':[6,12,14],'angle_4R':[12,14,16],
                  'angle_5L':[5,7,9],'angle_6L':[7,5,11],'angle_7L':[5,11,13], 'angle_8L':[11,13,15]}
    
    coord = []
    angles=[]
    #get x.y,c for each keypoint
    num_kpt = len(kpts)//3
    for i in range(num_kpt):
        cx,cy = kpts[3*i], kpts[3*i + 1]
        conf = kpts[3*i + 2]
        coord.append([i, cx, cy, conf])
    
    #calculate realtime angles->8
    for p in angle_points.values():
        x1,y1 = coord[p[0]][1:3]
        x2,y2 = coord[p[1]][1:3]
        x3,y3 = coord[p[2]][1:3]
        radians = np.arctan2(y3-y2,x3-x2) - np.arctan2(y1-y2, x1-x2)
        angle1 = np.abs(radians*180.0/np.pi)
        
        if angle1 >180.0:
            angle1 = 360-angle1
        
        #draw realtime angles
        cv2.putText(frame,str(int(angle1)), (int(x2),int(y2)),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)
        angles.append(int(angle1))
        
    return angles




def calculate_angle(a,b,c):
    a = np.array(a) 
    b = np.array(b) 
    c = np.array(c) 
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
    
    return angle




def dataset_angles(Row):
    x = []
                #Coordinates#
    handLMax = [Row[0].x10,Row[0].y10]
    handLMin = [Row[1].x10,Row[1].y10]
    handRMax = [Row[2].x11,Row[2].y11]
    handRMin = [Row[3].x11,Row[3].y11]

    elbowLMax = [Row[0].x8,Row[0].y8]
    elbowLMin = [Row[1].x8,Row[1].y8]
    elbowRMax = [Row[2].x9,Row[2].y9]
    elbowRMin = [Row[3].x9,Row[3].y9]

    shoulderLMax = [Row[0].x6,Row[0].y6]
    shoulderLMin = [Row[1].x6,Row[1].y6]
    shoulderRMax = [Row[2].x7,Row[2].y7]
    shoulderRMin = [Row[3].x7,Row[3].y7]

    hipLMax = [Row[0].x12,Row[0].y12]
    hipLMin = [Row[1].x12,Row[1].y12]
    hipRMax = [Row[2].x13,Row[2].y13]
    hipRMin = [Row[3].x13,Row[3].y13]

    kneeLMax = [Row[0].x14,Row[0].y14]
    kneeLMin = [Row[1].x14,Row[1].y14]
    kneeRMax = [Row[2].x15,Row[2].y15]
    kneeRMin = [Row[3].x15,Row[3].y15]

    footLMax = [Row[0].x16,Row[0].y16]
    footLMin = [Row[1].x16,Row[1].y16]
    footRMax = [Row[2].x17,Row[2].y17]
    footRMin = [Row[3].x17,Row[3].y17]

                    #Angles#
    elbowLMaxAngle = calculate_angle(handLMax , elbowLMax , shoulderLMax)
    elbowLMinAngle = calculate_angle(handLMin , elbowLMin , shoulderLMin)
    elbowRMaxAngle = calculate_angle(handRMax , elbowRMax , shoulderRMax)
    elbowRMinAngle = calculate_angle(handRMin , elbowRMin , shoulderRMin)

    shoulderLMaxAngle = calculate_angle(hipLMax , shoulderLMax , elbowLMax)
    shoulderLMinAngle = calculate_angle(hipLMin , shoulderLMin , elbowLMin)
    shoulderRMaxAngle = calculate_angle(hipRMax , shoulderRMax , elbowRMax)
    shoulderRMinAngle = calculate_angle(hipRMin , shoulderRMin , elbowRMin)

    hipLMaxAngle = calculate_angle(shoulderLMax , hipLMax , kneeLMax)
    hipLMinAngle = calculate_angle(shoulderLMin , hipLMin , kneeLMin)
    hipRMaxAngle = calculate_angle(shoulderRMax , hipRMax , kneeRMax)
    hipRMinAngle = calculate_angle(shoulderRMin , hipRMin , kneeRMin)

    kneeLMaxAngle = calculate_angle(hipLMax , kneeLMax , footLMax)
    kneeLMinAngle = calculate_angle(hipLMin , kneeLMin , footLMin)
    kneeRMaxAngle = calculate_angle(hipRMax , kneeRMax , footRMax)
    kneeRMinAngle = calculate_angle(hipRMin , kneeRMin , footRMin)

    Angles=[elbowLMaxAngle,elbowLMinAngle,elbowRMaxAngle,elbowRMinAngle,shoulderLMaxAngle,shoulderLMinAngle,shoulderRMaxAngle,shoulderRMinAngle,hipLMaxAngle,hipLMaxAngle,hipRMaxAngle,hipRMinAngle,kneeLMaxAngle,kneeLMinAngle,kneeRMaxAngle,kneeRMinAngle]

    x.append(elbowRMaxAngle)
    x.append(elbowRMinAngle)
    x.append(shoulderRMaxAngle)
    x.append(shoulderRMinAngle)
    x.append(hipRMaxAngle)
    x.append(hipRMinAngle)
    x.append(kneeRMaxAngle)
    x.append(kneeRMinAngle)
    
    x.append(elbowLMaxAngle)
    x.append(elbowLMinAngle)
    x.append(shoulderLMaxAngle)
    x.append(shoulderLMinAngle)
    x.append(hipLMaxAngle)
    x.append(hipLMinAngle)
    x.append(kneeLMaxAngle)
    x.append(kneeLMinAngle)
    
    return x

