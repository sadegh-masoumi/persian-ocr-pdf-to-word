# for mac 

```bash
brew install poppler
brew install tesseract
brew install tesseract-lang
brew install pdf2image
```


# for linux
``` bash
# At first you need to remove self-compiled deb-package of Poppler named build:
sudo apt-get purge build

# To install actual version of Poppler use package from repository:
sudo apt-get update
sudo apt-get install libpoppler-dev

# install tesseract
sudo apt install tesseract-ocr -y
```


# for windows

```
Download poppler
https://poppler.freedesktop.org/

Download tesseract
https://tesseract-ocr.github.io/tessdoc/Downloads.html

after install add this path to environ variables

or use this code in main.py
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
convert_from_path(pdf_path, poppler_path=r'C:\Users\ad\Downloads\Compressed\poppler-{version}\bin')
```

pdf2image and Popper
for convert pdf to image

tesseract is model for convert image to text

# requirements
```
pip install -r requirements.txt
```


# usage 
```
python main.py [pdf_path] [output_dir]
```