# -*- coding: utf-8 -*-
from os import listdir,mkdir,path
import nltk
from nltk.corpus import stopwords
from numpy import *
import re
from nltk.stem.porter import PorterStemmer
path1 = r'E:\code\git\20news-18828'
path2 = r'E:\code\git\20news'
path3 = r'E:\code\git'
path4 = r'E:\code\git\vsm'

def pre_process():
    source_data_file = listdir(path1)
    for i in range(len(source_data_file)):
        if path.exists(path2 + '/' + source_data_file[i])==False:
            mkdir(path2 + '/' + source_data_file[i])
        source_data = listdir(path1 + '/' + source_data_file[i])
        for j in range(len(source_data)):
            target_dir = path2 + '/' + source_data_file[i] + '/' + source_data[j]
            f = open(target_dir,'w')
            source_dir = path1 + '/' + source_data_file[i] + '/' + source_data[j]
            data = open(source_dir,'rb').readlines()
            for line in data:
                line = line.decode("utf-8",errors='ignore')
                #nltk.download('stopwords')
                #nltk.download('punkt')
                text_list = re.sub("[^a-zA-Z]", " ", line).split()
                stoplist = stopwords.words('english')           
                #wordlist = nltk.word_tokenize(sentence)
                for word in text_list:
                    word = PorterStemmer().stem(word.lower())
                    if word not in stoplist:
                        f.write('%s\n' % word)
            f.close()
            
def creat_dict():
    word_map = {}
    datafile = listdir(path2)
    for i in range(len(datafile)):
        datalist = listdir(path2 + '/' + datafile[i])
        for j in range(len(datalist)):
            for line in open(path2 + '/' + datafile[i] + '/' + datalist[j]).readlines():
                word = line.strip('\n')
                word_map[word] = word_map.get(word,0)+1
    new_dict_file = path3 + '/' + 'newdict'
    f = open( new_dict_file,'w')
    for key,value in word_map.items():
        if value > 4:
            f.write('%s\n' % key)
    f.close()
    
def VSM():
    source_file = listdir(path2)
    for i in range(len(source_file)):
        if path.exists(path4 + '/' + source_file[i])==False:
            mkdir(path4 + '/' + source_file[i])
        vsm_file = listdir(path2 + '/' + source_file[i])
        for j in range(len(vsm_file)):
            f = open(path4 + '/' + source_file[i] + '/' + vsm_file[j],'w')
            for word in open(path2 + '/' + source_file[i] + '/' + vsm_file[j]).readlines():
                for key in open(path3 + '/' + 'newdict').readlines():
                    if word == key:
                        f.write('%s\n' % word.strip('\n'))
                        break
            f.close()
print('ok')
            
                