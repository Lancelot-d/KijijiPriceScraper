import os
from Data import Data
import globalVar

if __name__ == "__main__":
    os.system("scrapy crawl spider1 -O "+ globalVar.fileName)

    dataPath = os.path.abspath(os.getcwd() + "/"+globalVar.fileName)
    data = Data(dataPath)
    data.createChart()





