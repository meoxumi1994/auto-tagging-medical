from keras.models import model_from_json
import numpy as np
import re

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk...")

# evaluate loaded model on test data

wordID = {}
tagID = {}
tagNameofID = []

stopWords = []
stopWordsFile = open("stopwords.txt", 'r')
for line in stopWordsFile:
    stopWords.append(line[:-1])

articleFile = open("data_crawl_article.txt", 'r')
medicalFile = open("data_crawl_medical.txt", 'r')

for id, line in enumerate(articleFile):
    line = re.sub(r"[^a-z ]+", ' ', line.lower())
    for word in line.split(" "):
        # word = removeSuffix(word)
        if word and word not in stopWords and len(word) > 2:
            wordID[word] = 1
N_word = 0
for word in wordID:
    wordID[word] = N_word
    N_word = N_word + 1

for id, line in enumerate(medicalFile):
    tag = re.sub(r"[^a-z ]+", ' ', line.lower())
    tagID[tag] = 1

N_tag = 0
for tag in tagID:
    tagID[tag] = N_tag
    tagNameofID.append(tag)
    N_tag = N_tag + 1

# API system :

from bottle import run, get

@get('/<sentence>')
def get(sentence):
    X = []
    sentence = re.sub(r"[^a-z ]+", ' ', sentence.lower())
    single_x = [0.0 for _ in range(N_word)]
    for word in sentence.split(" "):
        for tag in tagID:
            if word and word in tag.split(" ") and word != "surgery" and word != "medicine" and word != "transplantation" and word != "transplant":
                return tag
        if word in wordID:
            print(word)
            single_x[wordID[word]] = 1.0
    X.append(single_x)

    X_test = np.array(X)
    y_pred = loaded_model.predict(X_test)
    return tagNameofID[np.argmax(y_pred)]

run(reloader=True, debug=True)
