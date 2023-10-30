# # import PIL
# # import 


# import matplotlib.pyplot as plt
# import keras_ocr
# from PIL import Image

# # keras-ocr will automatically download pretrained
# # weights for the detector and recognizer.
# pipeline = keras_ocr.pipeline.Pipeline()

# # Get a set  example images
# # image_paths = ['img-2.jpg', 'img-3.jpg']

# # Load images using Pillow and store them in a list
# images = [
#     keras_ocr.tools.read(url) for url in [
#         'https://traderlionmedia.s3.us-east-2.amazonaws.com/wp-content/uploads/2021/07/08162042/Socrates-Quotes-1-1-1020x574.jpg',
#         'https://traderlionmedia.s3.us-east-2.amazonaws.com/wp-content/uploads/2021/07/08162041/Socrates-Quotes-2-1020x574.jpg',
#         'https://traderlionmedia.s3.us-east-2.amazonaws.com/wp-content/uploads/2021/07/08162041/Socrates-Quotes-3-1020x574.jpg'
#     ]
# ]
# # images.append(Image.open("img-2.jpg"))
# # images.append(Image.open("img-3.jpg"))
# # Each list of predictions in prediction_groups is a list of
# # (word, box) tuples.
# prediction_groups = pipeline.recognize(images)


# # Plot the predictions
# fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
# for ax, image, predictions in zip(axs, images, prediction_groups):
#     keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
# # Steps
#     # read pdf
#     # if pdf multiple pages: iterate over it
#     # extract image from pdf page, (check wich library use)
#     # Hypotesis: I need to know the coodinates of image and sizes so I can extract the position of the text found
#     # process the image to get text
#     # identify match
#     # if coordinates, find how to highlight matched text in image (overlay)
#     # and write all to a new file


import easyocr
from PIL import ImageDraw

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
    # print(f'Bounding Box: {bounding_box}')

# for result in result:
#     if result == "dämm"
#     bounding_box = result[0]
#     points = bounding_box
#     draw.rectangle(points, outline="red", width=2)  # You can choose the color and width you prefer