'''
I had help from instructor Robert Young in IBI1 lecture to create a definition
I had help to change decimals to fractions and keep two decimal places from
https://blog.csdn.net/qq_39353327/article/details/104903621[access:2022/4/20]
'''
import re
DNA= input('DNA sequence string:')
DNA = DNA.upper()

def content (x):
    group = re.findall(x,DNA)
    count = len(group)
    result = "%.2f%%" % (count/len(DNA)*100)
    print('the content of',x,'is:',result)

content('A')
content('T')
content('C')
content('G')



