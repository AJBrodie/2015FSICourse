close all;
clear all;

filename = 'DataOutFileFirstLine.txt';
[Pressure, Velocity_X1, Velocity_Y1, TimeSteps] = LoadData(filename);

filename = 'DataOutFileSecondLine.txt';
[Pressure, Velocity_X2, Velocity_Y2, TimeSteps] = LoadData(filename);

filename = 'DataOutFileThirdLine.txt';
[Pressure, Velocity_X3, Velocity_Y3, TimeSteps] = LoadData(filename);

middlePoint = round(length(Velocity_X3(1,:))/2);

% figure(1)
% subplot(2,3,1);
% plot(TimeSteps, Velocity_X1(:,middlePoint))
% subplot(2,3,4);
% plot(TimeSteps, Velocity_Y1(:,middlePoint))
% subplot(2,3,2);
% plot(TimeSteps, Velocity_X2(:,middlePoint))
% subplot(2,3,5);
% plot(TimeSteps, Velocity_Y2(:,middlePoint))
% subplot(2,3,3);
% plot(TimeSteps, Velocity_X3(:,middlePoint))
% subplot(2,3,6);
% plot(TimeSteps, Velocity_Y3(:,middlePoint))


% close(figure)
writerObj = VideoWriter('Video.avi');
open(writerObj);
y = linspace(0,20,21)
plot(Velocity_X2(1,:),y)
% axis tight
axis([0 1 0 20])
set(gca,'nextplot','replacechildren');
set(gcf,'Renderer','zbuffer');
for k = 1:length(TimeSteps)
    plot(Velocity_X1(k,:),y)
    frame = getframe;
    writeVideo(writerObj,frame);
end

close(writerObj);