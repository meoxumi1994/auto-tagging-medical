### Hi, this is project about automation tag medical condition from a sentence

##### Method :
* crawling data from wiki about all object given "Anesthesiology", "Dermatology", ...
* preprocess by using list stopword, convert to lowercase and just keep alphabet character, remove all word too short, ...
* we need tag a medical condition with each sentence so i use one-hot vector to display each sentence and medical condition
* after that i prepare training and testing data by using 10% of all data to test, acc = 0.98
##### How to run :
after clone project, go to auto-tagging-medical/ then
```
> npm install
> node crawler.js // crawl data from wikipeadia
> python training_model.py // filter data and training then save model File, install library if missing
> python load_model.py // read model File then run server
```
##### How to test:
* example you have a question : "I'm having a chest pain"
* then request `http://localhost:8080/I'm having a chest pain`
* then get result by string
