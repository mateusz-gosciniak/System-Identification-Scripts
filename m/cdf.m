
clear all;
grid on;
i=1;
y = ((1/2)*1-1+0.5)
for x = -0.9:0.01:1
    if x < 0 
        y = [y ,((1/2)*x^2+x+0.5)]
        
    elseif x>=0
     y = [y,(-0.5*x^2+x+0.5)];
     
     
    end
  i=+1;
   
end
j=1;
k=-1



for a = -0.9:0.01:1
    k=[k,a]
  
 
end

plot(k,y,'-');  
xlabel('F(X)'); ylabel('X');
title('Triangular distribution - CDF');
grid on 
grid minor
