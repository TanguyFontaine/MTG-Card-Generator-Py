import matplotlib.pyplot as plt
import numpy as np
import skimage
from skimage import data, io, color, transform, img_as_ubyte
from PIL import Image

#def func3(x, y):
#    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2 + y**2))


## make these smaller to increase the resolution
#dx, dy = 0.05, 0.05

#x = np.arange(-3.0, 3.0, dx)
#y = np.arange(-3.0, 3.0, dy)
#X, Y = np.meshgrid(x, y)

## when layering multiple images, the images need to have the same
## extent.  This does not mean they need to have the same shape, but
## they both need to render to the same coordinate system determined by
## xmin, xmax, ymin, ymax.  Note if you use different interpolations
## for the images their apparent extent could be different due to
## interpolation edge effects

#extent = np.min(x), np.max(x), np.min(y), np.max(y)
#fig = plt.figure(frameon=False)



#Z2 = io.imread("C:\Visual Studio Projects\CardGenerator\CardGenerator\image ressources\\black_mana.png")

#im2 = plt.imshow(Z2, cmap=plt.cm.viridis, interpolation='bilinear', extent=extent)

#Z1 = io.imread("C:\Visual Studio Projects\CardGenerator\CardGenerator\image ressources\golden_frame.png")
#im1 = plt.imshow(Z1, interpolation='nearest', extent=extent)

#plt.show()


background = Image.open("C:\Visual Studio Projects\CardGenerator\CardGenerator\image ressources\golden_frame.png")
foreground = Image.open("F:/Images/9gag/cap/Daniela Lopez Osorio/0fc576f4b21469737f9b87c98b38242b.jpg").convert('RGBA')

background.paste(foreground, (100, 100), foreground)
background.show()

