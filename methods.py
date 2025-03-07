#solver methods

def NewtonIsRoot(pol):
    fakedegree = len(pol)
    


    #calculate deriv coefficients

    ders =[]

    for d in range(0,fakedegree):
        ders.append(pol[d]*(fakedegree-d-1))
    #ders.append(0)
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
        
        y = 0
        der_ins = 0

        for n in range(0,fakedegree):
            y = y + pol[n]*(x**(fakedegree-1-n))

        print("guessing %f which gave %f"%(x,y)) 
        
        if (y < 0.05 and y > -0.05):
            acc=1
            isRoot = 1
            return isRoot
        else:
            pointless = pointless + 1
            subpointless = subpointless + 1
            if subpointless > subatlimit:
                
                x = -10*x 
                subpointless=0

        for nd in range(0,fakedegree-2):
            der_ins = der_ins + ders[nd]*(x**(fakedegree-nd))
            #print("x is %f, derX is %f"%(x,ders[nd]))
        der_ins = der_ins + ders[nd]
        if der_ins == 0:
            #print("local mininum reached")
            #subpointless = subpointless + subatlimit
            der_ins=0.1
        dx = y/der_ins

        x = x - dx
        
    
    
    return isRoot



def Overlap(a,b):
    print("---in Overlap")
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
    print(cmax)
    print(cmin)
    print("expecting change at %i"%(maxL-minL))
    for j in range(0,maxL):
        res.append(0)

    for i in range(maxL-1,0,-1):
        print(i)
        
        if i<=maxL-minL:
            res[i] = cmax[i]

        else:
            res[i] = cmax[i]-cmin[i]

            
    print(res)
