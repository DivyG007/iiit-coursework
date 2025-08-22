import nltk
import pandas as pd
nltk.download('brown')
from nltk.corpus import brown
from collections import Counter
from functools import reduce

# count number of words per genre
print("Number of words per genre are:")
for i in brown.categories():
    print(i, ":" , len(brown.words(categories=i)))

print(end="\n")

# type-token ration per genre
# Type-token ratio per genre
print("Type-token ratio:")
for genre in brown.categories():
    # Get all words in the genre and convert to lowercase, filtering only alphabetic words
    words = [word.lower() for word in brown.words(categories=genre) if word.isalpha()]
    
    # Calculate the number of unique words (types) and total words (tokens)
    num_unique_words = len(set(words))  # Unique words
    num_total_words = len(words)        # Total words
    
    # Calculate and print the type-token ratio
    ttr = num_unique_words / num_total_words
    print(f"{genre}: {ttr:.4f}")

