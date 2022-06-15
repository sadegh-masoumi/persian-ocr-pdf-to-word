from PIL import Image
import pytesseract

img_path = './test.jpg'

text = pytesseract.image_to_string(Image.open(img_path), lang='fas')
print(text)
