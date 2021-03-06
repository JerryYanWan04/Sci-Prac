
def mysqrt2(x):
    s = 1.
    kmax = 100
    tol = 1e-14
    for k in range(kmax):
        print "Before iteration %d, s = %20.15f" % (k, s)
        s0 = s
        s = 0.5 * (s + x/s)
        delta_s = s - s0
        if abs(delta_s / x) < tol:
            break
    
    print "After %d iteration,  s = %20.15f" %(k+1, s)
