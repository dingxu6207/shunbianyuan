A=imread('201906061526400716.jpg');   %��ȡ��һ��ͼƬ
gdata = rgb2gray(A);

[erzhiimage,doubleimage] = doerzhi(gdata);

K1=medfilt2(erzhiimage,[10 10]); %��ֵ�˲�

figure();
subplot(1,2,1);  
imshow(gdata);    %��ʾ��ֵ��֮ǰ��ͼƬ
title('ԭͼ'); 
subplot(1,2,2);
imshow(K1);    %��ʾ��ֵ��֮���ͼƬ
title('��ֵ��')
imwrite(K1,'v1.jpg','quality',80);