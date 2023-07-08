%输出参数，f,Y为频谱图的横纵坐标，y为原始信号，fs为采频
function [f,Y]=my_fft(y,fs)
    n=length(y);
    Y=2*abs(fft(y)/n);  
    f = (0:n/2)*fs/n;
    Y=Y(1:length(f));




    