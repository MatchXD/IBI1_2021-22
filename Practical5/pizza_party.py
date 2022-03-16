#Start with one cut and increase one cut each time  
#calculate the maximum number of pieces of cake that can be cut.  
#Stop until the maximum number of pieces is greater than or equal to 64
n=1
p=0
while p < 64:
      p=(n**2+n+2)/2
      print (str(p),"pieces of pizza that can be cut for",str(n),"cut")
      n=n+1
print ("that is enough for the whole IBI class (64 numbers)")

