import pickle

from nltk.data import retrieve


# بعد fit()

with open("models/tfidf/tfidf_model.pkl", "wb") as f:

    pickle.dump(retrieve, f)

print("Model saved.")