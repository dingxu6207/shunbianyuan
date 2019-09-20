function [image,doubleimage] = doerzhi(erimage)
[hang,lie] = size(erimage);

p = zeros(1,256);  
for i = 0:255  
   p(i+1)=length(find(erimage == i))/(hang*lie);  
end

[m,n] = max(p);
threhold = 150;

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
