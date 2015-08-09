# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 08:20:27 2015

@author: andrew
"""

from numpy import *

class InletVelocityFunc():
    def __init__(self):
        return
        
    def ApplyInletVelocity(self):
        return
        
class ParabolicInletVelocity(InletVelocityFunc):
    def __init__(self, inletNodes,vMax):
        self.inletNodes = inletNodes
        self.vMax = vMax
        
        yMin = inletNodes[0].coordinates[1]
        yMax = yMin
        for node in self.inletNodes:
            if(node.coordinates[1] > yMax):
                yMax = node.coordinates[1]
            elif(node.coordinates[1] < yMin):
                yMin = node.coordinates[1]
                    
        
        self.yMax = yMax
        self.yMin = yMin
        return
        
    def ApplyInletVelocity(self):      
        for node in self.inletNodes:
            #X = node.coordinates[0]
            Y = node.coordinates[1]
            #Z = node.coordinates[2]
            
            U = (Y-self.yMax)*(Y-self.yMin) * self.vMax/(self.yMin*self.yMax)
            
            node.SetSolutionStepValue(VELOCITY_X, 0, U)
        return
        
class OscillatingParabolicInletVelocity(InletVelocityFunc):
    def __init__(self,inletNodes,vRange,T):
        self.inletNodes = inletNodes
        self.vRange = vRange
        self.Period = T
        
        
        yMin = inletNodes[0].coordinates[1]
        yMax = yMin
        for node in self.inletNodes:
            if(node.coordinates[1] > yMax):
                yMax = node.coordinates[1]
            elif(node.coordinates[1] < yMin):
                yMin = node.coordinates[1]
                    
        
        self.yMax = yMax
        self.yMin = yMin
        return
        
    def ApplyInletVelocity(self,t):
                
        for node in self.inletNodes:
            Y = node.coordinates[1]
            vMax = self.vRange[1]
            vMin = self.vRange[0]            
            vAvg = (vMax + vMin)/2
            
            U = (Y-self.yMax)*(Y-self.yMin) * vAvg/(self.yMin*self.yMax) + (vMax-vAvg)*cos(t/self.Period*2*pi)
            
            node.SetSolutionStepValue("VELOCITY_X", 0, U)
        
        return
        
# Function for defining the inlet velocity
def GetNodes(model_part,dim,pos):
    NodeSet = []
    for node in model_part.NodeIterators():
        if(absolute(node.coordinates[dim]-pos)<1*10**-4):
            NodeSet.append(node)
    return NodeSet