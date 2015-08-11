function [Pressure, Velocity_X, Velocity_Y, TimeSteps] =  LoadData( filename )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
% path = '../';
filepath = strcat(filename);

% Open the file
fileID = fopen(filepath,'r');
fgetl(fileID);
line = fgetl(fileID);
lengthOfVector = cell2mat(textscan(line,  '%*s %f',1));

numberOfTimeSteps = 1;

while ~feof(fileID)
    line = fgetl(fileID);
    TimeSteps(numberOfTimeSteps) = cell2mat(textscan(line,  '%f',1));
    for i=1:lengthOfVector
        line = fgetl(fileID);
        Pressure(numberOfTimeSteps,i) = cell2mat(textscan(line,  '%f',1));
        Velocity_X(numberOfTimeSteps,i) = cell2mat(textscan(line,  '%*f %f',1));
        Velocity_Y(numberOfTimeSteps,i) = cell2mat(textscan(line,  '%*f %*f %f',1));
    end
    numberOfTimeSteps = numberOfTimeSteps + 1;
end

%% Close file
fclose(fileID);
end