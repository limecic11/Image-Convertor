from PIL import Image
import pyfiglet
print (pyfiglet.figlet_format("Image  Convertor"))
print ("Enter The Image Path==>")
path=input()
try:
    img=Image.open(path)
    myconverted_img=img.convert("L")
    myconverted_img.show()
except :
    print("Image Not Found")