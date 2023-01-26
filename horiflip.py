from PIL import Image 
Object = Image.open(r'abb.png')
# perform a flip of left and right 
flippedImage = Object.transpose(Image.FLIP_TOP_BOTTOM) 
 
# display the original image 
Object.show() 
 
# display the horizontal flipped image 
flippedImage.show()
