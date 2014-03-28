'''
Created on 18 марта 2014 г.

@author: elvira
'''

class CountedPoint(object):
    '''
    A pair of coordinates and a counter
    '''


    def __init__(self, coordinates):
        '''
        Constructor
        '''
        self.coordinates = coordinates
        self.counter = 0
        self.sum = coordinates
        
    def process_match(self, a, b):
        
        self.counter += 1
        self.average_coordinates_with_new_point(a, b)
        
    def get_coordinates(self):
        
        return self.coordinates   
        
    def get_counter(self):
        
        return self.counter
    
    def average_coordinates_with_new_point(self, a, b):
        self.sum = (self.sum[0]+a, self.sum[1]+b)
        self.coordinates = (self.sum[0]/self.counter, self.sum[1]/self.counter)
        
    def check_vicinity(self, a, b, tolerance):
        return True if (self.coordinates[0] - a) < tolerance[0] and (self.coordinates[1] - b) < tolerance[1] else False
            
        
