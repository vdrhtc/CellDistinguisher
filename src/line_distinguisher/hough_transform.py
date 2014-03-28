'''
Created on 18 марта 2014 г.

@author: elvira
'''
BLACK = 0
WHITE = 255

import sys, math


def get_coefficients(slice_, tolerance, max_a):
#     lines_parameters = fill_intersection_points_list(
#                                         get_hough_line_parameters(slices[1]), tolerance)
    lines_parameters = fill_accumulator_list(get_hough_line_parameters(slice_), tolerance, max_a)
    return lines_parameters
    
    
def get_hough_line_parameters(slice_):
    
    hough_line_parameters = []
    for x in range(0, slice_.getbbox()[2]):
        for y in range(0, slice_.getbbox()[3]):
            if slice_.getpixel((x,y)) == WHITE :
                hough_line_parameters.append((-y,x))
    print("Processing ", len(hough_line_parameters), "points.")
    return hough_line_parameters
                


def fill_accumulator_list(line_parameters, tolerance, max_a):      
    intersection_points = {}
    for i in range(0, len(line_parameters)):
        print('', end='\r')
        print('{}, {}'.format(len(intersection_points), i), end='')
        sys.stdout.flush()
            
        for j in range (i+1, len(line_parameters)):
            
            delta_Y = line_parameters[i][0]-line_parameters[j][0]
            
            if delta_Y == 0:
                continue
            
            a=(line_parameters[j][1]-line_parameters[i][1])/delta_Y
                
            if math.fabs(a)<max_a:
                
                b=line_parameters[i][0]*a+line_parameters[i][1]
                
                next_hough_coordinates = (round(a, tolerance[0]), round(b, tolerance[1]))
               
                if next_hough_coordinates in intersection_points.keys():
                    intersection_points[next_hough_coordinates] += 1
                else:
                    intersection_points[next_hough_coordinates] = 1
                    
    return intersection_points
                    
                    
                    
    
    
    