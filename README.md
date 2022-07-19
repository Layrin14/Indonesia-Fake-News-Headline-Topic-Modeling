# Indonesian Fake News Headline Topic Modeling w/ LDA (Latent Dirichlet Allocation)

## Introduction / Motivation <a class="anchor" name="chapter1"></a>
Internet is a place used by almost all citizens in the world to search news articles, including Indonesian citizens. Because of the ease of accessing the internet, it is often used as a place to spread fake news. Those fake news has titles that can deceive people to read it (clickbait) by writing about hot topics or famous figures such as religion issues or figures like president. Based on these titles, this notebook will conduct topic modeling to see which topics are often made into fake news.

## About the data
This project used scraped data from [TurnBackHoax.id](https://turnbackhoax.id/) using BeatifulSoup by running `news.py`. TurnBackHoax.ID is a site managed by the Indonesian anti-hoax forum (MAFINDO). Data was collected from July 31, 2015 to June 26, 2022 with a total of about 9 thousand data and 2 columns (`title` and `label`).

## Goal
Goal of this project is to see which topics that are often made into fake news using LDA model and BERT model (Transformer). The model will produce a different number of topics, as for LDA model will be evaluated using coherence score.

## Conclusion / Result

LDA model was able to be fitted with two different corpus, Bag of Words corpus and TF-IDF corpus. LDA + BoW model produces a coherence score of 0.57 with total 18 topics. While LDA + TF-IDF model produces higher coherence score of 0.63 with the same amount of topics, which is 18 topics in total. As for BERT, the model produces ~60 topics. The result of the 3 model are presented below in the form of a table:

|Model|Number of Topics|
|:---:|:---:|
|LDA + BoW|18|
|LDA + TF-IDF|18|
|BERT + UMAP + HDBSCAN|60|

---
### You can check model [here](https://nbviewer.org/github/Layrin14/Indonesia-Fake-News-Headline-Topic-Modeling/blob/master/Topic_modeling.ipynb)

