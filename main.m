clc;clear;close all;
warning off all;

%读取图像，拉伸对比度
imagedata = fitsread('E:\shunbianyuan\ldf_download\20190531M31-18object\20150307145403-011-RA.fits');
reimagedata = operateimage(imagedata);
lastdata = uint8(reimagedata);
filtdata = medfilt2(lastdata,[3,3]);
[height,width]=size(filtdata);
%二值化图像
[erzhiimage,doubleimage] = doerzhi(filtdata);

[L,num]=bwlabel(doubleimage,8);

plot_x=zeros(1,num);
plot_y=zeros(1,num);

for k=1:num 
    sum_x=0;    
    sum_y=0;    
    area=0;
   for i=1:height
       for j=1:width
          if L(i,j) == k
             sum_x  = sum_x+i;
             sum_y = sum_y+j;
             area=area+1;
          end
       end
   end
   plot_x(k)=fix(sum_x/area);
   plot_y(k)=fix(sum_y/area);
end
%显示图像
figure(1) 
imshow(filtdata);
figure(2)
imshow(doubleimage);
fitswrite(lastdata,'myfile.fits');

figure(3);imshow(filtdata);
for i=1:num
    hold  on
    plot(plot_y(i) ,plot_x(i), '*')
end
