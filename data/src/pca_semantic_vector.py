import spacy
import numpy as np
from collections import Counter
import json
import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn.decomposition import PCA

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

        c = nlp(title + " " + text)
        semantics.append(c.vector)
        courses.append(title)


    Xtrain = np.asarray(semantics)
    pca = PCA()
    reduced = pca.fit_transform(Xtrain)
    print("examples: ", len(reduced))
    # Save the PCA vectors
    with open("title_packet_pcainfo", "wb") as f:
        pickle.dump(reduced, f)
        pickle.dump(Xtrain, f)
        pickle.dump(courses, f)


if FLAG == 'INIT':
    main()
 
import sys
import pickle
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d


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
    print(Xtrain)
    print(Ytrain)
    print(Ytrain)
    xmin = -4
    xmax = 4
    ymin = -4
    ymax = 4
    fig = plt.figure()

    n = 100 # len(Xtrain)
    # Build the subgraph
    if flag is "3D":
        ax1 = fig.add_subplot(111, projection = "3d")
        col = ax1.scatter(reduced[:,0], reduced[:,1], reduced[:,2], s=100, c=Ytrain, alpha=0.5, picker=True)
    else:
        ax1 = fig.add_subplot(111)
        col = ax1.scatter(reduced[:n,0], reduced[:n,1])
        for i in range(n):
            ax1.annotate(Ytrain[i], (reduced[i, 0],reduced[i, 1]))

    fig.set_dpi(300)
    fig.canvas.mpl_connect('pick_event', onpick)
    fig.set_size_inches(20, 20)
    plt.axis([xmin,xmax,ymin,ymax])
    plt.title('Top 2 Principal Components')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.savefig('./jpg/similarity_cnn.jpg')
    plt.show()