from PIL import Image
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\r14ale\OCR\tesseract.exe'
filename = r'C:\Users\r14ale\Desktop\New\Images2.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

print(text)