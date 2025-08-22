import nltk
nltk.download('brown')
from nltk.corpus import brown

# Save words per genre into separate files
for genre in brown.categories():
    words = [word.lower() for word in brown.words(categories=genre) if word.isalpha()]
    with open(f"{genre}_words.txt", "w") as f:
        f.write("\n".join(words))