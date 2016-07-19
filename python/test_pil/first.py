from PIL import Image
import pytesseract

file_path = "index.png"
imag = Image.open(file_path)
vcode = pytesseract.image_to_string(imag)
print vcode