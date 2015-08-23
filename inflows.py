# -*- coding: utf-8 -*-
# > <
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
    def __init__(self, inletNodes, vRange, T):
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
        vMax = self.vRange[1]
        vMin = self.vRange[0]
        vAvg = (vMax + vMin)/2
        
        # Unit Frequency components
        f = 0
        for i in range(0,len(self.Period)):
            f = f + cos(t/self.Period[i]*2*pi)/len(self.Period)
            
        # Magnitude
        f = f * (vMax - vAvg) + vAvg
                
        for node in self.inletNodes:
            Y = node.coordinates[1]
                        
            # Unit Parabolic Base            
            NormalParabola = (Y-self.yMax)*(Y-self.yMin)/(self.yMin*self.yMax)
            
            # Compile            
            U = NormalParabola * f
            
            node.SetSolutionStepValue("VELOCITY_X", 0, U)
        
        return
        
class ConvolutedSinOnParabolicInletVelocity(InletVelocityFunc):
    def __init__(self, inletNodes, vRange, v_sin, X):
        self.inletNodes = inletNodes
        self.vRange = vRange
        self.v_sin = v_sin
        self.Period = X
        
        
        yMin = inletNodes[0].coordinates[1]
        yMax = yMin
        for node in self.inletNodes:
            if(node.coordinates[1] > yMax):
                yMax = node.coordinates[1]
            elif(node.coordinates[1] < yMin):
                yMin = node.coordinates[1]
                    
        
        self.yMax = yMax
        self.yMin = yMin
        
        self.inf1 = yMin
        self.dir1 = 1
        self.inf2 = yMax - self.Period
        self.dir2 = 0
        return
        
    def ApplyInletVelocity(self,t):
        vMax = self.vRange[1]
        vMin = self.vRange[0]
        vAvg = (vMax + vMin)/2
        
        # Track influence region
        # (Region1)
        if self.dir1 == 1:
            self.inf1 = self.inf1 + t*self.v_sin
        elif self.dir1 == 0:
            self.inf1 = self.inf1 - t*self.v_sin
            
        if self.inf1 < self.yMin:
            self.dir1 = 1
            self.inf1 = self.inf1 + 2*(self.yMin-self.inf1)
        elif self.inf1 + self.Period > self.yMax:
            self.dir1 = 0
            self.inf1 = self.inf1 - 2*((self.inf1 + self.Period) - self.yMax)
        # (Region2)
        if self.dir2 == 1:
            self.inf2 = self.inf2 + t*self.v_sin
        elif self.dir2 == 0:
            self.inf2 = self.inf2 - t*self.v_sin
            
        if self.inf2 < self.yMin:
            self.dir2 = 1
            self.inf2 = self.inf2 + 2*(self.yMin-self.inf2)
        elif self.inf2 + self.Period > self.yMax:
            self.dir2 = 0
            self.inf2 = self.inf2 - 2*((self.inf2 + self.Period) - self.yMax)
       
                
        for node in self.inletNodes:
            Y = node.coordinates[1]
                        
            # Unit Parabolic Base            
            NormalParabola = (Y-self.yMax)*(Y-self.yMin)/(self.yMin*self.yMax) * vAvg
            
            # Add sine if inside area of influence
            if Y >= self.inf1 and Y <= self.inf1 + self.Period :
                S1 = sin((Y-self.inf1)/self.Period*2*pi)
            else:
                S1 = 0
                
            if Y >= self.inf2 and Y <= self.inf2 + self.Period :
                S2 = -sin((Y-self.inf2)/self.Period*2*pi)
            else:
                S2 = 0
                
            S = (S1*S2)*(vMax-vAvg)
            
            U = NormalParabola + S
            
            node.SetSolutionStepValue("VELOCITY_X", 0, U)
        
        return
        
class AddedSinOnParabolicInletVelocity(InletVelocityFunc):
    def __init__(self, inletNodes, vRange, v_sin, X):
        self.inletNodes = inletNodes
        self.vRange = vRange
        self.v_sin = v_sin
        self.Period = X
        
        
        yMin = inletNodes[0].coordinates[1]
        yMax = yMin
        for node in self.inletNodes:
            if(node.coordinates[1] > yMax):
                yMax = node.coordinates[1]
            elif(node.coordinates[1] < yMin):
                yMin = node.coordinates[1]
                    
        
        self.yMax = yMax
        self.yMin = yMin
        
        self.inf1 = yMin
        self.dir1 = 1
        self.inf2 = yMax - self.Period
        self.dir2 = 0
        return
        
    def ApplyInletVelocity(self,t):
        vMax = self.vRange[1]
        vMin = self.vRange[0]
        vAvg = (vMax + vMin)/2
        
        # Track influence region
        # (Region1)
        if self.dir1 == 1:
            self.inf1 = self.inf1 + t*self.v_sin
        elif self.dir1 == 0:
            self.inf1 = self.inf1 - t*self.v_sin
            
        if self.inf1 < self.yMin:
            self.dir1 = 1
            self.inf1 = self.inf1 + 2*(self.yMin-self.inf1)
        elif self.inf1 + self.Period > self.yMax:
            self.dir1 = 0
            self.inf1 = self.inf1 - 2*((self.inf1 + self.Period) - self.yMax)
        # (Region2)
        if self.dir2 == 1:
            self.inf2 = self.inf2 + t*self.v_sin
        elif self.dir2 == 0:
            self.inf2 = self.inf2 - t*self.v_sin
            
        if self.inf2 < self.yMin:
            self.dir2 = 1
            self.inf2 = self.inf2 + 2*(self.yMin-self.inf2)
        elif self.inf2 + self.Period > self.yMax:
            self.dir2 = 0
            self.inf2 = self.inf2 - 2*((self.inf2 + self.Period) - self.yMax)
       
                
        for node in self.inletNodes:
            Y = node.coordinates[1]
                        
            # Unit Parabolic Base            
            NormalParabola = (Y-self.yMax)*(Y-self.yMin)/(self.yMin*self.yMax) * vAvg
            
            # Add sine if inside area of influence
            if Y >= self.inf1 and Y <= self.inf1 + self.Period:
                S1 = sin((Y-self.inf1)/self.Period*2*pi)
            else:
                S1 = 0
                
            if Y >= self.inf2 and Y <= self.inf2 + self.Period :
                S2 = -sin((Y-self.inf2)/self.Period*2*pi)
            else:
                S2 = 0
                
            S = (S1+S2)/2*(vMax-vAvg)
            
            U = NormalParabola + S
            
            node.SetSolutionStepValue("VELOCITY_X", 0, U)
        
        return
# Function for defining the inlet velocity
def GetNodes(model_part,dim,pos):
    NodeSet = []
    for node in model_part.NodeIterators():
        if(absolute(node.coordinates[dim]-pos)<1*10**-4):
            NodeSet.append(node)
    return NodeSet