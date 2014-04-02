
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

#rect = ([x1,y1], [x2, y2])

##why arent there 4 coordinates?
#get 2 more coordinates :bottom_right and top_left
rect1 = [ 
    rect1_bottom_left = [x1, y1],#min x
    rect1_bottom_right = [x2-x1, x2], #max x
    rect1_top_right = [x2, y2], #max y
    rect1_top_left = [y1-y2] #min y 
]

rect2 = [ 
    rect2_bottom_left = [x1, y1],#min x
    rect2_bottom_right = [x2-x1, x2], #max x
    rect2_top_right = [x2, y2], #max y
    rect2_top_left = [y1-y2] #min y 
]

def rec_intersection(rect1, rect2):
    #uh oh this is hard coding for once case
    #left_most_x_inter = rect1_bottom_right - rect2_bottom_left 
    #top_most_y_inter = rect1_top_right - rect2_top_left
    
    #are rec intersecting?
    rec1_bottom_right < rec2_bottom_left or 
    return rect_int

print rec_intersection(([0, 0], [2, 1]), ([1, 0], [3, 1]))

