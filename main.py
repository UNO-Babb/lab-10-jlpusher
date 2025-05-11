#MapPlot.py
#Name: Jessica Pusher
#Date: 5.11.25
#Assignment: Lab 10

import coffee
import pandas
import matplotlib.pyplot as plt

coffee = coffee.get_coffee()

#print(coffee[0]["Data"]["Scores"]["Total"])

years = []
#scores = []
#volume = []
bags = []

for bean in coffee:
    year = bean["Year"]
    numBags = bean["Data"]["Production"]["Number of bags"]
    #bagWeight = bean["Data"]["Production"]["Bag weight"]
    #totalVolume = numBags * bagWeight
    #totalVolume = int(totalVolume) #don't want to deal with decimals
    #score = bean["Data"]["Scores"]["Total"]
    #if totalVolume > 100:
    years.append(year)
    bags.append(numBags)
    #volume.append(totalVolume)

    #scores.append(score)
    #print(year, totalVolume)

#df = pandas.DataFrame({"Flavor": flavors,"Score": scores})

#print(df)
#df.plot(kind = 'scatter', x = 'Flavor', y = 'Score')
#plt.plot(years, bags, 'ro')
#plt.savefig("output")