'''
Created on 18 марта 2014 г.

@author: elvira
'''
BLACK = 0
WHITE = 255

from line_distinguisher.counted_point import CountedPoint
import sys, math


def get_coefficients(slices, tolerance):
    lines_parameters = fill_intersection_points_list(
                                        get_hough_line_parameters(slices[1]), tolerance)
    return lines_parameters
    
    
def get_hough_line_parameters(slice_):
    
    hough_line_parameters = []
    for x in range(0, slice_.getbbox()[2]):
        for y in range(0, slice_.getbbox()[3]):
            if slice_.getpixel((x,y)) == WHITE :
                hough_line_parameters.append((-y,x))
    print("Processing ", len(hough_line_parameters), "points.")
    return hough_line_parameters
            
def fill_intersection_points_list(line_parameters, tolerance):
    intersection_points = []
    for i in range(0, len(line_parameters)):
        print("", end='\r')
        print('{}, {}'.format(len(intersection_points), i), end='')
        sys.stdout.flush()
            
        for j in range (i+1, len(line_parameters)):
            
            delta_Y = line_parameters[i][0]-line_parameters[j][0]
            if delta_Y != 0:
                a=(line_parameters[j][1]-line_parameters[i][1])/delta_Y
                
                if math.fabs(a)<0.1:
                    b=line_parameters[i][0]*a+line_parameters[i][1]
                    found = False
                    for point in intersection_points:
                        if point.check_vicinity(a, b, tolerance):
                            point.process_match(a, b)
                            found = True
                            break
                            
                    if not found:
                        intersection_points.append(CountedPoint((a,b)))
    
                if len(intersection_points) == 0:
                    intersection_points.append(CountedPoint((a,b)))
                    
    return intersection_points          
