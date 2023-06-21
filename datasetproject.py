# Amirhossein Mokhbery           9911323

import threading
import pandas
import time

def fun1():
    
    # Read file and convert to dataframe
    datafarame = pandas.read_csv('D:\VScode\OS project\dataset.csv')
    # find the maximum values
    max = datafarame.loc[datafarame['Global_Sales'].idxmax()]
    print("Max value : \n")
    print(max)


def fun2():
    
    # Read file and convert to dataframe
    datafarame = pandas.read_csv('D:\VScode\OS project\dataset.csv')
    # find the minimum values
    min = datafarame.loc[datafarame['Global_Sales'].idxmin()]
    print("Min value : \n")
    print(min)


def main():
    
    # The current time when the code below executes
    start = time.time()
    fun1()
    print("------------------------------------------------------------")
    fun2()
    # The current time when the code below executes
    end = time.time()
    
    print("============================================================")
    print("time : ",end - start)
          
        
if __name__ == '__main__':
    main()
