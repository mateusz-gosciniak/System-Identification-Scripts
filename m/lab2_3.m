%L2_3
czas = 0:0.001:10
czas2 = 0:0.001:1
f=@(x) exp(-x).*(x>=0)
subplot(2,2,1);
plot(czas, f(czas))
grid on
%axis([-0.2 5 -0.2 1.2])
title('Rozk³ad')
%%
g=@(x) -exp(-x)+1.*(x>=0);
subplot(2,2,2);
plot(czas2, g(czas2))
grid on
title('dystrybuanta')
%%
h=@(x) -log(1-x).*(x>=0);
subplot(2,2,3);
plot(czas2, h(czas2),'LineWidth',2)
grid on
title('odwrotna dystrybuanta')
%%
iteracji = 100000;
ziarno = 0.2945

%[WY] = generator_pila(ziarno, iteracji);
randSet1 = rand(1,iteracji);%randGenTri(ziarno,iteracji); %rand(1,iteracji);%
arguments = randSet1;
arguments2=[0]
for i=1:iteracji-1
    temp = h(arguments(i)); % tu sie wszystko dzieje
    arguments2 = [arguments2, temp];
end

%subplot(2,2,4);
figure(2)
arguments1=arguments2/max(arguments2);
histogram(arguments1,100);
xlabel('zm. los [x]');
ylabel('ilosc wystapieñ [n]');
%axis([0 1.1 -0.1 2]);
title('n = 100000');