import PIL
import pytesseract # Not installed yet

# Steps
    # read pdf
    # if pdf multiple pages: iterate over it
    # extract image from pdf page, (check wich library use)
    # Hypotesis: I need to know the coodinates of image and sizes so I can extract the position of the text found
    # process the image to get text
    # identify match
    # if coordinates, find how to highlight matched text in image (overlay)
    # and write all to a new file
