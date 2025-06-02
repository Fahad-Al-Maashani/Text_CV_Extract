from google.cloud import vision
import json

client = vision.ImageAnnotatorClient()
with open("cv_image.png", "rb") as image_file:
    content = image_file.read()

image = vision.Image(content=content)
response = client.text_detection(image=image)
extracted_text = response.full_text_annotation.text

print(extracted_text)
