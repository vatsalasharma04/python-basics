from PIL import Image 
 
# Open an already existing image and create image object 
Object = Image.open(r'abb.png')
 
# perform a flip of left and right 
flippedImage = Object.transpose(Image.FLIP_LEFT_RIGHT) 
 
# display the original image 
Object.show() 
 
# display the horizontal flipped image 
flippedImage.show() 
