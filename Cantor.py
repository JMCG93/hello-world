from matplotlib import pyplot as plt
import numpy as np

#This is the cantor script.  It is a script that will create the cantor set
#up to a certain 'n' and plot the intervals on an axis.  The higher the n, the
#more plots at varying levels of zoom.

#Explain Cantor set and get number of iterations from user.
print("\n\nA Brief Explanation of the Cantor Set:\n")
print("The cantor set is a set made by taking")
print("the interval [0, 1] and repeatedly doubling the number of intervals by ")
print("removing the middle third.\n")
print("So, after the first division we are left with [0, 1/3] U [2/3, 1]\n")
print("After the second division we are left with [0, 1/9] U [2/9, 1/3] U ")
print("[2/3, 7/9] U [8/9, 1]")
print("If we denote the unions of intervals after n interations of this division")
print("process I_n, then the nth Cantor set, C_N, is the intersection of I_n")
print("for n = 0...N.  The Cantor Set is C_N as N goes to infinity.\n")
iterations = input("How many iterations would you like to perform?  ")

#Define function to remove middle third of a given interval
def removeMiddleThird(lower, upper):
    thirdDistance = (upper-lower)/3.0
    return np.array([lower, lower+thirdDistance, upper-thirdDistance, upper])

def makeCantorInterval(n):
    newInterval = np.array([0.0, 1.0])
    for x in range(n):
        print(x)
        oldInterval = np.copy(newInterval)
        newInterval = np.delete(newInterval, range(newInterval.size))
        for y in range(0, oldInterval.size, 2):
            newSplit = removeMiddleThird(oldInterval[y],oldInterval[y+1])
            newInterval = np.append(newInterval, newSplit)
    return newInterval
cantorIntervals = makeCantorInterval(iterations)

#Create histogram of lower bounds for intervals.
histograms=plt.figure("Bounds Histograms")
plt.subplot(211)
b=(np.array(range(2**(iterations+1)))%2)==0
plt.hist(x=cantorIntervals[b], bins=200, range=(0,1))
plt.title('Histogram of lower bounds')

#Create histogram of upper bounds for intervals.
plt.subplot(212)
b=(np.array(range(2**(iterations+1)))%2)==1
plt.hist(x=cantorIntervals[b], bins=200, range=(0,1))
plt.title('Histogram of upper bounds')

#Create bar chart to represent the cantor intervals.
#Note that since C_n is the intersection of all successive interval groups
    #that this plot will represent the Cantor set at the desired number of
    #iterations.
barChart=plt.figure("Cantor Intervals")
barWidth = cantorIntervals[1]
b=(np.array(range(2**(iterations+1)))%2)==0
heights = np.ones(2**(iterations))
plt.bar(left=cantorIntervals[b],height=heights, width=barWidth)
plt.title('Interval length: '+str(barWidth)+'\nNumber of Intervals: '+str(heights.size))

plt.show()
plt.close()
