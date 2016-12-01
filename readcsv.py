# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:41:13 2016

@author: medialab
"""

import csv,cPickle,pdb


    
def getAllidx(List, num,offset = 0 ):
    return [a+offset  for a in range(len(List)) if List[a]==num]    

#f = open('test2.csv', 'r')
#for row in csv.DictReader(f):
#    print (row['car'])
#
#f.close() 


#data = {}
#f =  open('test2.csv', 'r')
#reader = csv.reader(f)
#for row in reader:
#    pdb.set_trace()
#    a = iter(row[1:])
#    data[row[0]] = dict(zip(a, a))


data = {}
Bpidx = {} # Body part index
#pos={}
#pos['X']=[]
#pos['Y']=[]
#pos['Z']=[]

f =  open('test.csv', 'r')
for idx,row in enumerate(csv.reader(f)):
    if idx ==2:
        a = getAllidx(row,'Marker')[:99]         
    if idx ==3:
        Btype = set(row[a[0]:a[-1]+1]) 
        for i in Btype:
            Bpidx[i]=getAllidx(row[a[0]:a[-1]+1],i,a[0])
            data[i] = {}
            data[i]['X']=[]
            data[i]['Y']=[]
            data[i]['Z']=[]
    if idx >= 7:
        for part in Btype:
            try:
                data[part]['X'].append(float(row[Bpidx[part][0]]))
            except:
                if row[Bpidx[part][0]]== '':
                   data[part]['X'].append(-99.0)
                else:
                    print row[Bpidx[i][0]]
            try:
                data[part]['Y'].append(float(row[Bpidx[part][1]]))
            except:
                if row[Bpidx[part][1]]== '':
                   data[part]['Y'].append(-99.0)
                else:
                    print row[Bpidx[i][1]]
            try:
                data[part]['Z'].append(float(row[Bpidx[part][2]]))
            except:
                if row[Bpidx[part][2]]== '':
                   data[part]['Z'].append(-99.0)
                else:
                    print row[Bpidx[i][2]]
            
cPickle.dump(data,file('mocapdata1128.pkl','wb'))




