#!/usr/bin/env python

"""

Curves y1 and y2

Finds K (scale factor) to superimpose these 2 curves!)

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.optimize import leastsq

x = np.linspace(1, 10, 100)
y1 = np.exp(x/5)
y2 = (y1 + np.random.normal(0, 0.1, 100) ) * 2.2

#f = interpolate.UnivariateSpline(x, y2, s=0)
f1 = interpolate.interp1d(x, y1)
f2 = interpolate.interp1d(x, y2)

def residuals1(k, y, x):
    """
    k = scale factor
    """
    err = y-k*f1(x)
    return err

def peval1(x, k):
    return k*f1(x)

def residuals2(k, y, x):
    """
    k = scale factor
    """
    err = y-k*f2(x)
    return err

def peval2(x, k):
    return k*f2(x)

plsq1 = leastsq(residuals1, 1, args=(y2, x))
print "Scale factor tu superimpose y2 to y1: K = ",plsq1[0]

plsq2 = leastsq(residuals2, 1, args=(y1, x))
print "Scale factor tu superimpose y1 to y2: K = ",plsq2[0]

plt.plot(x,y1,label='y1')
plt.plot(x,y2,label='y2')

xnew = np.linspace(2, 9, 10)
print len(xnew), len(peval1(xnew,plsq1[0]))
plt.plot(xnew,peval1(xnew,plsq1[0]), 'o', label='Fit1. K=%.2f'%plsq1[0][0])
plt.plot(xnew,peval2(xnew,plsq2[0]), 'o', label='Fit2. K=%.2f'%plsq2[0][0])

plt.plot(x,y1*plsq1[0][0],label='y1*K')
plt.plot(x,y2*plsq2[0][0],label='y2*K')


plt.legend(loc=2)
plt.show()