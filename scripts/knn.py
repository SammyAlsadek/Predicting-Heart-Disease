# K-Nearest Neighbor

from math import inf
from unicodedata import numeric
from sklearn.neighbors import KNeighborsClassifier
import csv
import argparse
import os.path
import pickle

fname = '../stored models/knn.pkl'
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

# if the model doesn't exist
if not os.path.isfile(fname):

    training_data = []
    with open('../data/training-data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            training_data.append([float(x) for x in row])

    # seperate the instance dat from the instances classification
    X = []
    Y = []
    for instance in training_data:
        X.append(instance[:-1])
        Y.append(instance[-1])

    testing_data = []
    with open('../data/testing-data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            testing_data.append([float(x) for x in row])

    len_test_data = len(testing_data)
    lowest_error = inf

    for p in range(1, 3):
        for k in range(1, len(training_data)):
            # fitting the knn to the data
            clf = KNeighborsClassifier(n_neighbors=k, p=p)
            clf = clf.fit(X, Y)

            # count number of wrong predictions
            wrongCount = 0
            for instance in testing_data:
                class_predicted = clf.predict([instance[:-1]])
                if class_predicted != instance[-1]:
                    wrongCount += 1

            # keep the best model
            if wrongCount < lowest_error:
                lowest_error = wrongCount
                best_model = clf

    # store the best model
    with open(fname, 'wb') as f:
        pickle.dump([lowest_error, best_model, len_test_data], f)
    
else:
    # or load the best model
    with open(fname, 'rb') as f:
        loadf = pickle.load(f)
        lowest_error = loadf[0]
        best_model = loadf[1]
        len_test_data = loadf[2]

user_predicted = best_model.predict([user])

# print the accuracy
accuracy = (1 - (lowest_error / len_test_data)) * 100
if user_predicted:
    print(f"Positive with {round(accuracy, 2)}% Accuracy.")
else:
    print(f"Negative with {round(accuracy, 2)}% Accuracy.")
