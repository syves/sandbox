
# Write a function, rec_intersection(rect1, rect2) and returns the
# intersection of the two.
#
# Rectangles are represented as a pair of coordinate-pairs: the
# bottom-left and top-right coordinates (given in [x, y] notation).
#
# Hint: You can calculate the left-most x coordinate of the
# intersection by taking the maximum of the left-most x coordinate of
# each rectangle. Likewise, you can calculate the top-most y
# coordinate of the intersection by taking the minimum of the top most
# y coordinate of each rectangle. 319

#rect = ([x1,y1], [x2, y2]) = [left, bottom], [right , top]

class Rectangle(object):
    left = 0
    right = 0
    top = 0
    bottom = 0
    
    def __init__(self, left, right, top, bottom):
        if left > right:
            raise ValueError('right must be greater than left')
        if bottom > top:
            raise ValueError('top must be greater than bottom')
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        
    def __str__(self):
        return '<Rectangle left={} right={} top={} bottom={}>'.format(
                self.left, self.right, self.top, self.bottom)
        
def coords_to_rect(bottom_left, top_right):
    left, bottom = bottom_left
    right, top = top_right
    return Rectangle(left, right, top, bottom)
    
def rect_to_coords(rect):
    return ([rect.left, rect.bottom], [rect.right, rect.top])
  
    
def rec_intersection(rect1, rect2):
    left = max([rect1.left, rect2.left])
    right = min([rect1.right, rect2.right])
    top = min([rect1.top, rect2.top])
    bottom = max([rect1.bottom, rect2.bottom])
    try:
        intersection = Rectangle(left, right, top, bottom)
    except ValueError as e:
        return None
    return rect_to_coords(intersection)

print rec_intersection(coords_to_rect([0, 0], [2, 1]),
                       coords_to_rect([1, 0], [3, 1]))

