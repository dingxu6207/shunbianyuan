%读入原图 （左 右）
img1=imread('2.jpg');
img2=imread('1.jpg');

%查找它们的SIFT特征,并返回匹配点对---------------------特征匹配 开始
[des1, des2] = siftMatch(img1, img2);

pts1=des1';pts2=des2';
 
%单应矩阵过滤匹配
[Ht,matchs] = findHomography(pts1,pts2);
pts1=pts1(:,matchs);%取出内点
pts2=pts2(:,matchs);
des1=pts1';%格式转回
des2=pts2';
 
% 画出匹配特征点的连接线（好点）
drawLinedCorner(img1,des1,img2, des2) ;
%------------------------------------------------------特征匹配 结束
