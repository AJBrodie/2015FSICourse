% Frequency Example
clear all
close all
clc

xsamp = 0:0.01:20;
xcont = 0:0.0001:20;

y=@(x) sin(2*pi*60*x);

ysamp=y(xsamp);
ycont=y(xcont);

plot(xsamp,ysamp,xcont,ycont)
