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
import re

def main():

    target = "damm"
    # Create an EasyOCR Reader for german
    reader = easyocr.Reader(['de'])

    # Load an image
    image_path = 'sample2.jpg'

    # Recognize text in the image
    results = reader.readtext(image_path)
    # ic(results)

    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    # Print the recognized text and bounding boxes
    for result in results:
        text = result[1]  # Access the recognized text
        bounding_box = result[0]  # Access the bounding box
        # ic(f'Text: {text}')
        if target_is_present(text, target):
            # print(f'Bounding Box: {bounding_box[1]}')
            # Convert coordinates to PIL´s structure
            x = bounding_box[0]
            y = bounding_box[2]
            xy = x + y
            # Draw rectangle
            draw.rectangle(xy, outline="red", width=2)

    img.show()
    img.save('output_image2.jpg')        

def target_is_present(text, target):
    text = text.lower()
    pattern = r"damm"
    if re.search(pattern, text):
        return True
    else:
        return False

if __name__ == "__main__":
    main()

