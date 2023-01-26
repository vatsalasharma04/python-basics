#Import necessary image modules 
from PIL import Image,ImageColor 
 
# Create new image & get color RGB tuple. 
img = Image.new("RGB", (256, 256), ImageColor.getrgb("#779933")) 
 
#Show image 
img.show() 
