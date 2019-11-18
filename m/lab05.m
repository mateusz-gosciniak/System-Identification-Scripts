%Linear Dynamic System with memory
clear all;
close all;
%% Create System
N = 1000; % points
% input function
U = 2 * sqrt(3) * rand(1, N) - sqrt(3); %vector
% noise generate
E = -0.01 + (0.01+0.01)*rand(1,N); %vector
% output function without noise
V = zeros(1,N);
V(1) = 0;
for k = 2:1:N
    V(k) = V(k-1)/2 + U(k);
end
% output function with noise
Y = V + E;
%% Gamma Estimation
GammaN = 100;
GammaDash = zeros(1, GammaN);

for i = 1:1:GammaN
    SUM = 0;
    for k = 1:1:(N-i)
        SUM = SUM + U(k)*Y(k+1);
    end
    GammaDash(i) = SUM/(N-i);
end
%% Plots
% plot input function
plot(linspace(0, N, N), U)
figure
plot(linspace(0, N, N), E)
figure
plot(linspace(0, N, N), V)
figure
plot(linspace(0, N, N), Y)
figure
plot(GammaDash, "rx")