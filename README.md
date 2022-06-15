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


```

pdf2image and Popper
for convert pdf to image

tesseract is model for convert image to text

# requirements
```
pip install -r requirements.txt
```