import numpy as np
import matplotlib.pyplot as plt
marks=[45,36,86,57,53,92,65,45]
#Store the scores in the 'marks' array
print (sorted(marks))
#Prints the data in the Marks array in positive order
plt.boxplot(marks,vert=True,notch=False,showmeans=True,meanline=False,showbox=True,
            showcaps=True,showfliers=True,patch_artist=True,boxprops={'facecolor':'skyblue'})
#gave plot a title "marks"
plt.title('marks')
plt.show()
average=np.mean(marks)
print ('average of marks is:',int(average))
if average<60:
   print ('Rob failed the exam')
else:print ('Rob passed the exam')
