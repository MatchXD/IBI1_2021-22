#Sum is used to store the triangle sequence
sum = 0
#When the number of rows is less than or equal to 10,loop continues
#Increase one number of rows each time
for i in range(1,11):
#calculates the triangle sequence in this row
   sum = sum + i
#print the triangle sequence corresponding to the current rows after each calculation
   if i == 1:
      print(i,"row:",sum)
#when row==1,print "row"
#when row>1,print "rows"
   else: print(i,"rows:",sum)
