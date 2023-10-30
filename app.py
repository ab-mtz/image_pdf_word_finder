# # Steps
#     # read pdf
#     # if pdf multiple pages: iterate over it
#     # extract image from pdf page
#     # Hypotesis: I need to know the coodinates of image and sizes so I can extract the position of the text found
#     # process the image to get text
#     # identify match
#     # if coordinates, find how to highlight matched text in image (overlay)
#     # and write all to a new file


import easyocr
from PIL import Image, ImageDraw

# Create an EasyOCR Reader0< for English text recognition
reader = easyocr.Reader(['de'])

# Load an image
image_path = 'sample1.jpg'

# Recognize text in the image
results = reader.readtext(image_path)

# Print the recognized text and bounding boxes
for result in results:
    text = result[1]  # Access the recognized text
    bounding_box = result[0]  # Access the bounding box
    if text.isdigit():
        print(f'Text: {text}')
        print(f'Bounding Box: {bounding_box}')

img = Image.open(image_path)
draw = ImageDraw.Draw(img)

for result in results:
    bounding_box = result[0]
    # Need to calculate points from coordinates
    points = bounding_box
    draw.rectangle(points, outline="red", width=2)

img.show()