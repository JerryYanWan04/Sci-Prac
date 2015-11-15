x = 10.
s = 1.

for k in range(6):
    print "Before iteration %d, s = %20.15f" % (k, s)
    s = 0.5 * (s + x/s)

print "After %d iteration,  s = %20.15f" %(k+1, s)
