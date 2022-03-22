n=1
#Start with one cut
p=0
#p stores the maximum number of pieces of pizza that can be cut
while p < 64:#Continue cutting when the maximum number of pieces is less than 64
      p=(n**2+n+2)/2
#Calculate the maximum number of pieces that can be cut
      print (int(p),"pieces of pizza that can be cut for",int(n),"cut")
#print the maximum number of pieces that can be cut
      n=n+1
#increase one cut each time
print ("that is enough for the whole IBI class (64 numbers)")
#Stop until the maximum number of pieces is greater than or equal to 64
#print that's enough to give IBI a whole class
