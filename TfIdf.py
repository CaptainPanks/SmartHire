from sklearn.feature_extraction.text import TfidfVectorizer
corpus = ["This is very strange",
          "This is very nice"]
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus)
idf = vectorizer.idf_
tfidf = [[key,dict(zip(vectorizer.get_feature_names(), idf))[key]] for key in list(dict(zip(vectorizer.get_feature_names(), idf)).keys())]
tfidf = sorted(tfidf,key=lambda l:l[1], reverse=True)
print(tfidf)