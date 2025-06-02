import pytesseract
from PIL import Image

# Load image
image = Image.open("cv_image.png")

# Extract text
extracted_text = pytesseract.image_to_string(image)

print(extracted_text)
