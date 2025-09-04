# Term frequency : It measures how often a word is present in a Document.A high
# frequency shows importance in a document.
# Total number of times a word appears in a document / total number of words
# in a document.


from sklearn.feature_extraction.text import TfidfVectorizer
d0 = 'cats for geeks'
d1 = 'cats'
d2 = 'geeks'
string = [d0, d1, d2]
tfidf = TfidfVectorizer()
result = tfidf.fit_transform(string)
print('\nidf values:')
for ele1, ele2 in zip(tfidf.get_feature_names_out(), tfidf.idf_):
    print(ele1, ':', ele2)

# Inverse documnet Frequency : It Reduces the increment of the common word and
# Increasees the rare words in the document.
# Display IDF values print('\nidf values:')
# for ele1, ele2 in zip(tfidf.get_feature_names_out(), tfidf.idf_):
#  print(ele1, ':', ele2)
