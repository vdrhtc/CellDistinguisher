'''
Created on 12 марта 2014 г.

@author: gleb
'''

from core.distinguisher import BLACK, WHITE

class Cell(object):
    '''
    Class to represent a closed element of the same color
    '''
    
    def __init__(self, im):
        self.contained_points = []
        self.image = im
        self.area = 0

    def fill_self(self, image, start_point,pixel_size):
        self.search_and_add(start_point)
        self.pix_size=pixel_size
        
    def search_and_add(self, point_0):
        self.contained_points.append(point_0)
        self.image.putpixel(point_0, WHITE-100)
        self.area = 0
        while self.area != len(self.contained_points):
            self.area = len(self.contained_points)    
            for point in self.contained_points:
                if self.image.getpixel((point[0]+1, point[1]+1))==BLACK:
                    self.contained_points.append((point[0]+1, point[1]+1))
                    self.image.putpixel((point[0]+1, point[1]+1), WHITE-100)
                    
                if self.image.getpixel((point[0]+1, point[1]))==BLACK:
                    self.contained_points.append((point[0]+1, point[1]))
                    self.image.putpixel((point[0]+1, point[1]), WHITE-100)
                    
                if self.image.getpixel((point[0]+1, point[1]-1))==BLACK:
                    self.contained_points.append((point[0]+1, point[1]-1))
                    self.image.putpixel((point[0]+1, point[1]-1), WHITE-100)
                    
                if self.image.getpixel((point[0], point[1]+1))==BLACK:
                    self.contained_points.append((point[0], point[1]+1))
                    self.image.putpixel((point[0], point[1]+1), WHITE-100)
                if self.image.getpixel((point[0], point[1]-1))==BLACK:
                    self.contained_points.append((point[0], point[1]-1))
                    self.image.putpixel((point[0], point[1]-1), WHITE-100)
                    
                if self.image.getpixel((point[0]-1, point[1]+1))==BLACK:
                    self.contained_points.append((point[0]-1, point[1]+1))
                    self.image.putpixel((point[0]-1, point[1]+1), WHITE-100)
                if self.image.getpixel((point[0]-1, point[1]))==BLACK:
                    self.contained_points.append((point[0]-1, point[1]))
                    self.image.putpixel((point[0]-1, point[1]), WHITE-100)
                if self.image.getpixel((point[0]-1, point[1]-1))==BLACK:
                    self.contained_points.append((point[0]-1, point[1]-1))
                    self.image.putpixel((point[0]-1, point[1]-1), WHITE-100)
        
#             self.recursive_add((point[0], point[1]+1))
#             self.recursive_add((point[0], point[1]-1))
#             self.recursive_add((point[0]-1, point[1]+1))
#             self.recursive_add((point[0]-1, point[1]))
#             self.recursive_add((point[0]-1, point[1]-1))
            
    def first_norm(self):
        ''' Square root of area'''
        return self.pix_size*self.area**(1/2)
    def second_norm(self):
        ''' Max distance'''
        dist = 0
        for point_1 in self.contained_points:
            for point_2 in self.contained_points:
                next_dist = (point_1[0]-point_2[0])**2 +(point_1[1] - point_2[1])**2
                if  next_dist > dist:
                    dist = next_dist;
        return dist**(1/2)*self.pix_size
                
                
                
                
                
                
                