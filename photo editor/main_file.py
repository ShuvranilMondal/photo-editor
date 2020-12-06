from PIL import Image ,ImageEnhance                                    # this module used to opening, manipulating, and saving many different image file formats
import os                                                              # this module used to navigate system files,folder

def convert_image():
    path = input('Enter your path without double quotation  : ')
    imag = Image.open(path)
    imag.save('newfile.pdf')


def all_convert():
    path = input("Enter your path without double quotation  : ")
    con = input("Enter your format PNG OR PDF : ")
    if con == "PNG" or 'png':
        for item in os.listdir(path):
            if item.endswith('.jpg'):
                img = Image.open(item)
                filename, extension = os.path.splitext(item)
                img.save(F'{filename}.png')
    else:
        for item in os.listdir(path):
            if item.endswith('.jpg'):
                img = Image.open(item)
                filename, extension = os.path.splitext(item)
                img.save(F'{filename}.pdf')

def photo_reSize():
    path = input("Enter your path without double quotation  : ")
    height = int(input("Enter your image height : "))
    wide = int(input("Enter your image wide : "))
    img = Image.open(path)
    max_size = (height,wide)
    img.thumbnail(max_size)
    img.save('newfile.jpg')

def sharp_image():
    print('SELECT YOUR PARAMETER BETWEEN 1 TO 10')
    while True:
        try:
            path = input('Enter your path without double quotation  : ')
            parameter = float(input('Enter your parameter : '))
            break
        except ValueError:                     # error handling 
            print('Try again')
    img = Image.open(path)
    enhancer = ImageEnhance.Sharpness(img)
    enhancer.enhance(parameter).save('newFile.jpg')
    img2 = Image.open('newFile.jpg')
    img2.show()

def colour_image():
    print('..........SELECT YOUR PARAMETER BETWEEN 0 TO 10..........')
    while True:
        try:
            path = input('Enter your path without double quotation  : ')
            parameter = float(input('Enter your parameter : '))
            break
        except ValueError:
            print('try again ')
    img = Image.open(path)
    colour_change = ImageEnhance.Color(img)
    colour_change.enhance(parameter).save('new_image.jpg')
    img2 = Image.open('new_image.jpg')
    img2.show()

def conrast_image():
    print("........SELECT YOUR PARAMETER BETWEEN 1 TO 2.........")
    while True:
        try:
            path = input('Enter your path without double quotation  : ')
            parameter = float(input('Enter your parameter : '))
            break
        except ValueError:
            print('Try agian')
        
        
    img = Image.open(path)
    conrast_change = ImageEnhance.Contrast(img)
    conrast_change.enhance(parameter).save('newImage.jpg')
    img2 = Image.open('newImage.jpg')
    img2.show()
    

def bright_image():
    print("........SELECT YOUR PARAMETER BETWEEN 1 TO 2.........")
    while True:
        try:
            path = input('Enter your path without double quotation  : ')
            parameter = float(input('Enter your parameter : '))
            break
        except ValueError:
            print('Try agian')
        
        
    img = Image.open(path)
    brightness_change = ImageEnhance.Brightness(img)
    brightness_change.enhance(parameter).save('newImage2.jpg')
    img2 = Image.open('newImage2.jpg')
    img2.show()


def menu():              # for user interface 
    temp = " "
    print('Convert image to PDF or JPG : Press - 0')
    print('Reduce size of the image : press - 1')
    print('Edit Sharpness : press - 2')
    print('Edit Brightness : press - 3')
    print('Edit Colour : press - 4')
    print('Edit contrast : press - 5')
    print('Convert all images to PDF or JPG : Press - 6')

    num = int(input('Enter your option : '))
    
    if num == 0:
        print(convert_image())
    elif num == 1:
        print(photo_reSize())
    elif num == 2:
        print(sharp_image())
    elif num == 3:
        print(bright_image())
    elif num == 4:
        print(colour_image())
    elif num == 5:
        print(conrast_image())
    elif num == 6:
        print(all_convert())
    return temp

print(menu())
    

    

