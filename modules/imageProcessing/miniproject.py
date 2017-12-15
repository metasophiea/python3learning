import matplotlib.pyplot
import matplotlib.image
import numpy


def imag_tile(img, n=1, m=1):
    # The image "img" will be repeated n times in vertical and 
    # m times in horizontal direction.

    tiled_img = img

    imgStrip = []
    for a in range(n):
        imgStrip.append(tiled_img)  
    tiled_img = numpy.concatenate(imgStrip, axis=1)

    imgStrip = []
    for a in range(m):
        imgStrip.append(tiled_img)  
    tiled_img = numpy.concatenate(imgStrip, axis=0)

    return tiled_img

basic_pattern = matplotlib.image.imread('testImage.png')
decorators_img = imag_tile(basic_pattern, 3, 3)
matplotlib.pyplot.axis("off")
matplotlib.pyplot.imshow(decorators_img)
matplotlib.pyplot.show()