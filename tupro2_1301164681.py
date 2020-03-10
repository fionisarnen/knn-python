import csv
import pandas as fi
from math import sqrt
from operator import itemgetter

with open('DataTrain.csv','r') as dataTrain_CSV:
    lines = csv.reader(dataTrain_CSV)
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    kelas = []
    for row in lines:
        p1.append(row[0])
        p2.append(row[1])
        p3.append(row[2])
        p4.append(row[3])
        kelas.append(row[4])       
with open('DataTest.csv','r') as dataTest_CSV:
    lines = csv.reader(dataTest_CSV)
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    kelas2 = []
    for row in lines:
        q1.append(row[0])
        q2.append(row[1])
        q3.append(row[2])
        q4.append(row[3])
        kelas2.append(row[4])
        
k = 3
def euclideanDistance(p1, p2, p3, p4, q1, q2, q3, q4):
   rank = []
   distance = 0
   for x in range(len(p1)):
      distance = sqrt((float(p1[x])-float(q1))**2 + (float(p2[x])-float(q2))**2 + (float(p3[x])-float(q3))**2 + (float(p4[x])-float(q4))**2)
      rank.append(distance)
   return rank

def merge(data1, data2):    
   data_merged = [(data1[i], data2[i]) for i in range(0, len(data1))]
   return data_merged

def knn(p1, p2, p3, p4, q1, q2, q3, q4, kelas, kelas2, k):
   x = 0
   for x in range(len(q1)):
       interval = []
       interval = euclideanDistance(p1, p2, p3, p4, q1[x], q2[x], q3[x], q4[x])
       matchInterval_Kelas = merge(interval, kelas) 
       sortInterval_Kelas = sorted(matchInterval_Kelas, key=itemgetter(0))
       klasifikasi1 = sum(row[1].count('1') for row in sortInterval_Kelas[0:k])
       klasifikasi2 = sum(row[1].count('0') for row in sortInterval_Kelas[0:k])
       kelas2[x] = cekKelas(klasifikasi1, klasifikasi2)
              
def cekKelas(klasifikasi1, klasifikasi2):
   if (klasifikasi1 > klasifikasi2):
      return 1
   else:
      return 0
        
def SaveFile(kelas2):
   fc = fi.DataFrame(kelas2)
   fc.to_csv('Prediksi_Tugas2AI_[1301164681].csv')
file1 = 'Validasi.csv'
file2 = 'Prediksi_Tugas2AI_[1301164681].csv'
def getAccuracy(file1, file2):
    baca1 = fi.read_csv (file1)
    baca2 = fi.read_csv (file2)
    t = 0
    for t in range (len(baca1)):
        if baca1['0'][t] == baca2['0'][t]:
            t = t + 1
    return t

knn(p1, p2, p3, p4, q1, q2, q3, q4, kelas, kelas2, k)
SaveFile(kelas2)

print('K : ', k)
print('Akurasi : ', getAccuracy(file1, file2)/10,"%")

#print('kelas DataSet : ',kelas2)
