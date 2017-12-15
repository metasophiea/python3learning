from scipy import misc
import matplotlib.pyplot, numpy

# # gathers the package provided picture 'ascent'
# ascent = misc.ascent()
# print( ascent.dtype )
# print( ascent.shape )
# print( ascent.max() )

# matplotlib.pyplot.axis("off")
# matplotlib.pyplot.gray()
# matplotlib.pyplot.imshow(ascent)
# matplotlib.pyplot.show()




# Loading in an image and displaying it
import matplotlib.image
# img = matplotlib.image.imread('testImage.png')  # only images of the format png are supported
# print(img[:3])

# matplotlib.pyplot.axis("off")
# matplotlib.pyplot.imshow(img)
# matplotlib.pyplot.show()

# matplotlib.pyplot.imshow(img[:,:,1])
# matplotlib.pyplot.show()




# # Tinting and Shading an image
# def tint(img, percent):
#     # this function finds the difference between each pixel of the image and pure white,
#     # then adds on a percentage amount of that different to that pixel (defined by 'percent')
#     return img + (numpy.ones(img.shape)-img)*percent

# def shade(img, percent):
#     # performing the opposite operation to tint; this function replaces each pixel's value
#     # with a percentage of itself 
#     return img*(1-percent)

# matplotlib.pyplot.imshow( tint(img,0.5) ) 
# matplotlib.pyplot.show()
# matplotlib.pyplot.imshow( shade(img,0.5) ) 
# matplotlib.pyplot.show()




# # Applying Gradients
# def vertical_gradient_line(image, reverse=False):
#     number_of_columns = image.shape[1]

#     if reverse:
#         C = numpy.linspace(1, 0, number_of_columns)
#     else:
#         C = numpy.linspace(0, 1, number_of_columns)

#     C = numpy.dstack((C, C, C))

#     return C

# def horizontal_gradient_line(image, reverse=False):
#     number_of_rows, number_of_columns = image.shape[:2]
#     if reverse:
#         C = numpy.linspace(1, 0, number_of_rows)
#     else:
#         C = numpy.linspace(0, 1, number_of_rows)

#     C = C[numpy.newaxis,:]
#     C = numpy.concatenate((C, C, C)).transpose()
#     C = C[:, numpy.newaxis]
    
#     return C

# matplotlib.pyplot.imshow( img*vertical_gradient_line(img) ) 
# matplotlib.pyplot.show()
# matplotlib.pyplot.imshow( img*vertical_gradient_line(img, reverse=True) ) 
# matplotlib.pyplot.show()

# matplotlib.pyplot.imshow( img*horizontal_gradient_line(img) ) 
# matplotlib.pyplot.show()
# matplotlib.pyplot.imshow( img*horizontal_gradient_line(img, reverse=True) ) 
# matplotlib.pyplot.show()



# Cropping
img = matplotlib.image.imread('testImage.png')[20:150, 210:490]
matplotlib.pyplot.axis("off")
matplotlib.pyplot.imshow(img)
matplotlib.pyplot.show()








