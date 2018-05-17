import numpy as np
import re

#step 1: load tags and words
wordID = {}
tagID = {}

stopWords = []
stopWordsFile = open("stopwords.txt", 'r')
for line in stopWordsFile:
    stopWords.append(line[:-1])

articleFile = open("data_crawl_article.txt", 'r')
medicalFile = open("data_crawl_medical.txt", 'r')

singleLine = {}

for id, line in enumerate(articleFile):
    line = re.sub(r"[^a-z ]+", ' ', line.lower())
    for word in line.split(" "):
        if word and word not in stopWords and len(word) > 2:
            wordID[word] = 1
N_word = 0
for word in wordID:
    wordID[word] = N_word
    N_word = N_word + 1

for id, line in enumerate(medicalFile):
    tag = re.sub(r"[^a-z ]+", '', line.lower())
    tagID[tag] = 1

N_tag = 0
for tag in tagID:
    tagID[tag] = N_tag
    N_tag = N_tag + 1

#step 2: prepare training and testing data

X, Y = [], []
articleFile = open("data_crawl_article.txt", 'r')
medicalFile = open("data_crawl_medical.txt", 'r')

singleLine = {}

# print(N_word, N_tag)
for id, line in enumerate(articleFile):
    line = re.sub(r"[^a-z ]+", ' ', line.lower())
    single_x = [0.0 for _ in range(N_word)]
    for word in line.split(" "):
        if word in wordID:
            single_x[wordID[word]] = 1.0
    X.append(single_x)

for id, line in enumerate(medicalFile):
    tag = re.sub(r"[^a-z ]+", '', line.lower())
    single_y = [0.0 for _ in range(N_tag)]
    single_y[tagID[tag]] = 1.0
    Y.append(single_y)

X = np.array(X)
Y = np.array(Y)

print(N_tag, N_word)
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from keras import regularizers
# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(2048, kernel_initializer = 'uniform', activation = 'relu', input_dim = N_word))
# Adding the second hidden layer
classifier.add(Dense(1024, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(512, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(256, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(128, kernel_initializer = 'uniform', activation = 'relu'))
# Adding the output layer
classifier.add(Dense(N_tag, kernel_initializer = 'uniform', activation = 'softmax'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 25, epochs = 30)

# Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)


# serialize model to JSON
model_json = classifier.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
classifier.save_weights("model.h5")
print("Saved model to disk")

# later...
