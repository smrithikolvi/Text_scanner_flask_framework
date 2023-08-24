try:  
    from PIL import Image
except ImportError:  
    import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract'
def ocr_core(filename):  
    """
    This function will handle the core OCR processing of images.
    """
    text = tess.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text
#




#import pytesseract as tess
#tess.pytesseract.tesseract_cmd=r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract'
#from PIL import Image
#img=Image.open('C:\\Users\\Admin\\Documents\\new.png')
#t=tess.image_to_string(img)
#print(t)
