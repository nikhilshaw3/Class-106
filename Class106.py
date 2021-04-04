import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
  iceCream_sales = []
  ColdDrink_sales = []
  with open(data_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      iceCream_sales.append(float(row("Temaperature")))
      ColdDrink_sales.append(float(row("Cold drink sales( ₹ )")))
      return{"x":iceCream_sales,"y":ColdDrink_sales}


def findCorrelation(data_source):
  correlation = np.corrcoef(data_source["x"],data_source["y"])
  print("Correlation Between Temperature vs IceCream Sales is ", correlation[0,1])


def setup():
  data_path ="IceCream.csv"
  data_source = getDataSource(data_path)
  findCorrelation(data_source)


setup()