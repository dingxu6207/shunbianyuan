%����ԭͼ ���� �ң�
img1=imread('2.jpg');
img2=imread('1.jpg');

%�������ǵ�SIFT����,������ƥ����---------------------����ƥ�� ��ʼ
[des1, des2] = siftMatch(img1, img2);

pts1=des1';pts2=des2';
 
%��Ӧ�������ƥ��
[Ht,matchs] = findHomography(pts1,pts2);
pts1=pts1(:,matchs);%ȡ���ڵ�
pts2=pts2(:,matchs);
des1=pts1';%��ʽת��
des2=pts2';
 
% ����ƥ��������������ߣ��õ㣩
drawLinedCorner(img1,des1,img2, des2) ;
%------------------------------------------------------����ƥ�� ����
