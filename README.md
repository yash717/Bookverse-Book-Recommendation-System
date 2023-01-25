# Book Recommender System with Flask
[![GPLv3 License](https://camo.githubusercontent.com/5c3e00a7238fe082f0e7d85aa27ba7a70a123baf59d195c40e05b31cebdf399a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e392e362d626c756576696f6c6574)](https://opensource.org/licenses/)

[![GPLv3 License](https://camo.githubusercontent.com/a8256d965b9ade271a5aa6fffecc3b4564a0ede3c8a77287b1de5310fece95da/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4672616d65776f726b2d466c61736b2d726564)](https://opensource.org/licenses/)



[![GPLv3 License](https://camo.githubusercontent.com/8785a2cfa54ec466fe1d65c77a0aa7495f2b9188c4c46e50588f3bd65641dcd8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4150492d544d44422d666362613033)](https://opensource.org/licenses/)

## Overview 📋

A book recommendation system using Flask and an API is a web-based tool that suggests books to users based on their reading preferences and history. The system is built using the Flask framework, which allows for the creation of web applications in Python. The system also utilizes an API (Application Programming Interface) to access and retrieve data such as book information, user preferences, and ratings.📚







## Authors

- [@yash717](https://www.github.com/yash717)
Yash Dubbalwar

[![GPLv3 License](https://img.shields.io/badge/Maintained-Yes-orange)](https://opensource.org/licenses/)





## Installation 📦

Clone or download this repository to your local machine.

1.Install all the libraries mentioned in the [requirements.txt]

```bash
  $ pip install -r requirements.txt
```
2.Then run the flask server by

```bash
  $ python app.py
```






    
# Architecture

![alt text](https://miro.medium.com/max/792/1*P63ZaFHlssabl34XbJgong.jpeg)

# Algorithm For Recommendation

The Recommendations are made by computing similarity scores for movies using consine simarity. For each movie tags are created by combining various details like genre of the movie, title, top cast, director and then they are converted to vectors using which similarity matrix is formed. Then for any searched movie the movies with the largest similarity score with it are sorted and then recommended.

#Cosine similarity

![alt text](https://user-images.githubusercontent.com/74367889/170820479-843243b2-3659-4101-8adf-2e5c7cdbcc19.png)

 
## Project Screenshots 📷

### Homepage

![alt text](https://github.com/yash717/Bookverse-Book-Recommendation-System/blob/main/Screenshot%20(125).png?raw=true)

### Search bar with list

![alt text](https://github.com/yash717/Bookverse-Book-Recommendation-System/blob/main/Screenshot%20(126).png?raw=true)


### Recommended Books

![alt text](https://github.com/yash717/Bookverse-Book-Recommendation-System/blob/main/Screenshot%20(127).png?raw=true)



