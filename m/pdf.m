clear all;
grid on;
i=1;
y = 0

u= rand()

for n= 1:100
u= [u,rand()]
end

 k=-1;
for x = -0.9:0.01:1
    if x < 0 
        y = [y ,x+1]
        
    elseif x>=0
     y = [y, -x+1];
     
     
    end
  i=+1;
    k=[k,x]
end
j=1;




plot(k,y,'-');  
grid on; grid minor;
xlabel('X'); ylabel('f(X)');
title('Triangular distribution - PDF');
grid on 
grid minor
