i1=imread('v1.jpg');
i2=imread('v2.jpg');

% i11=rgb2gray(i1);
% i22=rgb2gray(i2);
% imwrite(i11,'v1.jpg','quality',80);
% imwrite(i22,'v2.jpg','quality',80);

num = match('v1.jpg','v2.jpg');

