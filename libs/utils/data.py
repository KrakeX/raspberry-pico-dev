def getAverageFromList(list):
    return round(sum(list) / len(list),2)

def maintainAmountOfValuesInList(array, value):
    if len(array) <= 10:
        array.append(value)
    else:
        array.pop(0)
        array.append(value)
    return array