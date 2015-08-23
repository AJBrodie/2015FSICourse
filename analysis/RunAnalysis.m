close all;
%clear all;
%% Read in data and define points of interest
filename = 'DataOutFileFirstLine.txt';
[Pressure, Velocity_X1, Velocity_Y1, TimeSteps] = LoadData(filename);

filename = 'DataOutFileSecondLine.txt';
[Pressure, Velocity_X2, Velocity_Y2, TimeSteps] = LoadData(filename);

filename = 'DataOutFileThirdLine.txt';
[Pressure, Velocity_X3, Velocity_Y3, TimeSteps] = LoadData(filename);

% filename = 'Line01.res';
% [Pressure, Velocity_X1, Velocity_Y1, TimeSteps] = LoadData(filename);
% 
% filename = 'Line02.res';
% [Pressure, Velocity_X2, Velocity_Y2, TimeSteps] = LoadData(filename);
% 
% filename = 'Line03.res';
% [Pressure, Velocity_X3, Velocity_Y3, TimeSteps] = LoadData(filename);

middlePoint = round(length(Velocity_X3(1,:))/2);
quarterPoint = ceil(length(Velocity_X3(1,:))/4);
threequarterPoint = ceil(3*length(Velocity_X3(1,:))/4);

%% Calculating Fourier Transforms
Ts = 0.01;                      % Sample period
Fs = 1/Ts;                      % Sampling frequency
L = length(Velocity_X1);        % Length of signal
t = (0:L-1)*Ts;                  % Time vector
NFFT = 2^nextpow2(L);           % Next power of 2 from length of y

temp = fft(Velocity_X1(:,quarterPoint),NFFT)/L;
f_quarter_VelX1 = 2*abs(temp(1:NFFT/2+1));
temp = fft(Velocity_X1(:,middlePoint),NFFT)/L;
f_middle_VelX1 = 2*abs(temp(1:NFFT/2+1));
temp = fft(Velocity_X1(:,threequarterPoint),NFFT)/L;
f_threequarter_VelX1 = 2*abs(temp(1:NFFT/2+1));

temp = fft(Velocity_X2(:,quarterPoint),NFFT)/L;
f_quarter_VelX2 = 2*abs(temp(1:NFFT/2+1));
temp = fft(Velocity_X2(:,middlePoint),NFFT)/L;
f_middle_VelX2 = 2*abs(temp(1:NFFT/2+1));
temp = fft(Velocity_X2(:,threequarterPoint),NFFT)/L;
f_threequarter_VelX2 = 2*abs(temp(1:NFFT/2+1));

temp = fft(Velocity_X3(:,quarterPoint),NFFT)/L;
f_quarter_VelX3 = 2*abs(temp(1:NFFT/2+1));
temp = fft(Velocity_X3(:,middlePoint),NFFT)/L;
f_middle_VelX3 = 2*abs(temp(1:NFFT/2+1));
temp = fft(Velocity_X3(:,threequarterPoint),NFFT)/L;
f_threequarter_VelX3 = 2*abs(temp(1:NFFT/2+1));

temp = fft(Velocity_Y1(:,quarterPoint),NFFT)/L;
f_quarter_VelY1 = 2*abs(temp(1:NFFT/2+1));
temp = fft(Velocity_Y1(:,middlePoint),NFFT)/L;
f_middle_VelY1 = 2*abs(temp(1:NFFT/2+1));
temp = fft(Velocity_Y1(:,threequarterPoint),NFFT)/L;
f_threequarter_VelY1 = 2*abs(temp(1:NFFT/2+1));

temp = fft(Velocity_Y2(:,quarterPoint),NFFT)/L;
f_quarter_VelY2 = 2*abs(temp(1:NFFT/2+1));
temp = fft(Velocity_Y2(:,middlePoint),NFFT)/L;
f_middle_VelY2 = 2*abs(temp(1:NFFT/2+1));
temp = fft(Velocity_Y2(:,threequarterPoint),NFFT)/L;
f_threequarter_VelY2 = 2*abs(temp(1:NFFT/2+1));

temp = fft(Velocity_Y3(:,quarterPoint),NFFT)/L;
f_quarter_VelY3 = 2*abs(temp(1:NFFT/2+1));
temp = fft(Velocity_Y3(:,middlePoint),NFFT)/L;
f_middle_VelY3 = 2*abs(temp(1:NFFT/2+1));
temp = fft(Velocity_Y3(:,threequarterPoint),NFFT)/L;
f_threequarter_VelY3 = 2*abs(temp(1:NFFT/2+1));

f = Fs/2*linspace(0,1,NFFT/2+1);


%% Plots

% Plot velocity over time at a point
figure(1)
subplot(2,3,1);
plot(TimeSteps, Velocity_X1(:,quarterPoint),TimeSteps, Velocity_X1(:,middlePoint),TimeSteps, Velocity_X1(:,threequarterPoint))
title('X=-10')
ylabel('U')
xlabel('Time')
legend('Y=-5','Y=0','Y=5')
subplot(2,3,4);
plot(TimeSteps, Velocity_Y1(:,quarterPoint),TimeSteps, Velocity_Y1(:,middlePoint),TimeSteps, Velocity_Y1(:,threequarterPoint))
title('X=-10')
ylabel('V')
xlabel('Time')
legend('Y=-5','Y=0','Y=5')

subplot(2,3,2);
plot(TimeSteps, Velocity_X2(:,quarterPoint),TimeSteps, Velocity_X2(:,middlePoint),TimeSteps, Velocity_X2(:,threequarterPoint))
title('X=7')
ylabel('U')
xlabel('Time')
legend('Y=-5','Y=0','Y=5')
subplot(2,3,5);
plot(TimeSteps, Velocity_Y2(:,quarterPoint),TimeSteps, Velocity_Y2(:,middlePoint),TimeSteps, Velocity_Y2(:,threequarterPoint))
title('X=7')
ylabel('V')
xlabel('Time')
legend('Y=-5','Y=0','Y=5')

subplot(2,3,3);
plot(TimeSteps, Velocity_X3(:,quarterPoint),TimeSteps, Velocity_X3(:,middlePoint),TimeSteps, Velocity_X3(:,threequarterPoint))
title('X=24')
ylabel('U')
xlabel('Time')
legend('Y=-5','Y=0','Y=5')
subplot(2,3,6);
plot(TimeSteps, Velocity_Y3(:,quarterPoint),TimeSteps, Velocity_Y3(:,middlePoint),TimeSteps, Velocity_Y3(:,threequarterPoint))
title('X=24')
ylabel('V')
xlabel('Time')
legend('Y=-5','Y=0','Y=5')

% Plot Velocity by frequency content at point
figure(2)
subplot(2,3,1);
plot(f,f_quarter_VelX1,f,f_middle_VelX1,f,f_threequarter_VelX1) 
title('X=-10')
xlabel('Frequency (Hz)')
legend('Y=-5','Y=0','Y=5')
subplot(2,3,4);
plot(f,f_quarter_VelY1,f,f_middle_VelY1,f,f_threequarter_VelY1) 
title('X=-10')
xlabel('Frequency (Hz)')
legend('Y=-5','Y=0','Y=5')

subplot(2,3,2);
plot(f,f_quarter_VelX2,f,f_middle_VelX2,f,f_threequarter_VelX2) 
title('X=7')
xlabel('Frequency (Hz)')
legend('Y=-5','Y=0','Y=5')
subplot(2,3,5);
plot(f,f_quarter_VelY2,f,f_middle_VelY2,f,f_threequarter_VelY2) 
title('X=7')
xlabel('Frequency (Hz)')
legend('Y=-5','Y=0','Y=5')

subplot(2,3,3);
plot(f,f_quarter_VelX3,f,f_middle_VelX3,f,f_threequarter_VelX3) 
title('X=24')
xlabel('Frequency (Hz)')
legend('Y=-5','Y=0','Y=5')
subplot(2,3,6);
plot(f,f_quarter_VelY3,f,f_middle_VelY3,f,f_threequarter_VelY3) 
title('X=24')
xlabel('Frequency (Hz)')
legend('Y=-5','Y=0','Y=5')


% % close(figure)
% figure
% writerObj = VideoWriter('VideoInlet.avi');
% open(writerObj);
% y = linspace(0,20,21)
% plot(Velocity_X1(1,:),y)
% xlabel('U')
% ylabel('Y')
% % axis tight
% axis([0 10 0 20])
% set(gca,'nextplot','replacechildren');
% set(gcf,'Renderer','zbuffer');
% for k = 1:length(TimeSteps)
%     plot(Velocity_X1(k,:),y)
%     frame = getframe;
%     writeVideo(writerObj,frame);
% end
% 
% close(writerObj);