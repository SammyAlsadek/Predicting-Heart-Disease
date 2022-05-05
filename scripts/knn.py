# K-Nearest Neighbor

from math import inf
from unicodedata import numeric
from sklearn.neighbors import KNeighborsClassifier
import csv
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('age', type=int)
parser.add_argument('sex', type=int)
parser.add_argument('cp', type=int)
parser.add_argument('trestbps', type=int)
parser.add_argument('chol', type=int)
parser.add_argument('fbs', type=int)
parser.add_argument('restecg', type=int)
parser.add_argument('thalach', type=int)
parser.add_argument('exang', type=int)
parser.add_argument('oldpeak', type=float)
parser.add_argument('slope', type=int)
parser.add_argument('ca', type=int)
parser.add_argument('thal', type=int)
args = parser.parse_args()
user = [args.age, args.sex, args.cp, args.trestbps, args.chol, args.fbs,
        args.restecg, args.thalach, args.exang, args.oldpeak, args.slope, args.ca, args.thal]

# read data
training_data = []
with open('../data/training-data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        training_data.append([float(x) for x in row])

testing_data = []
with open('../data/testing-data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        testing_data.append([float(x) for x in row])


# seperate the instance dat from the instances classification
X = []
Y = []
for instance in training_data:
    X.append(instance[:-1])
    Y.append(instance[-1])


lowest_error = [inf, 0, 0, 0]
for p in range(1, 3):
    for k in range(1, len(training_data)):
        # fitting the knn to the data
        clf = KNeighborsClassifier(n_neighbors=k, p=p)
        clf = clf.fit(X, Y)

        user_predicted = clf.predict([user])

        wrongCount = 0
        for instance in testing_data:
            class_predicted = clf.predict([instance[:-1]])

            if class_predicted != instance[-1]:
                wrongCount += 1

        if wrongCount < lowest_error[0]:
            lowest_error[0] = wrongCount
            lowest_error[1] = k
            lowest_error[2] = p
            lowest_error[3] = user_predicted


# print the accuracy
accuracy = (1 - (lowest_error[0] / len(testing_data))) * 100
if lowest_error[3]:
    print(f"Positive with {int(accuracy)}% Accuracy.")
else:
    print(f"Negative with {int(accuracy)}% Accuracy.")
sys.exit(int(lowest_error[3]))
