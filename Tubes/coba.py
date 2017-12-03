from __future__ import division
import nltk
from bs4 import BeautifulSoup as BS
from xml.etree import cElementTree as ET
import xml.dom.minidom
import string
import math
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
#nltk.download('punkt')
# nltk.download('stopwords')

#inisialisasi file
kelas = 'B:/Kul/Teksmin/dataset/topic/Training101.txt'
testfolder = 'B:/Kul/Teksmin/dataset/topic/Test101.txt'

#Mengambil data nama folder untuk data tes dan training
#data tes
buka = open(testfolder,"r")
ambil = buka.readlines()
testset=[]
for i in ambil:
    a = i.split()
    testset.append(a)

#data training
buka = open(kelas,"r")
ambil = buka.readlines()
b=[]
for i in ambil:
    a = i.split()
    b.append(a)

#menghitung probabilitas dari kelas 0 dan 1
d=[0,1]
jum1 = len(b)
for i in range(0, jum1-1):
    if "0" in (b[i][2]):
        d[0]+=1
    else:
        d[1]+=1

d[0] = d[0]/jum1
d[1] = d[1]/jum1


itr = 0
dict = {'0':"",'1':""}

#TRAINING
for item in b:
    file = 'B:/Kul/Teksmin/dataset/Training101/'+b[itr][1]+'.xml'
#Mengambil isi data pada teks data Training
    xmlObject = xml.dom.minidom.parse(file)
    xmlstr = xmlObject.toprettyxml()
    xmlstr = str(xmlstr)
    soup = BS(xmlstr, 'html.parser')
    a = soup.find_all('text')
    for link in a:
        l = (link.get_text())
    if(b[itr][2]=="0"):
        dict['0'] += l
    else:
        dict['1'] += l
    itr += 1

#Tokenisasi data training
dict['0'] = nltk.word_tokenize(dict['0'].casefold())
dict['1'] = nltk.word_tokenize(dict['1'].casefold())

#Stemming data training
ps = PorterStemmer()
stem0 = []
stem1 = []
for w in dict['0']:
    stem0.append(ps.stem(w))
for w in dict['1']:
    stem1.append(ps.stem(w))

#Proses stop words
stop_words = set(stopwords.words('english'))
filter0 = []
filter1 = []
for w in stem0:
    if w not in stop_words:
        filter0.append(w)
for w in stem1:
    if w not in stop_words:
        filter1.append(w)
punctuations = list(string.punctuation)
punc0 = [];
punc1 = [];
for w in filter0:
    if w not in punctuations:
        punc0.append(w)
for w in filter1:
    if w not in punctuations:
        punc1.append(w)

#Proses perhitungan jumlah kemunculan kata
TotalKata0 = len(punc0)
TotalKata1 = len(punc1)

c0 = {}
c1 = {}

listTag0 = set()
listTag1 = set()
listTag = set()

for w in punc0:
    try:
        listTag0.add(w)
    except:
        pass
    try:
        listTag.add(w)
    except:
        pass

for item in listTag0:
    c0[item] = 0

for w in punc0:
    c0[w]+=1

for w in punc1:
    try:
        listTag1.add(w)
    except:
        pass
    try:
        listTag.add(w)
    except:
        pass
for item in listTag1:
    c1[item] = 0

for w in punc1:
    c1[w] += 1

Hasil = []
TotalKata = len(listTag)

#TESTING
itr = 0
for test in testset:
    filetes = 'B:/Kul/Teksmin/dataset/Test101/'+testset[itr][1]+'.xml'
    xmlObject = xml.dom.minidom.parse(filetes)
    xmlstr = xmlObject.toprettyxml()
    xmlstr = str(xmlstr)
    soup = BS(xmlstr, 'html.parser')
    a = soup.find_all('text')
    for link in a:
        l = (link.get_text())
    ab = l.casefold()
    tokens= nltk.word_tokenize(ab)
    ps = PorterStemmer()
    stemming = []
    for w in tokens:
         stemming.append(ps.stem(w))
    stop_words = set(stopwords.words('english'))
    filtered_sentence = []
    for w in stemming:
        if w not in stop_words:
            filtered_sentence.append(w)
    punctuations = list(string.punctuation)
    punc = []
    for w in filtered_sentence:
        if w not in punctuations:
            punc.append(w)
    c = {}
    listTag = set()
    for w in punc:
        try:
            listTag.add(w)
        except:
            pass
    for item in listTag:
        c[item]= 0

    for w in punc:
        c[w]+=1

    hasil0 = 0

#Proses Perhitungan Probabilitas kata dari dokumen untuk tiap kelas
    for item in listTag:
        try:
            x = c0[item]+1
            y = TotalKata0+TotalKata
            z = c[item]
            hasil0 = hasil0+math.log1p((x/y)**z)
        except:
            x = 1
            y = TotalKata0 + TotalKata
            z = c[item]
            hasil0 = hasil0 + math.log1p((x / y) ** z)
    hasil1 = 0
    for item in listTag:
        try:
            x = c1[item]+1
            y = TotalKata1+TotalKata
            z = c[item]
            hasil1 = hasil1+math.log1p ((x/y)**z)
        except:
            x = 1
            y = TotalKata1 + TotalKata
            z = c[item]
            hasil1 = hasil1+math.log1p((x / y) ** z)

#Proses membandingkan besar probabilitas kedua kelas
    if((hasil0+math.log1p(d[0]))>=(hasil1+math.log1p(d[1]))):
        Hasil.append("0")
    else:
        Hasil.append("1")
    itr+=1
akurasi = 0

for i in range(0,len(testset)-1):
    if(testset[i][2]==Hasil[i]):
        akurasi+=1
print("%d %%" % (akurasi/len(testset)*100))
