# import PIL
# import 


import matplotlib.pyplot as plt
import keras_ocr
import PIL

# keras-ocr will automatically download pretrained
# weights for the detector and recognizer.
pipeline = keras_ocr.pipeline.Pipeline()

# Get a set of three example images
image_paths = ['img-2.jpg', 'img-3.jpg']

# Load images using Pillow and store them in a list
images = [Image.open(image_path) for image_path in image_paths]
# [
#     keras_ocr.tools.read(url) for url in [
#         'https://upload.wikimedia.org/wikipedia/commons/b/bd/Army_Reserves_Recruitment_Banner_MOD_45156284.jpg',
#         'https://upload.wikimedia.org/wikipedia/commons/e/e8/FseeG2QeLXo.jpg',
#         'https://upload.wikimedia.org/wikipedia/commons/b/b4/EUBanana-500x112.jpg'
#     ]
# ]

# Each list of predictions in prediction_groups is a list of
# (word, box) tuples.
prediction_groups = pipeline.recognize(images)

# Plot the predictions
fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
for ax, image, predictions in zip(axs, images, prediction_groups):
    keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
# Steps
    # read pdf
    # if pdf multiple pages: iterate over it
    # extract image from pdf page, (check wich library use)
    # Hypotesis: I need to know the coodinates of image and sizes so I can extract the position of the text found
    # process the image to get text
    # identify match
    # if coordinates, find how to highlight matched text in image (overlay)
    # and write all to a new file
