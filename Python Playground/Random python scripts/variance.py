#! /usr/bin/env python3
import math

#Declare the variables
numb = [11, 74, 62, 67, 63, 82, 10, 96, 25, 87, 53, 63, 29, 36, 55, 78, 14, 68, 63, 35, 57, 55, 72, 88, 26, 19, 29, 33, 66, 46]
numb2 = [23, 18, 15, 15, 21, 28, 29, 27]
variance = 0
variance2 = 0
onmean = 0
onmean2 = 0
Svariance = 0


#Calculate mear
for i in range(len(numb)):
    onmean += numb[i]
   # onmean2 += numb2[i]

mean = onmean / len(numb)
#mean2 = onmean2 / len(numb2)



#calculate Variancen numerator
for i in range(len(numb)):
    variance += (numb[i] - mean)**2
   # variance2 += (numb2[i] - mean2)**2

#covarianve numerator
'''for i in range(len(numb)):
    Svariance += (numb[i] - mean) * (numb2[i] - mean2)'''

#sCovariance = Svariance / (len(numb) - 1)
SVariance  = variance / len(numb)
sDeviation = math.sqrt(SVariance)
sDev1 = mean + sDeviation
sDev2 = mean + (2 * sDeviation)
sDev3 = mean + 3 * sDeviation

negSdev1 = mean - sDeviation
negSdev2 = mean - 2 * sDeviation
negSdev3 = mean - 3 * sDeviation

count1 = 0
count2 = 0
count3 = 0

for i in numb:
    if i > negSdev1 and i < sDev1:
        count1 += 1
    elif i > negSdev2 and i < sDev2 :
        count2 += 1
    elif i > negSdev3 and i < sDev3:
        count3 += 1

print("Mean x: " + str(mean))
#print("Mean y: " + str(mean2))
print("Variance x: " + str(SVariance))
#print("Variance y: " + str(variance2))
#print("Sample Covariance: " + str(sCovariance))
print("Standard Deviation: " + str(sDeviation))
print("SD 1: " + str(sDev1))
print("SD 1: " + str(negSdev1))
print("SD 2: " + str(sDev2))
print("SD 2: " + str(negSdev2))
print("SD 3: " + str(sDev3))
print("SD 3: " + str(negSdev3))

print("Number of items in 1 sd: " + str(count1) + " and percent: " + str((count1/len(numb) * 100))) 
print("Number of items in 2 sd: " + str(count2) + " and percent: " + str((count2/len(numb) * 100))) 
print("Number of items in 3 sd: " + str(count3) + " and percent: " + str((count3/len(numb) * 100))) 

