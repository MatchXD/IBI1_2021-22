from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
from collections import defaultdict
import sys

sys.setrecursionlimit(3000)

DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
dic = defaultdict(list)
n = 0
num = []
num2 = []

def num_go (x):
    global dic2
    for i in range(0,len(dic[x])):
        dic2[dic[x][i]] = 0
        if dic[x][i] in dic:
            num_go(dic[x][i])
    return len(dic2.keys())

for term in terms:
    n += 1
    string1 = term.getElementsByTagName('id')[0]
    ID = string1.childNodes[0].data
    number = len(term.getElementsByTagName('is_a'))
    for i in range(0,number):
        string2 = term.getElementsByTagName('is_a')[i]
        ParentGo = string2.childNodes[0].data
        dic[ParentGo].append(ID)

for term in terms:
    dic2 = {}
    string1 = term.getElementsByTagName('id')[0]
    ID = string1.childNodes[0].data
    num.append(num_go(ID))
    judgment = term.getElementsByTagName('defstr')[0]
    string = judgment.childNodes[0].data
    if 'translation' in string:
        dic2 = {}
        num2.append(num_go(ID))
'''
for term in terms:
    string1 = term.getElementsByTagName('id')[0]
    ID = string1.childNodes[0].data
    while ID in dic:

def num_sub (x):
    global m
    for i in range(0,len(dic[x])):
        m += 1
        sub = dic[x][i]
        if sub in dic:
            num_sub(sub)

x = 0
for term in terms:
    string1 = term.getElementsByTagName('id')[0]
    ID = string1.childNodes[0].data
    while ID in dic:
        for i in range(0,len(dic[ID])):
            x += 1
            ID + str(x)


        num.append(m)
    m = 0

'''
print('the number of terms is:', n)

plt.boxplot(num, vert=True, whis=1.5, patch_artist=True, meanline=False, showbox=True, showcaps=True, showfliers=True,
            notch=False)
plt.title('boxplot of the distribution of child nodes across terms in the Gene Ontology')
plt.xlabel('childNodes')
plt.ylabel('number')
plt.show()

plt.boxplot(num2, vert=True, whis=1.5, patch_artist=True, meanline=False, showbox=True, showcaps=True,
            showfliers=True,notch=False)
plt.title('boxplot of the distribution of child nodes across terms associated with translation')
plt.xlabel('childNodes')
plt.ylabel('number')
plt.show()

print('the translation terms contain a smaller number of child nodes than the overall Gene Ontology')

