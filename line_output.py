# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 15:07:44 2015

@author: andrew
"""

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