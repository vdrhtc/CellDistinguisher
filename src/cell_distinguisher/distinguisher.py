'''
Created on 12 марта 2014 г.

@author: gleb
'''
BLACK = 0
WHITE = 255

from PIL import Image
from cell_distinguisher.cell import Cell

cells = []

def get_cells_from_image(im, tl_corner, br_corner, pixel_size, threshold):
    image = im.copy()
    make_threshold(image, threshold)
    __iterate_through_image__(image, (tl_corner, br_corner), pixel_size)
    return image
    
    
def make_threshold(im, threshold):
    for x in range(0, im.getbbox()[2]):
        for y in range(0, im.getbbox()[3]):
            if(im.getpixel((x,y)) > threshold):
                im.putpixel((x, y), WHITE)
            else:
                im.putpixel((x, y), BLACK)
                
    return 


def __iterate_through_image__(im, bounds, pixel_size):
    for x in range(bounds[0][0], bounds[1][0]):
        for y in range(bounds[0][1], bounds[1][1]):
            if(im.getpixel((x,y)) == BLACK):
                cell = Cell(im);
                cell.fill_self(im, (x,y), pixel_size)
                if cell.area >= 10 :
                    cells.append(cell)
            

if __name__ == '__main__':
    get_cells_from_image(Image.open('/home/gleb/Документы/Черноголовка/Gruppa1/1_01.tif'))