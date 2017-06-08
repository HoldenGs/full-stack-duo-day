#!/usr/bin/python3

'''

Find the closest pairs of points in an array of 2D or 3D points

Usage:
./find_pair.py

'''


def find_pair(array=[]):
    dimensions = 2
    if len(array) == 0:
        return "No array found"
    if len(array[0]) == 3:
        dimensions = 3
    if dimensions == 3:
            distance = ((array[0][0] - array[1][0])**2 +
                        (array[0][1] - array[1][1])**2 +
                        (array[0][2] - array[1][2])**2)**0.5
    else:
        distance = ((array[0][0] - array[1][0])**2 +
                    (array[0][1] - array[1][1])**2)**0.5
    closest_pair = ((0, 1), distance)
    for i1, point_1 in enumerate(array):
        i2 = i1 + 1
        while i2 < len(array):
            point_2 = array[i2]
            if dimensions  == 3:
                new_distance = ((point_1[0] - point_2[0])**2 +
                                (point_1[1] - point_2[1])**2 +
                                (point_1[2] - point_2[2])**2)**0.5
            else:
                new_distance = ((point_1[0] - point_2[0])**2 +
                                (point_1[1] - point_2[1])**2)**0.5
            if new_distance < closest_pair[1] and i1 != i2:
                closest_pair = ((i1, i2), new_distance)
            i2 += 1
    return closest_pair


array = [(1, 5), (1, 7), (1, 8), (1, 2)]

new_array = [(3, 5), (4, -1), (7, 2), (1, 8), (8, 9)]

print(find_pair(new_array))
