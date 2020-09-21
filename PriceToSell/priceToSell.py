#!/bin/python3

import math
import os
import random
import re
import sys



import numpy as np

def valuation(reqArea, area, price):
    def removeOutliers(areaOut, priceOut):
        newArea = []
        newPrice = []
        visited = []
        duplicates = {}
        for i in range(len(areaOut)):
            compList = [priceOut[x] for x in range(len(areaOut)) if areaOut[i] == areaOut[x] and i != x]

            if not compList:
                if areaOut[i] in newArea:
                    if areaOut[i] in duplicates:
                        val = duplicates.get(areaOut[i])
                        val[0] += priceOut[i]
                        val[1] += 1
                        duplicates[areaOut[i]] = val
                    else:
                        duplicates[areaOut[i]] = [priceOut[i], 2]
                else:
                    newArea.append(areaOut[i])
                    newPrice.append(priceOut[i])
            else:
                if (abs(priceOut[i] - (sum(compList)/(len(compList)))) > (3 * np.std(compList))) == False:
                    if areaOut[i] in newArea:
                        if areaOut[i] in duplicates:
                            val = duplicates.get(areaOut[i])
                            val[0] += priceOut[i]
                            val[1] += 1
                            duplicates[areaOut[i]] = val
                        else:
                            duplicates[areaOut[i]] = [priceOut[i], 2]
                    else:
                        newArea.append(areaOut[i])
                        newPrice.append(priceOut[i])

        return newArea, newPrice, duplicates

    if reqArea in area:
        areasEqualed = [price[i] for i in range(len(area)) if area[i] == reqArea]
        return int(sum(areasEqualed)/len(areasEqualed))
    
    uniques_Area = []
    uniques_Price = []
    nonUniques_Area = []
    nonUniques_Price = []
    visited = []
    
    for i in range(len(area)):
        if area[i] not in uniques_Area and area[i] not in visited:
            uniques_Area.append(area[i])
            uniques_Price.append(price[i])
            visited.append(area[i])
        else:
            if area[i] in uniques_Area:
                index = uniques_Area.index(area[i])

                nonUniques_Area.append(area[i])
                nonUniques_Price.append(price[i])
                nonUniques_Area.append(area[i])
                nonUniques_Price.append(uniques_Price[index])

                uniques_Area.remove(area[i])
                uniques_Price.remove(uniques_Price[index])
            else:
                nonUniques_Area.append(area[i])
                nonUniques_Price.append(price[i])
    
    a, b, dp = removeOutliers(nonUniques_Area, nonUniques_Price)
    a += uniques_Area
    b += uniques_Price

    if min(a) < reqArea < max(a):
        y1_index = a.index(min([i for i in a if i > reqArea]))
        y2_index = a.index(max([i for i in a if i < reqArea]))
        interSquare = [a[y1_index], a[y2_index]]
        interPrice = [b[y1_index], b[y2_index]]

        for i in range(len(interSquare)):
            if interSquare[i] in dp:
                dpVal = dp.get(interSquare[i])
                interPrice[i] = (interPrice[i] + dpVal[0])/dpVal[1]
        
        print(reqArea)
        print(interSquare)
        print(interPrice)

        ans = interPrice[0] + (((interPrice[1]-interPrice[0])* (reqArea - interSquare[0]))/(interSquare[1] - interSquare[0])) 
        print("Internpolate : ", int(round(ans)))
        return int(round(ans))
    
    else:
        #ExtraPolate
        if max(a) < reqArea:
            y1_index = a.index(max(a))
            y2_index = a.index(max([i for i in a if i != a[y1_index]]))
            interSquare = [a[y2_index], a[y1_index]]
            interPrice = [b[y2_index], b[y1_index]]
        else:
            y1_index = a.index(min(a))
            y2_index = a.index(min([i for i in a if i != a[y1_index]]))
            interSquare = [a[y2_index], a[y1_index]]
            interPrice = [b[y2_index], b[y1_index]]
    
        for i in range(len(interSquare)):
            if interSquare[i] in dp:
                dpVal = dp.get(interSquare[i])
                interPrice[i] = (interPrice[i] + dpVal[0])/dpVal[1]
        
        print(reqArea)
        print(interSquare, interPrice)
        ans = interPrice[1] + (reqArea - interSquare[1]) * ((interPrice[1] - interPrice[0])/(interSquare[1]-interSquare[0]))
        if ans > 1000000:
            ans = 1000000
        if ans < 1000:
            ans = 1000
        print("Extrapolate : ", int(round(ans)))
        return int(round(ans))


if __name__ == '__main__':