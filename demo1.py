#python

"""
a spline is given from an opendrive file.

the agent must traverse down its middle

currently, the route given by opendrive is converted into a time-position table, and a driving module on the agent figures out how it should maneuvre towards each timepoint.

if there is a stop event planned in advance, that gets included in the timepos table.

if there is a conflict, that gets calculated in advance as well.

is such a table the end-goal?

the human has to figure out, how to include the stop event in the TP, how to include an overtake.

we want some kind of unified algorithm, that can interpret everything it needs to from a map.

the map should show the full geometric situation on the road, signage, parking spots, road markings.

the algorithm should figure out how to navigate them.

if a new sign is introduced, or, for example, a randomly-shaped object with erratic behaviour is added, the unified algorithm should be able to guess like a human how to navigate it.

so, we start with a curved spline and make an attempt at an algorithm that figures out a sensible way to drive it, without having to be given the actual rail-route to follow

"""


import random
import numpy as np

def fit(p):
    L = len(p)
    if L > 0:
        a=[]
        b=[]
        y=[]
        for i in range(0,L):
            y.append(p[i][1])
            for j in range(0,L):
                a.append(p[i][0]**j)

            b.append(a[:])
            a=[]



        X = np.array(b)
        Y = np.array(y)
        W = np.linalg.solve(X,Y)
        return W
    else:
        return 0
    


#what construct can store a spline? its a 4xL set of x and y values, right?

#read X0,Y0,X1,Y0 - this is a 'rung' in the ladder. element 4 is the start of the next rung. X0Y0 is always the left point of the rung if we go up the array. there needs to be checks that there isn't any width 0 anywhere, or inverted roads.

ROAD1 = [0,0,2,0,0,2,5,2,0,4,3,4,0,6,2,6,0,8,2,8,0,10,2,10]

n = int(len(ROAD1)/4)

#now, what is your goal? follow the 'edge' of the spline with a constant distance from it.


#p = [1.2,0,1.2,1,1.2,2 etc...] - 2xL


#try this first, then add time


w_target = 0.25 

margin = 0.01 #1% accuracy desired

#outward journey -


#generate values for P such that they pass comparison to w_target sufficiently

#could generate random P values, iterate, correct
#or zero values

print(n)
    
p=[]
for i in range(0,n):
    p.append(random.random()*100)
    p.append(random.random()*100)
    print(ROAD1[i*2])
#we have a 'random' p

#iterate through list, check fit, adjust 
#now i realise - the initial guess can simply be the railroad route, or railroad route with event modifications. then, the algorithm only improves it.


x0 = 2
y0 = 4
x1 = 10
y1 = -50
x2 = 20
y2 = 8

x3 = 9
y3 = 11

x4 = 7
y4 = 6
x5 = 6
y5 = 8

#a = np.array([[x0**2,x0,1],[x1**2,x1,1],[x2**2,x2,1],[x3**2,x3,1],[x4**2,x4,1],[x5**2,x5,1]])
#b = np.array([y0,y1,y2,y3,y4,y5])

a = np.array([[x0**2,x0,1],[x1**2,x1,1],[x2**2,x2,1]])
b = np.array([y0,y1,y2]) 


SL = np.linalg.solve(a,b)

print(SL)
pr = [[x0,y0],[x1,y1],[x2,y2],[x3,y3],[x4,y4],[x5,y5]]
py = fit(pr)
print(py)


def fitcompare(x0,x1,y0,y1,s0,s1):
    print("function")    

