% 此函数读取两幅图像，查找它们的SIFT特征
% 仅当匹配的距离小于与第二个最接近匹配的距离的阈值时，才接受匹配。
% 它返回两个图像的匹配点，matchLoc1 = [x1,y1;x2,y2;...]
%
% 
 
function [matchLoc1,matchLoc2] = siftMatch(img1, img2)
 
% 在每个图像查找 SIFT 特征点
[des1, loc1] = sift(img1);
[des2, loc2] = sift(img2);
 
% 对于MATLAB中的效率,计算单位向量之间的点乘比欧式距离更快捷。请注意: 
% 注意角的比率(单位矢量点积的反余弦)是小角度的欧氏距离之比的近似值。
%
% distRatio: 在这两队匹配中只保留矢量角从最近的第二近邻的比值小于distRatio的。
distRatio = 0.7;   
 
% 在第一个图像中的每个描述符，选择它的匹配到第二个图像。
des2t = des2';                          % 预计算矩阵转置 
matchTable = zeros(1,size(des1,1));
for i = 1 : size(des1,1)
   dotprods = des1(i,:) * des2t;        % 计算点积向量
   [vals,indx] = sort(acos(dotprods));  % 取逆余弦和排序结果
 
   % 看看和最近的邻居角比率小于distRatio。
   if (vals(1) < distRatio * vals(2))
      matchTable(i) = indx(1);
   else
      matchTable(i) = 0;
   end
end
% 保存匹配数据表
 
num = sum(matchTable > 0);
fprintf('找到 %d 对匹配点.\n', num);
 
idx1 = find(matchTable);
idx2 = matchTable(idx1);
x1 = loc1(idx1,2);
x2 = loc2(idx2,2);
y1 = loc1(idx1,1);
y2 = loc2(idx2,1);
 
matchLoc1 = [y1,x1];%把y坐标放前面
matchLoc2 = [y2,x2];
 
end
 