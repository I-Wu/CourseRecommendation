import spacy
import numpy as np
from collections import Counter
import json
import pickle
import numpy as np
from sklearn.decomposition import PCA
from pprint import pprint
 
import sys
import pickle
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d


""" Sample input
filename = "./packet/CryptXXX/small_train"
"""

COURSES = sys.argv[1]
FLAG = sys.argv[2]

#filename = sys.argv[1]
def main():
    # read a file which saves semantic presentation
    l = []
    with open(COURSES) as json_data:
        d = json.load(json_data)
        for dd in d:
            l.append(dd)

    nlp = spacy.load('en')
    courses = []
    semantics = []
    course = l[0]
    print(course)
    print("Begin Preprocessing")
    appeared = {}
    title2index = {}
    idx = 0
    for course in l:
        # Avoid reappearance of course title
        title = course['course_title']
        if title in appeared:
            continue
        appeared[title] = 1

        text = course['course_descr']
        if text == 'null' or text == 'n/a':
            continue
        if course['course_title'] == 'Topics:' or course['course_title'] == 'Seminar:' or course['course_title'] == 'Independent Study':
            continue

        title2index[title] = idx
        c = nlp(title + " " + text)
        semantics.append(c.vector)
        courses.append(title)
        idx = idx + 1


    Xtrain = np.asarray(semantics)
    pca = PCA()
    reduced = pca.fit_transform(Xtrain)


    # Save the PCA vectors
    with open("title_packet_pcainfo", "wb") as f:
        pickle.dump(reduced, f)
        pickle.dump(Xtrain, f)
        pickle.dump(courses, f)



    with open('./title_test/course_batch_final_with_title_space.json') as data_file:    
        data = json.load(data_file)

    title = []
    title.append('Modern Italy')

    for k, v in data['Modern Italy'].items():
        title.append(k)

    for t in range(1, len(title)):
        for k, v in data[title[t]].items():
            title.append(k)
    word2vec = []
    print(len(word2vec))
    for t in title:
        word2vec.append(semantics[title2index[t]])
    word2vec_reduced = pca.fit_transform(word2vec)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    col = ax.scatter(word2vec_reduced[:,0], word2vec_reduced[:,1])
    for i in range(len(word2vec)):
        ax.annotate(title[i], (word2vec_reduced[i, 0],word2vec_reduced[i, 1]))
    plt.title('Modern Italy')
    plt.savefig('./neighbor_pca_modern_italy.jpg')

if FLAG == 'INIT':
    main()



def text_display(text):
    return ''.join([chr(int(t)) for t in text if t != 0])


def onpick(event):
    ind = event.ind
    print('scatter: {} {} {}'.format(ind[0], text_display(Xtrain[ind[0]].A1), Ytrain[ind[0]]))


flag = "2D"

with open('title_packet_pcainfo', "rb") as f:
    reduced = pickle.load(f)
    Xtrain = pickle.load(f)
    Ytrain = pickle.load(f)
    xmin = -4
    xmax = 4
    ymin = -4
    ymax = 4
    fig = plt.figure()

    s = 5000
    e = 5100 # len(Xtrain)
    # Build the subgraph
    if flag is "3D":
        ax1 = fig.add_subplot(111, projection = "3d")
        col = ax1.scatter(reduced[:,0], reduced[:,1], reduced[:,2], s=100, c=Ytrain, alpha=0.5, picker=True)
    else:
        ax1 = fig.add_subplot(111)
        col = ax1.scatter(reduced[s:e,0], reduced[s:e,1])
        for i in range(s, e):
            ax1.annotate(Ytrain[i], (reduced[i, 0],reduced[i, 1]))

    #fig.set_dpi(300)
    fig.canvas.mpl_connect('pick_event', onpick)
    fig.set_size_inches(20, 10)
    plt.axis([xmin,xmax,ymin,ymax])
    plt.title('Top 2 Principal Components')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.savefig('./jpg/similarity_cnn.jpg')
    plt.show()

