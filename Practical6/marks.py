import numpy as np
import matplotlib.pyplot as plt
marks=[45,36,86,57,53,92,65,45]
#Store the scores in the 'marks' array
print (sorted(marks))
#Prints the data in the Marks array in positive order
#I had help from instructor Robert Young in IBI1 lecture to create a boxplot.  
#I had help to change the color from https://blog.csdn.net/weixin_40683253/article/details/87857194
plt.boxplot(marks,labels= ['Rob'], vert=True,notch=False,showmeans=True,meanline=False,showbox=True,
            showcaps=True,showfliers=True,patch_artist=True,boxprops={'facecolor':'skyblue','color':'blue'})
#gave plot a title "marks"
plt.title('marks')
plt.xlabel('Person')
plt.ylabel('Marks')
plt.show()
#I had help to calculate the average from https://blog.csdn.net/reyyy/article/details/108279103
average=np.mean(marks)
#print the average
print ('average of marks is:',int(average))
#Judge whether Rob has passed
if average<60:
   print ('Rob failed the exam')
else:print ('Rob passed the exam')
