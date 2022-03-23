#creat a dictinary to store the paternal_age and chd 
dictinary={'30':1.03,'35':1.07,'40':1.11,'45':1.17,'50':1.23,'55':1.32,
           '60':1.42,'65':1.55,'70':1.72,'75':1.94}
#print the dictinary
print (dictinary)
import numpy as np
import matplotlib.pyplot as plt
#paternal_age stores the father’s age at the time of the offspring birth
paternal_age=[30,35,40,45,50,55,60,65,70,75]
#chd stores the risk of congenital heart disease for the offspring
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
#Determine the x and y value of the scatter plot
x=np.array(paternal_age)
y=np.array(chd)
#construct a scatter plot from the data
#I had help from instructor Robert Young in IBI1 lecture to create a scatter.
#I had help to change the color from https://www.runoob.com/matplotlib/matplotlib-scatter.html
plt.scatter(x,y,marker='o',c="green")
plt.xlabel('age of father')
plt.ylabel('risk of offspring')
plt.show()
#print the risk of congenital heart disease in the offspring of a father of a given age from the input list
print (dictinary['40'])
