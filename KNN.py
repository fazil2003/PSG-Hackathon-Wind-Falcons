import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def kClosest(points):
        y = quick_select(points, 5)
        return y

def quick_select(points, k):
        """Perform the QuickSelect algorithm on the list"""
        left, right = 0, len(points) - 1
        pivot_index = len(points)
        while pivot_index != k:
            # Repeatedly partition the list
            # while narrowing in on the kth element
            pivot_index = partition(points, left, right)
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1
        
        # Return the first k elements of the partially sorted list
        return points[:k]
    
def partition(points, left, right):
        """Partition the list around the pivot value"""
        pivot = choose_pivot(points, left, right)
        pivot_dist = squared_distance(pivot)
        while left < right:
            # Iterate through the range and swap elements to make sure
            # that all points closer than the pivot are to the left
            if squared_distance(points[left]) >= pivot_dist:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1
        
        # Ensure the left pointer is just past the end of
        # the left range then return it as the new pivotIndex
        if squared_distance(points[left]) < pivot_dist:
            left += 1
        return left
    
def choose_pivot(points, left, right):
        """Choose a pivot element of the list"""
        return points[left + (right - left) // 2]
    
def squared_distance(point):
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2
def get_2(points,curr=[1,2]):
    m=kClosest(points)
    m1=[[0,0],[0,0]]
    m1[0][0]=m[0][0]+curr[0]
    m1[0][1]=m[0][1]+curr[1]
    m1[1][0]=m[1][0]+curr[0]
    m1[1][1]=m[1][1]+curr[1]
    return m1

data = pd.read_csv("2013.csv")
data.head()
k=data.values.tolist()
# for i in k:
#   d[(i[0]+' '+i[1]).tolower()]=i[-1]
# for i in

def geocode(m):
    import requests
    import urllib.parse

    address = m
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

    response = requests.get(url).json()
    try:
        return [response[0]["lon"],response[0]["lat"]]
    except:
        return (0,0)
pts=[]
for i in k:
    pts.append(geocode(i[0]+' '+i[1]))

points=[]
for i in pts:
    points.append(i[1])
city_n=[]
for i in pts:
    city_n.append(i[0])
c=[]
for i in get_2(points):
    c.append(city_n[points.index(i)])
print(c)

