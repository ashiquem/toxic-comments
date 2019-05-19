# Toxic Comments Classification

## Project Motivation

This project aims to understand the patterns in our hate online. Using the Cross-Industry Standard Process of Data Mining (CRISP-DM), the data provided by Jigsaw is studied to answer the following questions:

* How diverse is our hate?
* What are the ingredients of toxic comments?
* Where do we draw the line?

## Files

The repository contains the `Toxic-comments.ipynb` notebook used to draw insights for writing this blog post [here](https://medium.com/@ashiquem/the-nitty-gritty-of-online-toxicity-8d37080943b9). 

This repository also contains the  code for the web application running [here](https://classify-toxic-comments.herokuapp.com/). You can classify your comments into different classes of toxicity. The model was trained using the data from Jigsaw, hosted as a kaggle competition. 
 
You can find the training script used to develop the deep learning model [here](https://www.kaggle.com/ashiquemahmood/train).

## Usage

Libraries required (besides the standard anaconda dist) for the notebook: 

* plotly
* tqdm
* wordcloud

The data used for the analysis can be found [here](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data) hosted on Kaggle.

Libraries required for running the web application are listed in the `requirements.txt` file.

## Results

The results of the analysis are summarized [here](https://medium.com/@ashiquem/the-nitty-gritty-of-online-toxicity-8d37080943b9) in this medium blog post.

The deep learning model built has been deployed as a web application and is running [here](https://classify-toxic-comments.herokuapp.com/). 

## Licensing, Authors, Acknowledgements

Data provided by [Jigsaw](https://jigsaw.google.com/).