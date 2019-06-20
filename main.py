try:
    from vrep import vrep
    from vrep import vrepConst
except:
    print ('--------------------------------------------------------------')
    print ('"vrep.py" could not be imported. This means very probably that')
    print ('either "vrep.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "vrep.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time

print ('Program started')
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP

if clientID!=-1:
    print ('Connected to remote API server')
else:
    print ('Failed connecting to remote API server')
print ('Program ended')
#vrep.sim_object_shape_type
#vrep.simx_opmode_oneshot
#simxGetObjectHandle
errorCode, carro = vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx', vrep.simx_opmode_oneshot_wait)
errorCode, left_Motor = vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor', vrep.simx_opmode_oneshot_wait)
errorCode, right_Motor = vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor', vrep.simx_opmode_oneshot_wait)
errorCode, sensor1 = vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor1', vrep.simx_opmode_oneshot_wait)
errorCode, cam1 = vrep.simxGetObjectHandle(clientID,'cam2', vrep.simx_opmode_oneshot_wait)
#
#vrep.simxReadProximitySensor
returnCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_streaming)
time.sleep(1)
returnCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
#returnCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_streaming)
print returnCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector
#
vrep.simxSetJointTargetVelocity(clientID,left_Motor,0, vrep.simx_opmode_streaming)
##time.sleep(5)
vrep.simxSetJointTargetVelocity(clientID,right_Motor,0, vrep.simx_opmode_streaming)
##vrep.simxGetCollectionHandle() (clientID,'Pioneer_p3dx',vrep.simxServiceCall())

a = vrep.simxGetObjects(clientID,vrep.sim_handle_all,vrep.simx_opmode_oneshot_wait)
#print a
#vrep.simxGetVisionSensorImage(clientID,cam1,,simx_opmode_streaming)
returnCode,resolution,image=vrep.simxGetVisionSensorImage(clientID,cam1,0,vrep.simx_opmode_streaming)
time.sleep(1)
returnCode,resolution,image=vrep.simxGetVisionSensorImage(clientID,cam1,0,vrep.simx_opmode_buffer)

import numpy as np
from matplotlib import pyplot as plt

im = np.array(image,dtype=np.uint8)

im.resize([resolution[0], resolution[1],3])
print im.shape
plt.imshow(im, origin='lower')
#for i in range(0,len(a)):
#    returnCode, childObjectHandle=vrep.simxGetObjectChild(clientID,carro,i,vrep.simx_opmode_blocking)
#    print childObjectHandle

#print vrep.simxGetObjects(clientID,vrep.sim_object_joint_type ,vrep.simx_opmode_oneshot_wait)
#print vrep.simxGetObjectName()
#vrep.simxGetObjectsInTree(vrep.sim.handle_scen)
print sensor1, carro, childObjectHandle
print carro, left_Motor, right_Motor, cam1
