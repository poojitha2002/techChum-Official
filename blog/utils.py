import matplotlib.pyplot as plt
import base64
from io import BytesIO
import random

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Rating Graph')
    plt.pie(x,y)
    plt.tight_layout()
    graph=get_graph()
    return graph


def get_plot9(x,y,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,7))
    # plt.title('items vs price')
    plt.plot(x,y)
    randomlist = [0.1]
    cols = ['c','m','r','g','b','y']
    #print("x= ",len(x))
    expldelist=[]
    p=len(x)
    while p>0:
        expldelist.append(random.choice(randomlist))
        p-=1

    explode = tuple(expldelist)
    print()
    plt.pie(y,labels=x,colors=cols,startangle=90,shadow=True,explode=explode,autopct='%1.1f%%')
    plt.xticks(rotation=90)
    # plt.legend(x)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot10(x,y,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,7))
    # plt.title('items vs price')
    plt.plot(x,y)
    cols = ['c','m','r','g','b','y']
    randomlist = [0.1]
    #print(len(x))
    expldelist = []
    p = len(x)
    while p > 0:
        expldelist.append(random.choice(randomlist))
        p -= 1

    explode = tuple(expldelist)
    plt.pie(y,labels=x,colors=cols,startangle=90,shadow=True,explode=explode,autopct='%1.1f%%')
    plt.xticks(rotation=90)
    # plt.legend(x)
    plt.tight_layout()
    graph = get_graph()
    return graph