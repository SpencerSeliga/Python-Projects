import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Lab 4 CMPE 365
# Spencer Seliga - 1012599
def bbox(points):
    a = np.zeros((2,2))
    #min values x,y
    a[:,0] = np.min(points, axis=0)
    #max values of x,y
    a[:,1] = np.max(points, axis=0)
    box = [a[0,0], a[0,1], a[1,0], a[1,1]]

    return box

def check_point(point, bounding_box):
    minX = bounding_box[0]
    maxX = bounding_box[1]
    minY = bounding_box[2]
    maxY = bounding_box[3]
    if (minX <= point[0] <= maxX) and (minY <= point[1] <= maxY):
        return True
    else:
        return False

def splithoriz(bounding_box, points): #for the second part I would add max_ratio and Max_coords
    rectangle1 = [bounding_box[0], bounding_box[0]+(bounding_box[1]-bounding_box[0])/2,
                  bounding_box[2], bounding_box[3]]
    rectangle2 = [bounding_box[0] + (bounding_box[1] - bounding_box[0]) / 2, bounding_box[1],
                  bounding_box[2], bounding_box[3]]

    #print rectangle1
    #print rectangle2
    counter1 = 0
    counter2 = 0
    for point in points:
        if(check_point(point, rectangle1) == True):
            counter1 = counter1 + 1
        elif (check_point(point, rectangle2) == True):
            counter2 = counter2 + 1

    area1 = area(rectangle1)
    area2 = area(rectangle2)
    area3 = area(bounding_box)

    ratio1 = counter1/area1
    ratio2 = counter2/area2
    ratio3 = (counter1 + counter2)/ area3

    if (ratio1 > ratio2) and (ratio1 > ratio3):
        final = splitvert(rectangle1, points)
        return final
    elif (ratio2 > ratio1) and (ratio2 > ratio3):
        final = splitvert(rectangle2, points)
        return final
    elif (ratio3 > ratio1) and (ratio3 > ratio2):
        print (bounding_box)
        return bounding_box
    else:
        return bounding_box


def splitvert(bounding_box, points): #For the second part I would add max_ratio, and Max_coords
    rectangle1 = [bounding_box[0], bounding_box[1],
                  bounding_box[2], bounding_box[2]+(bounding_box[3]-bounding_box[2])/2]
    rectangle2 = [bounding_box[0], bounding_box[1],
                  bounding_box[2] + (bounding_box[3] - bounding_box[2]) / 2, bounding_box[3]]
    counter1 = 0
    counter2 = 0
    for point in points:
        if(check_point(point, rectangle1) == True):
            counter1 = counter1 + 1
        elif (check_point(point, rectangle2) == True):
            counter2 = counter2 + 1

    area1 = area(rectangle1)
    area2 = area(rectangle2)
    area3 = area(bounding_box)

    ratio1 = counter1 / area1
    ratio2 = counter2 / area2
    ratio3 = (counter1 + counter2) / area3

    if (ratio1 > ratio2) and (ratio1 > ratio3):
        final = splithoriz(rectangle1, points)
        return final
    elif (ratio2 > ratio1) and (ratio2 > ratio3):
        final = splithoriz(rectangle2, points)
        return final
    elif (ratio3 > ratio1) and (ratio3 > ratio2):
        print (bounding_box)
        return bounding_box
    else:
        return bounding_box


def area(rectangle):
    area = (rectangle[1]-rectangle[0]) * (rectangle[3]-rectangle[2])
    return area

data = np.genfromtxt('points.csv',delimiter=",")
ind = np.lexsort((data[:,1], data[:,0]))
bounding_box = bbox(data[ind])
#max_ratio = 0
#max_coords = [0,0,0,0]
best = splithoriz(bounding_box, data)

coordinates = [[best[0], best[2]], [best[0], best[3]], [best[1], best[2]], [best[1], best[3]]]

Xaxis = data[:,0]
Yaxis = data[:,1]


plt.scatter(Xaxis, Yaxis)
rectangleX = [coordinates[0][0], coordinates[1][0], coordinates[3][0], coordinates[2][0], coordinates[0][0]]
rectangleY = [coordinates[0][1], coordinates[1][1], coordinates[3][1], coordinates[2][1], coordinates[0][1]]
#plt.plot(rectangleX, rectangleY, 'o')
plt.plot(rectangleX, rectangleY, '-')
plt.show()

print (coordinates)


