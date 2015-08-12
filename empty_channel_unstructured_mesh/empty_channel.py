from __future__ import print_function, absolute_import, division 
import sys
import timeit

sys.path.append("..")
print(sys.path)

from numpy import *
from pyKratos import *

from inflows import *
from line_output import *

#this i a modified copy of the stokes testcase to test the first prototype of the navier stokes element (steady) 

#messure runtime
start = timeit.default_timer()

# add variables to be allocated from the list in variables.py
solution_step_variables = [
    VELOCITY_X,
    VELOCITY_Y,
    ACCELERATION_X,
    ACCELERATION_Y,
    PRESSURE,
    IS_LAGRANGIAN,
    EXTERNAL_FORCE_X,
    EXTERNAL_FORCE_Y,
    IS_STRUCTURE
]

property_list = {
    0: {VISCOSITY: 1.5e-5,
        DENSITY: 1.0,
        BODY_FORCE_X: 0.0,
        BODY_FORCE_Y: 0.0,
        }
}

#create buffer size and model part
buffer_size = 2  # store current step and 1 in the past
model_part = ModelPart(buffer_size, solution_step_variables)
model_part.AddProperties(property_list)

#read in geometry from input - nodes and elements
input_file = "01_empty_channelFluid.mdpa"
#input_file = "triangle_testFluid.mdpa"
output_file = "01_empty_channelFluid.OUT"
dragLiftFile= "dragLift.txt"

#initialize GiDIO object
from pyKratos import gid_io_navier_stokes
gid_io_input = gid_io_navier_stokes.GidIONS(input_file, output_file)
#read model from mdpa file
gid_io_input.ReadModelPart(model_part)


import bossak_scheme
alphaBossak = -0.3;
time_scheme = bossak_scheme.BossakScheme(model_part, alphaBossak)


builder_and_solver = builder_and_solver.BuilderAndSolver(
    model_part, time_scheme)

from pyKratos import newton_raphson_strategy
strategy = newton_raphson_strategy.NewtonRaphsonStrategy(
    model_part, time_scheme, builder_and_solver, 100, 1.0e-5, 1.0e-3)

strategy.Initialize()
#open file for drag and lift computation
strategy.OpenFile(dragLiftFile)

mesh_name = "test"
gid_io_input.WriteMesh(model_part, mesh_name)
dt = 0.01
nsteps = 2000
outputStep = 10
step = 1

#to be consistend with kratos results
model_part.CloneTimeStep(dt)
model_part.CloneTimeStep(2*dt)

# ------------------------ Define Velocity Input Type ----------------------- #
#vMax = 1
vRange = array([2.5, 5])
Period = array([1, 2, 3])
for node in model_part.NodeIterators():
    if 'xMin' in locals():
        if(node.coordinates[0] < xMin):
            xMin = node.coordinates[0]
    else:
        xMin = node.coordinates[0]
     
inletNodes = GetNodes(model_part, 0, xMin)

#InletVelocity = ParabolicInletVelocity(inletNodes, vMax)
InletVelocity = OscillatingParabolicInletVelocity(inletNodes, vRange, Period)

# --------------------- Define and Preallocate Node Sets -------------------- #
sampleNodes1 = GetNodes(model_part, 0, -10)		
sampleNodes2 = GetNodes(model_part, 0, 7)
sampleNodes3 = GetNodes(model_part, 0, 24)
sampleNodes4 = GetNodes(model_part, 0, 40)

DataOutput1 = outputLine("DataOutFileFirstLine.txt",sampleNodes1)
DataOutput2 = outputLine("DataOutFileSecondLine.txt",sampleNodes2)
DataOutput3 = outputLine("DataOutFileThirdLine.txt",sampleNodes3)
DataOutput4 = outputLine("DataOutFileFourthLine.txt",sampleNodes4)


for i in range(3,nsteps):
    time = i*dt
    model_part.CloneTimeStep(time)
    print("time = ", time)
    
    InletVelocity.ApplyInletVelocity(time)
    
    strategy.Solve()
    
    DataOutput1.writeTimeStep(time)
    DataOutput2.writeTimeStep(time)
    DataOutput3.writeTimeStep(time)
    DataOutput4.writeTimeStep(time)
    
    #check if this step results are written
    if(step >= outputStep):
        gid_io_input.WriteNodalResults(PRESSURE, model_part.NodeIterators(), time)
        gid_io_input.WriteNodalResults(VELOCITY, model_part.NodeIterators(), time)
        #gid_io_input.WriteNodalResults(ACCELERATION, model_part.NodeIterators(), time)
        step = 0
    else:
        step = step + 1


strategy.CloseFile()

DataOutput1.closeFile()
DataOutput2.closeFile()
DataOutput3.closeFile()
DataOutput4.closeFile()

#stop timer
stop = timeit.default_timer()

LogFile = open("LOG.txt","w")
resultTime = "Program runntime: " + str(stop - start)
LogFile.write(resultTime)
LogFile.close()
print("Program runntime: ",stop - start)