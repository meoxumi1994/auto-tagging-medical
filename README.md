### Hi, this is project about automation tag medical condition from a sentence

##### Method :
* crawls data from wiki about all object given "Anesthesiology", "Dermatology", ...
* preprocess by using list stopword, convert to lowercase and just keep alphabet character, remove all word too short, ...
* with each sentence we need tag a medical condition so i using one-hot vector to display each sentence and each medical condition
* after that i prepare train and test data by using 10% of all data to test
##### How to run :
after clone project, go to auto-tagging-medical/ then
```
> npm install
> node crawler.js // crawl data from wikipeadia
> python trainning_model.py // filter data and trainning then save model File
> python load_model.py // read model File then run server
```
##### How to test:
* example you have a question : "I'm having a chest pain"
* then request `http://localhost:8080/I'm having a chest pain`
* then get result by string
