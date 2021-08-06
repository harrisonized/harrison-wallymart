

## Introduction

Object oriented back-end will be contained in `wallymart`, everything front-end will be contained in `wallymart_django`.



## Project X Prompt

For those students who have no ideas or just want something to work on, you may choose this idea without my permission.

Wallymart has asked you to take on AmazingCo in the online e-commerce space. Wallymart can't seem to catch up, but they have identified several areas that are crucial to a successful e-commerce site:
• high quality customer reviews
• large selection of products
• fast delivery

You know Wallymart does really well in physical in-store space. You also know Wallymart has appetite to radically change the way their e-commerce store is designed today.
You are in the driver seat.

Option #1: Design a web store complete with products, reviews, ordering capabilities, and delivery. You will own this end to end meaning that Wallymart has decided to even own the delivery of the products and not outsource to USPS, UPS, etc.



## Installation

Default conda environment is `wallymart`

```django
# create
conda create --name wallymart python=3.8  # The Python version is important!
conda activate wallymart
conda install conda
conda install -c anaconda django
conda install pandas
python setup.py develop
```



## Command Line App

Entry point is `wallymart/wallymart_app`.

```django
./wallymart/wallymart_app.py
```

Alternatively:

```django
./wallymart_app.sh
```

