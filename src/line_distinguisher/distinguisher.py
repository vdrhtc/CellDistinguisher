'''
Created on 18 марта 2014 г.

@author: elvira
'''

from line_distinguisher.hough_transform import get_coefficients
from PIL import ImageFilter
from cell_distinguisher.distinguisher import make_threshold
import sys

def prepare_image(im, slice_thickness = 50, threshold = 80):
    image = im.copy()   
    image = __image_preparing__(image, threshold)
    slices =__slice_image__(image, slice_thickness)
    return slices

def get_lines(slice_, tolerance_a_b = (2, 0), max_a = 0.1):
    print("Getting coefficients..."); sys.stdout.flush()
    coeffs = get_coefficients(slice_, tolerance_a_b, max_a)
    return coeffs

def __image_preparing__(im, threshold):
        converted_im = im.convert(mode = 'L') 
        filtered_converted_im = converted_im.filter(ImageFilter.FIND_EDGES) 
        make_threshold(filtered_converted_im, threshold)
        return filtered_converted_im

def __slice_image__(im, slice_thickness):
    im_width, im_height = im.getbbox()[2:]
    slices = []
    i=0
    while i<=im_width-slice_thickness :
        slices.append(im.crop((i, 0, i+slice_thickness, im_height)))   
        i+=slice_thickness
    return slices

