def setInRange(value, rangeValue):
    if(value < rangeValue[0]):
        return rangeValue[0]
    elif(value > rangeValue[1]):
        return rangeValue[1]
    else:
        return value
