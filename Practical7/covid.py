import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
covid_data = pd.read_csv("full_data.csv")
input("Enter 1 to display the first and third columns from Rows 10-20:")
print(covid_data.iloc[9:20, 0:3:2])
input("Enter 1 to display the all rows corresponding to Afghanistan:")
for i in range(0, 7995):
    if covid_data.iloc[i, 1] == "Afghanistan":
        print(i, covid_data.iloc[i, 4])
input("Enter 1 to display the mean number of new cases and new deaths in China:")
china_date = pd.read_csv("china_new_data.csv")
print('the mean number of new cases in China is', np.average(china_date.iloc[:, 2]))
print('the mean number of new deathes in China is', np.average(china_date.iloc[:, 3]))
input("Enter 1 to display  the boxplot of new cases and new deaths in China worldwide:")
china_new_cases = china_date.iloc[:, 2]
china_new_deathes = china_date.iloc[:, 3]
color = ['skyblue','pink']
plt.boxplot([china_new_cases, china_new_deathes], notch=False, patch_artist=True, boxprops={'facecolor':'skyblue'})
plt.title('boxplot of new cases and new deaths in China')
plt.show()
input("Enter 1 to display the plot of both new cases and new deaths in China over time:")
china_dates = china_date.iloc[:, 0]
plt.plot(china_dates, china_new_cases, "r+")
plt.plot(china_dates, china_new_deathes, "b+")
plt.title('new cases and new deaths in China over time')
plt.xticks(china_dates.iloc[0:len(china_dates):4], rotation=-90)
plt.legend(['new cases in China', 'new deathes in China'], loc='upper left')
plt.show()
input("Enter 1 to display a plot of total number of COVID cases over time in South korea, Kenya and Colombia:")
SouthKorea_date = pd.read_csv("SouthKorea_date.csv")
Kenya_date = pd.read_csv("Kenya_date.csv")
Colombia_date = pd.read_csv("Colombia_date.csv")
SouthKorea_total_date = SouthKorea_date.iloc[:,2]
Kenya_total_date = Kenya_date.iloc[:,2]
Colombia_total_date = Colombia_date.iloc[:,2]
date1 = SouthKorea_date.iloc[:,0]
date2 = Kenya_date.iloc[:,0]
date3 = Colombia_date.iloc[:,0]
plt.plot(date1,SouthKorea_total_date,'r+')
plt.plot(date2,Kenya_total_date,'b+')
plt.plot(date3,Colombia_total_date,'y+')
plt.title('the total number of COVID cases over time in all three')
plt.legend(['total date of South Korea', 'total date of Kenya', 'total date of Colombia', ], loc='upper left')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.show()
