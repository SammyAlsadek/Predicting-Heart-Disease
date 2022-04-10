# K-Nearest Neighbor

from math import inf
from sklearn.neighbors import KNeighborsClassifier
import csv


# read data
training_data = []
with open('./data/training-data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        training_data.append([float(x) for x in row])

testing_data = []
with open('./data/testing-data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        testing_data.append([float(x) for x in row])


# seperate the instance dat from the instances classification
X = []
Y = []
for instance in training_data:
    X.append(instance[:-1])
    Y.append(instance[-1])


lowest_error = [inf, 0, 0]
for p in range(1, 3):
    for k in range(1, len(training_data)):

        # fitting the knn to the data
        clf = KNeighborsClassifier(n_neighbors=k, p=p)
        clf = clf.fit(X, Y)

        wrongCount = 0
        for instance in testing_data:
            class_predicted = clf.predict([instance[:-1]])

            if class_predicted != instance[-1]:
                wrongCount += 1

        if wrongCount < lowest_error[0]:
            lowest_error[0] = wrongCount
            lowest_error[1] = k
            lowest_error[2] = p


# print the accuracy
accuracy = 1 - (lowest_error[0] / len(testing_data))
print(f"Accuracy = {accuracy}, K = {lowest_error[1]}, P = {lowest_error[2]}")
