# Project 3

## Objective

**Nozomi NLP Co., Ltd.** is a company focusing on artificial intelligence about **Natural Language Processing (NLP)**. But due to the name of company, those who misunderstand for **Neuro Linguistic Programming (NLP)** send inquiry E-mails to us. Thus, we need a classifier to inspect such a irrelevant E-mail.

In [reddit](https://www.reddit.com/), there are many webboards called _subreddit_ where people are discussing according to its topic. Text data of subreddit about these 2 NLP in reddits can be helpful to create a classifier.

## Outflow

1. scrape reddit posts about _Natural Language Processing_ and _Neuro Linguistic Programming_
    - `code/scrape_reddit.ipynb`
2. EDA and text preprocessing
    - `code/preprocessing.ipynb`
3. modelling and evaluation
    - `code/modelling.ipynb`

## Data

#### data dictionary

|column|data type|description|
|:-:|:-:|:-:|
|`title`|string|title of the post|
|`text`|string|content of the post|
|`vote`|int|(the number of likes) - (the number of dislikes)|
|`date`|datetime|date of the post, e.g. `2011-3-11`|

#### details of 2 subreddits data

|file name|description|records|date|
|:-:|:-:|:-:|:-:|
|`LanguageTechnology.json`| `/r/languagetechnology` : subreddit about Natural Language Processing|5,821|2010-03-10 ~ 2023-10-23|
|`LanguageTechnology_withtext.json`| after dropping records without `text`|3,473|2011-11-02 ~ 2023-06-10|
|`NLP.json`| `/r/nlp` : subreddit about Neuro Linguistic Programming|1,927|2010-06-18 ~ 2023-10-23|
|`NLP_withtext.json`| after dropping records without `text`|448|2010-09-24 ~ 2023-06-08|

## Text Preprocessing

- remove URLs
- tokenization and lemmatization
- **not remove the word "NLP"**, because it's not data leakage

## Modelling