#Student Name: Varsha Ganesh
#UBID : 50288433
#Email: vganesh2@buffalo.edu

import copy
import cv2

def zero_pad(img, pwx, pwy):
    """Pads a given image with zero at the border."""
    padded_img = copy.deepcopy(img)
    for i in range(pwx):
        padded_img.insert(0, [0 for value in enumerate(padded_img[i])])
        padded_img.insert(len(padded_img), [0 for value in enumerate(padded_img[-1])])
    for i, row in enumerate(padded_img):
        for j in range(pwy):
            row.insert(0, 0)
            row.insert(len(row), 0)
    return padded_img

def crop(img, xmin, xmax, ymin, ymax):
    """Crops a given image."""
    if len(img) < xmax:
        print('WARNING')
    patch = img[xmin: xmax]
    patch = [row[ymin: ymax] for row in patch]
    return patch

def elementwise_add(a, b):
    """Elementwise addition."""
    c = copy.deepcopy(a)
    for i, row in enumerate(a):
        for j, num in enumerate(row):
            c[i][j] += b[i][j]
    return c

def elementwise_sub(a, b):
    """Elementwise substraction."""
    c = copy.deepcopy(a)
    for i, row in enumerate(a):
        for j, num in enumerate(row):
            c[i][j] -= b[i][j]
    return c

def elementwise_mul(a, b):
    """Elementwise multiplication."""
    c = copy.deepcopy(a)
    for i, row in enumerate(a):
        for j, num in enumerate(row):
            c[i][j] *= b[i][j]
    return c

def elementwise_div(a, b):
    """Elementwise division."""
    c = copy.deepcopy(a)
    for i, row in enumerate(a):
        for j, num in enumerate(row):
            c[i][j] /= b[i][j]
    return c

def flip_x(img):
    """Flips a given image along x axis."""
    flipped_img = copy.deepcopy(img)
    center = int(len(img) / 2)
    for i in range(center):
        flipped_img[i] = img[(len(img) - 1) - i]
        flipped_img[(len(img) - 1) - i] = img[i]
    return flipped_img

def flip_y(img):
    """Flips a given image along y axis."""
    flipped_img = copy.deepcopy(img)
    center = int(len(img[0]) / 2)
    for i, row in enumerate(img):
        for j in range(center):
            flipped_img[i][j] = img[i][(len(img[0]) - 1) - j]
            flipped_img[i][(len(img[0]) - 1) - j] = img[i][j]
    return flipped_img

def flip2d(img, axis=None):
     if axis == 0:
         return flip_x(img)
     if axis == 1:
         return flip_y(img)
     if axis == None:
         img = flip_x(img)
         return flip_y(img)
     
    # TODO: implement this function.
    #raise NotImplementedError
def absolute(value):
    if value < 0:
        value = value*-1
    return value