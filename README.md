### Hi, this is the project about automation tag medical condition from a sentence

##### Method :
* Crawling data from wiki about all object is given "Anesthesiology", "Dermatology", ...
* Preprocess by using list stopword, convert to lowercase and just keep alphabet character, remove all word too short, ...
* We need tag a medical condition with each sentence so I use the one-hot vector to display each sentence and medical condition
* After that I prepare training and testing data by using 10% of all data to test, acc = 0.98
##### How to run :
After clone project, go to auto-tagging-medical/ then
```
> npm install
> node crawler.js // crawl data from Wikipedia
> python training_model.py // filter data and training then save model File, install library if missing
> python load_model.py // read model File then run a server
```
##### How to test:
* An example you have a question : "I'm having a chest pain"
* Then request `http://localhost:8080/I'm having a chest pain`
* Then get the result by a string
