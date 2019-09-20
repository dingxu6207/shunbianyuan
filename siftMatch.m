% �˺�����ȡ����ͼ�񣬲������ǵ�SIFT����
% ����ƥ��ľ���С����ڶ�����ӽ�ƥ��ľ������ֵʱ���Ž���ƥ�䡣
% ����������ͼ���ƥ��㣬matchLoc1 = [x1,y1;x2,y2;...]
%
% 
 
function [matchLoc1,matchLoc2] = siftMatch(img1, img2)
 
% ��ÿ��ͼ����� SIFT ������
[des1, loc1] = sift(img1);
[des2, loc2] = sift(img2);
 
% ����MATLAB�е�Ч��,���㵥λ����֮��ĵ�˱�ŷʽ�������ݡ���ע��: 
% ע��ǵı���(��λʸ������ķ�����)��С�Ƕȵ�ŷ�Ͼ���֮�ȵĽ���ֵ��
%
% distRatio: ��������ƥ����ֻ����ʸ���Ǵ�����ĵڶ����ڵı�ֵС��distRatio�ġ�
distRatio = 0.7;   
 
% �ڵ�һ��ͼ���е�ÿ����������ѡ������ƥ�䵽�ڶ���ͼ��
des2t = des2';                          % Ԥ�������ת�� 
matchTable = zeros(1,size(des1,1));
for i = 1 : size(des1,1)
   dotprods = des1(i,:) * des2t;        % ����������
   [vals,indx] = sort(acos(dotprods));  % ȡ�����Һ�������
 
   % ������������ھӽǱ���С��distRatio��
   if (vals(1) < distRatio * vals(2))
      matchTable(i) = indx(1);
   else
      matchTable(i) = 0;
   end
end
% ����ƥ�����ݱ�
 
num = sum(matchTable > 0);
fprintf('�ҵ� %d ��ƥ���.\n', num);
 
idx1 = find(matchTable);
idx2 = matchTable(idx1);
x1 = loc1(idx1,2);
x2 = loc2(idx2,2);
y1 = loc1(idx1,1);
y2 = loc2(idx2,1);
 
matchLoc1 = [y1,x1];%��y�����ǰ��
matchLoc2 = [y2,x2];
 
end
 