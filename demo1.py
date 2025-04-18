#python

import methods

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
    print("fitting:")
    print(p)
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
        #print(X)
        Y = np.array(y)
        #print(Y)
        W = np.linalg.solve(X,Y)
        #print(W)
        return W
    else:
        return 0
    
def draw(w,x):
    rank = len(w)
    if rank > 0:
        y=0
        for i in range(0,rank-1):
           y = y + (x**i)*(w[rank-i-1])
           
        y = y + w[rank]
        return y

    else:
        return 0


def lcomp(g,h):
    rank = len(g)
    if rank==len(h) and rank > 0:

        print("need to find solution for the difference-line")
        
    else:
        return -1




#what construct can store a spline? its a 4xL set of x and y values, right?

#read X0,Y0,X1,Y0 - this is a 'rung' in the ladder. element 4 is the start of the next rung. X0Y0 is always the left point of the rung if we go up the array. there needs to be checks that there isn't any width 0 anywhere, or inverted roads.
#now, what is your goal? follow the 'edge' of the spline with a constant distance from it.


#p = [1.2,0,1.2,1,1.2,2 etc...] - 2xL


#try this first, then add time


w_target = 0.25 

margin = 0.01 #1% accuracy desired

#outward journey -


#generate values for P such that they pass comparison to w_target sufficiently

#could generate random P values, iterate, correct
#or zero values


#iterate through list, check fit, adjust 
#now i realise - the initial guess can simply be the railroad route, or railroad route with event modifications. then, the algorithm only improves it.


x0 = -2
y0 = -7
x1 = -1
y1 = 5
x2 = 0
y2 = 50

x3 = 10
y3 = 5

x4 = 2
y4 = -7
#x5 = 6
#y5 = 8

#a = np.array([[x0**2,x0,1],[x1**2,x1,1],[x2**2,x2,1],[x3**2,x3,1],[x4**2,x4,1],[x5**2,x5,1]])
#b = np.array([y0,y1,y2,y3,y4,y5])

a = np.array([[x0**2,x0,1],[x1**2,x1,1],[x2**2,x2,1]])
b = np.array([y0,y1,y2]) 


SL = np.linalg.solve(a,b)

#print(SL)
pr = [[x0,y0],[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
#py = fit(pr)


p2 = [[x0,y0],[x1,y1],[x2,y2]]
py = fit(pr)

print("degree of polynomial: %d"%(len(py)-1))
print("polynomial coefficients:")
print(py)

print(methods.NewtonIsRoot(py))


a0 = 0
b0 = 2
a1 = 1
b1 = 3
a2= 2
b2= 6
a3 = 3
b3 = 11
a4 = 4
b4 = 18
p3 = fit([[a0,b0],[a1,b1],[a2,b2],[a3,b3],[a4,b4]])


p4 = fit([[0,10],[1,11],[2,26],[3,91],[4,266]])


#methods.Overlap(p3,p4)


#iteratively try to find a polynomial that doesn't overlap with p4

overlap = 1
degree = 1

R = 10
T= 10

rotate_attempts = 0
translate_attempts = 0
attempts = 0
coff_select = 0

coffs = np.array([R,T])

while overlap == 1:
    #coffs = np.array([R,T])
    print("trying:")
    print(coffs)
    if methods.Overlap(coffs,p4) == 0:
        overlap = 0
        print("fit found")
    else:
        for coffitem in range(0,degree+1):
            ranitem = float(random.randint(2,10))/8.0
            print("modifying coefficient %f with %f"%(coffs[coffitem],ranitem))
            coffs[coffitem] = coffs[coffitem]*-1.0*ranitem + 0.22 #nparray automatically rounds values to ints
            print("its now %f"%coffs[coffitem])
        attempts = attempts + 1
        print("unsuccessful")

    if attempts%10 == 0:
        degree=degree+1
        coffs = np.append(coffs,10)
        

    if attempts > 50:
        print("failed to find fit")
        break


    







def fitcompare(x0,x1,y0,y1,s0,s1):
    print("function")    



