def Joke(listik=[]):
    floatus=[]
    for x in listik:
        floatus.append(round(x%1,6))
    print(floatus)
    return(max(floatus)-min(floatus))

listus=[0.1341,4.231,5.321,0.29]
print(Joke(listus))
