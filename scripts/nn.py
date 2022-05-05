# Neural Network

from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
from math import inf
import numpy as np
import pandas as pd
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

X_training = []
Y_training = []
testing_data = []

n = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0]
r = [True, False]


# read data
with open('../data/training-data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        X_training.append([float(x) for x in row[:-1]])
        Y_training.append(float(row[-1]))

with open('../data/testing-data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        testing_data.append([float(x) for x in row])


lowest_error = [inf, 0, True, 0, 0]
for w in n:
    for b in r:
        for a in range(1, 2):
            # Create a Neural Network classifier
            if a == 0:
                clf = Perceptron(eta0=w, shuffle=b, max_iter=1000)
            else:
                clf = MLPClassifier(activation='logistic', learning_rate_init=w, hidden_layer_sizes=(
                    25,), shuffle=b, max_iter=1000)

            # Fit the Neural Network to the training data
            clf.fit(X_training, Y_training)

            user_predicted = clf.predict([user])

            wrongCount = 0
            for instance in testing_data:
                class_predicted = clf.predict([instance[:-1]])

                if class_predicted != instance[-1]:
                    wrongCount += 1

            if wrongCount < lowest_error[0]:
                lowest_error[0] = wrongCount
                lowest_error[1] = w
                lowest_error[2] = b
                lowest_error[3] = a
                lowest_error[4] = user_predicted

# print the accuracy
accuracy = (1 - (lowest_error[0] / len(testing_data))) * 100
if lowest_error[3]:
    print(f"Positive with {int(accuracy)}% Accuracy.")
else:
    print(f"Negative with {int(accuracy)}% Accuracy.")
sys.exit(int(lowest_error[4]))
