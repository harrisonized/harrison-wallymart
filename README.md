## Introduction

This is the project for the UCSC's SEQA.X401 [Object-Oriented Analysis and Design](https://www.ucsc-extension.edu/courses/object-oriented-analysis-and-design/) couse. The idea is to create an app using the object-oriented programming paradigm that utilizes 10 or more classes. I will first be building this as a command-line tool, but if I have extra time, I would love to put the front-end on the Django framework. If I do not get to it by the time this project is due, I may be returning to this in the future, as I think this could be an important portfolio piece and is good for my general skills development.



## Project X Prompt

Wallymart has asked you to take on AmazingCo in the online e-commerce space. Wallymart can't seem to catch up, but they have identified several areas that are crucial to a successful e-commerce site:
• high quality customer reviews
• large selection of products
• fast delivery

You know Wallymart does really well in physical in-store space. You also know Wallymart has appetite to radically change the way their e-commerce store is designed today.
You are in the driver seat.

Option #1: Design a web store complete with products, reviews, ordering capabilities, and delivery. You will own this end to end meaning that Wallymart has decided to even own the delivery of the products and not outsource to USPS, UPS, etc.



## Installation

Default conda environment is `wallymart`

```
# create
conda create --name wallymart python=3.8  # The Python version is important!
conda activate wallymart
conda install conda
conda install -c anaconda django
conda install pandas
python setup.py develop
```



## Command Line App Entry Point

```
./run-wallymart.sh
```



## Django Entry Point

Note: This part is not built.

```
python manage.py runserver
```
