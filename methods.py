#solver methods

def NewtonIsRoot(pol):
    fakedegree = len(pol)
    
    #print("received into NewtonIsRoot polynomial:")
   # print(pol)

    #calculate deriv coefficients

    ders =[]

    for d in range(0,fakedegree):
        ders.append(pol[d]*(d))
    #ders.append(0)
    print("++++ in newton")
    print("derivatives:")
    print(ders)
    x = 0 
    y = 100
    dx = 0
    acc = 0
    pointless = 0 
    subpointless=0
    atlimit = 50
    subatlimit = 30
    searchrange = 0

    isRoot = 0

    while acc == 0 and pointless < atlimit:
        
        y = pol[0]
        der_ins = 0

        for n in range(1,fakedegree):
            
            y = y + pol[n]*(x**(fakedegree-n+1))
            #print("at n = %i, coefficient is %f"%(n,fakedegree-1-n))
        #print("guessing %f which gave %f"%(x,y)) 
        
        if (y < 0.05 and y > -0.05):
            acc=1
            isRoot = 1
            return isRoot
        elif (y>(2**30)):
            x = -0.0001*x
        else:
            pointless = pointless + 1
            subpointless = subpointless + 1
            if subpointless > subatlimit:
                
                x = -10*(x+1) 
                subpointless=0

        for nd in range(1,fakedegree-1):
            der_ins = der_ins + ders[nd]*(x**(fakedegree-nd))
            #print("x is %f, dertem is %f"%(x,der_ins))
        der_ins = der_ins + ders[nd]
        #print("final derterm is %f"%der_ins)
        if der_ins == 0:
            #print("local mininum reached")
            #subpointless = subpointless + subatlimit
            x=-10*(x+1)
        else:
            dx = y/der_ins

            x = x - dx
        
    
    
    return isRoot



def Overlap(a,b):
    #print("---in Overlap")
    aL = len(a)
    bL = len(b)
    maxL = 1
    res=[]

    cmax=[]
    cmin=[]
    if aL > bL:
        maxL = aL
        minL = bL
        cmax = a[:]
        cmin = b[:]
    else:
        maxL = bL
        minL = aL
        cmax = b[:]
        cmin= a[:]
    #print(cmax)
    #print(cmin)
    #print("expecting change at %i"%(maxL-minL))
    for j in range(0,maxL):
        res.append(0)

    for i in range(0,maxL):
       #print(i)
        
        if i<=(maxL-minL-1):
            res[i] = cmax[i]

        else:
            res[i] = cmax[i]-cmin[i-(maxL-minL)]

            
    #print(res)

    #print(NewtonIsRoot(res))
