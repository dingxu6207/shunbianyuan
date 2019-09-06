function [image,doubleimage] = doerzhi(erimage)
[hang,lie] = size(erimage);
threhold = 110;
for i = 1:hang
    for j = 1:lie
        if (erimage(i,j) >= threhold)
            erimage(i,j) = 1;
        else 
            erimage(i,j) = 0;
        end
    end
    
end

image = erimage*255;
doubleimage = double(image);
end
