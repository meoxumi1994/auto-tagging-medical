var Crawler = require("crawler");
var fs = require("fs");

fs.writeFile("./data_crawl_article.txt", "", function(err) {});
fs.writeFile("./data_crawl_medical.txt", "", function(err) {});

var c = new Crawler({
    maxConnections: 10,
    userAgent:
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    // This will be called for each crawled page
    callback: function(error, res, done) {
        if (error) {
            console.log(error);
        } else {
            var $ = res.$;
            medical = res.options.uri.split("/wiki/")[1]
            $("p").text().split(".").map(sentence => {

                sentence = sentence.toLowerCase()
                sentence = sentence.replace(new RegExp(medical, 'g'), "")
                medical.split("_").map(word => {
                    sentence = sentence.replace(new RegExp(word, 'g'), "")
                })
                if(sentence.split(" ").length > 4){
                    fs.appendFile("./data_crawl_article.txt", sentence.replace(new RegExp("\n", 'g')  , "") + "\n", function(err) {});
                    fs.appendFile("./data_crawl_medical.txt", medical + "\n", function(err) {});
                }
            })
            $("dd").text().split(".").map(sentence => {

                sentence = sentence.toLowerCase()
                sentence = sentence.replace(new RegExp(medical, 'g'), "")
                medical.split("_").map(word => {
                    sentence = sentence.replace(new RegExp(word, 'g'), "")
                })
                if(sentence.split(" ").length > 4){
                    fs.appendFile("./data_crawl_article.txt", sentence.replace(new RegExp("\n", 'g'), "") + "\n", function(err) {});
                    fs.appendFile("./data_crawl_medical.txt", medical + "\n", function(err) {});
                }
            })
            $("dt").text().split(".").map(sentence => {
                sentence = sentence.toLowerCase()
                sentence = sentence.replace(new RegExp(medical, 'g'), "")
                medical.split("_").map(word => {
                    sentence = sentence.replace(new RegExp(word, 'g'), "")
                })
                if(sentence.split(" ").length > 4){
                    fs.appendFile("./data_crawl_article.txt", sentence.replace(new RegExp("\n", 'g'), "") + "\n", function(err) {});
                    fs.appendFile("./data_crawl_medical.txt", medical + "\n", function(err) {});
                }
            })
        }
        done();
    }
});

const medical_object = {
  "anaesthesia": [
    "Anesthesiology"
  ],
  "dermatology": [
    "Dermatology"
  ],
  "brains-nerve": [
    "Neurology",
    "Neurosurgery"
  ],
  "oral": [
    "Oral Surgery",
    "Maxillofacial Surgery"
  ],
  "bones": [
    "Orthopaedic",
    "Hand Surgery"
  ],
  "dentistry": [
    "Endodontic",
    "Periodontology",
    "Prosthodontic"
  ],
  "cancer": [
    "Oncology",
    "Radiation Oncology"
  ],
  "children": [
    "Pediatric Medicine",
    "Pediatric Surgery",
    "Pediatric Dentistry"
  ],
  "palliative": [
    "Palliative Medicine"
  ],
  "plastic-surgery": [
    "Plastic Surgery"
  ],
  "psychiatry": [
    "Psychiatry"
  ],
  "geriatric": [
    "Geriatric Medicine"
  ],
  "ear-nose-throat": [
    "Otorhinolaryngology"
  ],
  "eyes": [
    "Ophthalmology"
  ],
  "general-surgery": [
    "General Surgery"
  ],
  "heart-vascular": [
    "Cardiothoracic Surgery",
    "Cardiology"
  ],
  "hormone-disorder": [
    "Endocrinology"
  ],
  "kidneys": [
    "Nephrology"
  ],
  "lungs": [
    "Pulmonology"
  ],
  "stomach-digestive": [
    "Gastroenterology"
  ],
  "transplantation-cellular": [
    "Liver Transplantation",
    "Hematopoietic Stem Cell Transplantation",
    "Kidney Transplant"
  ],
  "urinary-reproductive": [
    "Urology"
  ],
  "women-gynaecology": [
    "Obstetrics",
    "Gynaecology"
  ],
  "infection-disease": [
    "Infectious Disease"
  ],
  "internal-medicine": [
    "Haematology",
    "Internal Medicine"
  ],
  "rheumatology": [
    "Rheumatology"
  ],
  "sport-medicine": [
    "Sports Medicine"
  ]
}

const arr_queue = []

for(let item in medical_object){
    medical_object[item].map(i => {
        i = i.replace(new RegExp(" ", 'g'),"_").toLowerCase()
        arr_queue.push("https://en.wikipedia.org/wiki/" + i)
    })
}

c.queue(arr_queue);
