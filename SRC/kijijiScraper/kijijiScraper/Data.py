import matplotlib.pyplot as plt
import csv

class Data():

    def __init__(self,csvPath):
        self.file = open(csvPath)

    def extractData(self):
        csvreader = csv.reader(self.file)

        price_list = []
        for row in csvreader:
            onlyNumber = True;
            for carac in row:
                if(carac.isalpha()):
                    onlyNumber=False
            if(onlyNumber):price_list.append(float(row[0].replace(",",".")))

        return price_list

    #remove price to far from mean price
    def cleanData(self, price_list, mean):
        price_list_update = []
        for price in price_list:
            i = mean*0.8
            y=mean*1.2
            if(price >= mean*0.4 and price <= mean*1.5):
                price_list_update.append(price)

        return price_list_update

    def getMean(self, price_list):
        mean = 0

        for price in price_list:
            mean+=price

        mean /= len(price_list)
        return mean

    def createChart(self):
        data = self.extractData()
        mean = self.getMean(data)
        data = self.cleanData(data, mean)
        mean = self.getMean(data)

        plt.plot(data, color ="b")
        plt.plot([0, len(data)],[mean, mean], color="red")
        plt.xlabel("Quantity of product : "+str(len(data)))
        plt.ylabel("Price")
        plt.title("Mean price : "+str(int(mean)) + " $")
        plt.show()

