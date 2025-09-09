# what is sentiment analysis?
# it is a popular task in NLP.The goal of sentiment analysis is to classify the
# text based on the mood and mentality written in the Text,which can be neutral
# positive and Negative.
# It not only on polarity (positive, negative & neutral) but also on emotions
# (happy, sad, angry, etc.). It uses various Natural Language Processing
# algorithms such as Rule-based, Automatic, and Hybrid.

"1: why is Sentiment Analysis important?"
# Sentiment analysis is the contextual meaning of words that indicates the
# social sentiment of a brand and also helps the business to determine whether
# the product they are manufacturing is going to make a demand in the market
# or not.
" Here are a few uses of sentiment analysis:"
# 1.Customer feedback Analysis:Businesses can analyze customer reviews,comments
# and feedback to understand the sentiment behind them.

# 2.Brand Reputation Management: Sentiment analysis allows businesses to
# monitor their brand reputation in real-time.

# 3.Product Development and Innovation: Understanding customers sentiments and
# making sure the same problem doesnt happens again and again in the same way.
"what are the types of Sentiment Analysis?"
# 1.Emotion detection:-
# The sentiments happy, sad, angry, upset, jolly, pleasant,and so on come under
# emotion detection.It is known as a lexicon method of sentiment analysis.

# 2.Aspect-Based Sentiment Analysis:
#  if a person wants to check the feature of the cell phone then it checks the
# aspect such as the battery,screen,and camera quality then aspect is used.

import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
import io
import unicodedatacode
import numpy as np
import re
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


with open('kindle.txt', encoding='ISO-8859-2') as f:
    text = f.read()

sent_tokenizer = PunktSentenceTokenizer(text)
sents = sent_tokenizer.tokenize(text)

print(word_tokenize(text))
print(sent_tokenize(text))

porter_stemmer = PorterStemmer()

nltk_tokens = nltk.word_tokenize(text)

for w in nltk_tokens:
    print("Actual: % s Stem: % s" % (w, porter_stemmer.stem(w)))


wordnet_lemmatizer = WordNetLemmatizer()
nltk_tokens = nltk.word_tokenize(text)

for w in nltk_tokens:
    print("Actual: % s Lemma: % s" % (w, wordnet_lemmatizer.lemmatize(w)))

text = nltk.word_tokenize(text)
print(nltk.pos_tag(text))

sid = SentimentIntensityAnalyzer() 
tokenizer = nltk.data.load('tokenizers / punkt / english.pickle')

with open('kindle.txt', encoding='ISO-8859-2') as f:
    for text in f.read().split('\n'):
        print(text)
        scores = sid.polarity_scores(text)
        for key in sorted(scores):
            print('{0}: {1}, '.format(key, scores[key]), end='')

    print()
