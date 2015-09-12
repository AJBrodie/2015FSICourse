# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 15:07:44 2015

@author: andrew
"""
from numpy import *
from inflows import *

class outputLine():
    def __init__(self, outputFileName, nodeSet):
        
        self.outputFile = open(outputFileName,"w")
        self.outputFile.write("Line output v1.0 \n")

        self.nodeSet = nodeSet
        self.outputFile.write("Length: {} \n".format(len(nodeSet)))
        return
    
    def writeTimeStep(self,time):
        self.outputFile.write(str(time) + "\n")
        for node in self.nodeSet:
            self.outputFile.write("{} {} {}\n".format(node.GetSolutionStepValue("PRESSURE",0), node.GetSolutionStepValue("VELOCITY_X",0), node.GetSolutionStepValue("VELOCITY_Y",0)))
        return
            
    def closeFile(self):
        self.outputFile.close()
        return
        
class channelInput():
    def __init__(self,fileName):
        self.input_file = open(fileName,'r')
        return
    
    def readInput(self):
        if self.input_file:
            line = self.input_file.readline()
            #print(line)
            if line == 'EmptyChannelInputFile\n':
                for line in self.input_file:
                    if line.find("Mesh") != -1:
                        section = self.input_file.readline()
                        section = section.split()
                        
                        if len(section) > 1:
                            print('The mesh type section is not properly defined')
                            return
                        
                        if section[0] != 'Structured' and section[0] != 'Unstructured':
                            print('Unknown mesh type')
                            return
                        
                        self.meshType = section[0]
                            
                                                
                    elif line.find("Type") != -1:
                        section = self.input_file.readline()
                        section = section.split()
                        
                        if len(section) > 1:
                            print('The flow type section is not properly defined')
                            return
                            
                        self.inletType = section[0]
                          
                            
                    elif line.find("vRange") != -1:
                        section = self.input_file.readline()
                        section = section.split()
                        
                        if len(section) > 2:
                            print('The velocity range is not properly defined')
                            return
                        
                        vRange = zeros(len(section))
                        
                        for i in range(0,len(section)):
                            vRange[i] = section[i]
                            
                        self.vRange = vRange
                            
                    elif line.find("vMax") != -1:
                        section = self.input_file.readline()
                        section = section.split()
                        
                        vMax=zeros(len(section))
                        
                        if len(section) > 1:
                            print('The maximum velocity is not properly defined')
                            return
                        
                        vMax[0] = section[0]                        
                                                    
                        self.vMax = vMax[0]
                                                        
                            
                            
                    elif line.find("Period-Time") != -1:
                        section = self.input_file.readline()
                        section = section.split()
                        
                        T = zeros(len(section))                        
                        
                        for i in range(0,len(section)):
                            T[i] = section[i]
                            
                        self.T = T
                        
                    elif line.find("Period-Space") != -1:
                        section = self.input_file.readline()
                        section = section.split()
                        
                        X = zeros(len(section))                        
                        
                        for i in range(0,len(section)):
                            X[i] = section[i]
                            
                        self.X = X
                        
                    elif line.find("Spatial Velocity") != -1:
                        section = self.input_file.readline()
                        section = section.split()
                        
                        vSin=zeros(len(section))
                        
                        if len(section) > 1:
                            print('The Sin velocity is not properly defined')
                            return
                        
                        vSin[0] = section[0]                        
                                                    
                        self.vSin = vSin[0]
                            
            else:           
                print('This is not a suitable input file')
                
                            
    def readSection(self,line):
        
        if i != -1:
            return line[:i].split() 
        return line.split() 
        
