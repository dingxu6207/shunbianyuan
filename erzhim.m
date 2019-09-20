A=imread('201906061526400716.jpg');   %读取到一张图片
gdata = rgb2gray(A);

[erzhiimage,doubleimage] = doerzhi(gdata);

K1=medfilt2(erzhiimage,[10 10]); %中值滤波

figure();
subplot(1,2,1);  
imshow(gdata);    %显示二值化之前的图片
title('原图'); 
subplot(1,2,2);
imshow(K1);    %显示二值化之后的图片
title('二值化')
imwrite(K1,'v1.jpg','quality',80);