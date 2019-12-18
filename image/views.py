from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import numpy as np
from PIL import Image

import urllib.request


def gaussian_kernel(size, sigma=1):
    size = int(size)
    x, y = np.mgrid[-size:size + 1, -size:size + 1]
    normal = 1 / (2.0 * np.pi * sigma ** 2)
    g = np.exp(-((x ** 2 + y ** 2) / (2.0 * sigma ** 2))) * normal
    return g


def gauss_blur_application(img):
    im_array = img
    if type(img) is not np.ndarray:
        im_array = np.array(img)

    gaussian_filter = gaussian_kernel(2)

    for i in range(5):
        for x in range(im_array.shape[0]):
            for y in range(im_array.shape[1]):
                if (x != 0 and x != 1 and x != 2 and x != im_array.shape[0] - 1 and x != im_array.shape[0] - 2 and x !=
                        im_array.shape[0] - 3 and y != 0 and y != 1 and y != 2 and y != im_array.shape[1] - 1 and y !=
                        im_array.shape[1] - 2 and y != im_array.shape[1] - 3):
                    s = np.dot(im_array[x - 2:x + 3, y - 2:y + 3].flatten(), gaussian_filter.flatten().T)

                    im_array[x, y] = s

    return np.array(im_array)





def index(request):

    """url = "https://m.media-amazon.com/images/I/91dHjorKkhL._SS500_.jpg"

    image = Image.open(urllib.request.urlopen(url)).convert('L²')
    im_array = np.array(image)

    image = gauss_blur_application(im_array)

    image = Image.fromarray(im_array)
    image.save("image/static/image/test.jpg")"""

    template = loader.get_template('image/index.html')

    return HttpResponse(template.render(request=request))


def floutage(request):
    



def inversion(request):
