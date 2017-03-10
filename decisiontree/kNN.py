from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plot

def createDataSet():
    group = array([[1.0, 1.0], [2.0, 2.01], [11.5, 21.87], [13, 23]])
    labels = ['C', 'C', 'B', 'B']

    return (group, labels)

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    distances = ((diffMat ** 2).sum(axis = 1)) ** 0.5
    sortedIndexes = distances.argsort()
    print(sortedIndexes)
    classCount = {}
    for i in range(k):
        print(str(i) + str(sortedIndexes[i])+ labels[sortedIndexes[i]])
        votedLabel = labels[sortedIndexes[i]]
        print(votedLabel)
        classCount[votedLabel] = classCount.get(votedLabel, 0) +1

    print("result")
    print(classCount.items())
    print(sorted(classCount))
    #s = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    s = max(classCount.items(), key=operator.itemgetter(1))
    print(classCount)
    print(s)
    print(s[0])
    #print(s[0][0])

def drawPic(group):
    fig = plot.figure()
    ax = fig.add_subplot(111)
    full = group.flatten().tolist()
    print(full)
    print(full[0::2])
    print(full[1::2])
    ax.plot(full[0::2], full[1::2], "r*")


    fig.show()
    fig.savefig("test.pdf")



if __name__ == "__main__":
    group, label = createDataSet()
    classify0((2, 2), group, label, 3)



