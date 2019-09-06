function reimagedata = operateimage(imagedata)
[hang,lie] = size(imagedata);
mindata = min(imagedata(:));
maxdata = max(imagedata(:));

for i = 1:hang
    for j = 1:lie
    if (imagedata(i,j)> maxdata)
        imagedata(i,j) = 255;
    elseif (imagedata(i,j)< mindata)
        imagedata(i,j) = 0;
    else
        imagedata(i,j) = 255*((imagedata(i,j) - mindata)/(maxdata - mindata));
    end
    end
    
end
%reimagedata = imagedata;
 rmindata = 0;
 rmaxdata = 255;
 reimagedata = (255/log(256))*log(1+(255*(imagedata-rmindata))/(rmaxdata - rmindata));


            
 
            