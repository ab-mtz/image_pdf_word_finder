# # Steps
#     # read pdf
#     # if pdf multiple pages: iterate over it
#     # extract image from pdf page
#     # Hypotesis: I need to know the coodinates of image and sizes so I can extract the position of the text found
#     # process the image to get text
#     # identify match
#     # if coordinates, find how to highlight matched text in image (overlay)


import easyocr
from PIL import Image, ImageDraw
from icecream import ic

# Create an EasyOCR Reader0< for English text recognition
reader = easyocr.Reader(['de'])

# Load an image
image_path = 'sample1.jpg'

# Recognize text in the image
results = reader.readtext(image_path)
ic(results)
# Print the recognized text and bounding boxes
for result in results:
    text = result[1]  # Access the recognized text
    bounding_box = result[0]  # Access the bounding box
    if text.isdigit():
        print(f'Text: {text}')
        print(f'Bounding Box: {bounding_box}')

# Convert the values from coordinates easyocr to PIL
#  [[53, 405], [77, 405], [77, 419], [53, 419]] to
# [(x0, y0), (x1, y1)] or [x0, y0, x1, y1]


###### and write all to a new file
# img = Image.open(image_path)
# draw = ImageDraw.Draw(img)


# for result in results:
#     bounding_box = result[0]

#     # Need to calculate points from coordinates
#     for box in result[0]:
#         print(box)
#         x1, y1, x2, y2 = box

#         pillow_format_box = (x1, y1, x2, y2)
#         points = bounding_box
#         draw.rectangle(points, outline="red", width=2)

# img.show()
# img.save('output_image.jpg')