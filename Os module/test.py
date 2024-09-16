from pytesseract import pytesseract
from PIL import Image

# Set the path to Tesseract if needed
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Test image (you can use any image with text for testing)
image_path = 'test_image.png'  # Replace with your actual image path
img = Image.open('blue2.jpg')

# Extract text from image
text = pytesseract.image_to_string(img)
print(text)

# with open('tesseractNew.txt', '+a') as file:
#     for i in text:
#         file.write(i , " ")
