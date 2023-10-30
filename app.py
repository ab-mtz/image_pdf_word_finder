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

def main():
    # Create an EasyOCR Reader0< for English text recognition
    reader = easyocr.Reader(['de'])

    # Load an image
    image_path = 'sample1.jpg'

    # Recognize text in the image
    results = reader.readtext(image_path)
    # ic(results)

    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    # Print the recognized text and bounding boxes
    for result in results:
        text = result[1]  # Access the recognized text
        bounding_box = result[0]  # Access the bounding box
        if text == "37":
            print(f'Text: {text}')
            ic(bounding_box)
            print(f'Bounding Box: {bounding_box[1]}')
            x = bounding_box[0]
            ic(x)
            y = bounding_box[1]
            ic(y)
            xy = x + y
            draw.rectangle(xy, outline="red", width=2)

    img.show()
    img.save('output_image.jpg')        



if __name__ == "__main__":
    main()

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