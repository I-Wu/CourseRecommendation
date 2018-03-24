import requests
import json
import spacy
from collections import OrderedDict
import pickle
import matplotlib.pyplot as plt
import time;  # This is required to include time module.
import sys
import gensim.models.

class _Course:
    title = ""
    key = 0

    def __init__(self, title, similarity):
        self.title = title
        self.key = similarity

class priority_queue:
    def __init__(self):
        self._list = []
        self.capacity = 10
        
    def push(self, item):
        if len(self._list) == 0:
            self._list.append(item)
            return

        if len(self._list) < self.capacity:
            for i in range(len(self._list)):
                if item.key > self._list[i].key:                
                    self._list.insert(i, item)
                    return
            self._list.append(item)
        elif len(self._list) == self.capacity:
            for i in range(len(self._list)):
                if item.key > self._list[i].key:                
                    self._list.insert(i, item)
                    break
            if len(self._list) > self.capacity:
                self.pop()
        return
                
            
    def pop(self):
        self._list.pop()
    
    def serialize(self):
        '''
        if len(self._list) == 10:
            print("It's ", len(self._list))
        '''
        dic = OrderedDict()
        for i in self._list:
            dic[i.title] = i.key
        
        '''
            for j in self._list:
                print(j.title, j.key)
            print("--")
            for k, v in dic.items():
                print("key = ", k, "val = ", v)
        '''
        return dic

def to_json(similarity):
    dic = {}
    for k, v in similarity.items():
        dic[k] = v.serialize()
        if len(dic[k]) < 10:
            print("It's not 10 after to OrderedDict ", k)

    return dic

l = []

COURSES = sys.argv[1]
PATH = sys.argv[2]
MODEL = sys.argv[3]
if MODEL is None:
    MOEL = 'spacy'

with open(COURSES) as json_data:
    d = json.load(json_data)
    for dd in d:
        l.append(dd)


nlp = spacy.load('en')
course_lists = []
i = 0
ticks = time.time()
course = l[0]
print(course)
print("Begin Preprocessing")
appeared = {}
for course in l:
    i = i + 1
    # Avoid reappearance of course title
    title = course['course_title']
    if title in appeared:
        continue
    appeared[title] = 1

    c = {}
    text = course['course_descr']
    if text == 'null' or text == 'n/a':
        continue
    if course['course_title'] == 'Topics:' or course['course_title'] == 'Seminar:' or course['course_title'] == 'Independent Study':
        continue

    c['course_title'] = title 
    c['descr'] = text
    c['doc'] = nlp(title+text)
    course_lists.append(c)


print(len(course_lists))
print("Preprocessing Time: ", time.time() - ticks)


##### Preprocessing ######
batch_size = 1000
ticks = time.time()
similarity = {}

op = 0
print("course lists length: ", len(course_lists))
for i in range(len(course_lists)):
    course_i = course_lists[i]
    title_i = course_i['course_title']
    #if title_i == 'Modern Italy':
    #print("Running on Course: ", i)
    for j in range(len(course_lists)):
        if i <= j:
            continue
        course_j = course_lists[j]
        title_j = course_j['course_title']
        
        if model == 'gensim':
            sim = gm.wv.similarity(course_i['course_descr'], course_j['course_descr'])
        else:
            sim = course_i['doc'].similarity(course_j['doc'])
        #print("Running on Course: ", j, "sim = ", sim)

        if title_i not in similarity:
            _c = _Course(title_j, sim)
            _q = priority_queue()
            _q.push(_c)
            similarity[title_i] = _q
        else:
            _c = _Course(title_j, sim)
            similarity[title_i].push(_c)

        if title_j not in similarity:
            _c = _Course(title_i, sim)
            _q = priority_queue()
            _q.push(_c)
            similarity[title_j] = _q
        else:
            _c = _Course(title_i, sim)
            similarity[title_j].push(_c)
        op = op +1

        #if title_i == 'Creative Response:':
        #    print("len: ", len(similarity[title_i]._list))
    # save
    if i % batch_size == 0:
        filename = PATH +str(i) + '.json'
        with open(filename, 'w') as outfile:
            json.dump(to_json(similarity), outfile)
print("total operations = ", op)
FINAL_FNAME = 'course_batch_final.json'
with open(PATH+FINAL_FNAME, 'w') as outfile:
    json.dump(to_json(similarity), outfile)

print("Time: ", time.time() - ticks)
