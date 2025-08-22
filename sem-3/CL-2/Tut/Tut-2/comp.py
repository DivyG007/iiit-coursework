import nltk
from nltk.corpus import brown

nltk.download('brown')

def lexical_diversity(tokens):
    return len(set(tokens)) / len(tokens)

results = {}
for genre in brown.categories():
    words = brown.words(categories=genre)
    diversity_normal = lexical_diversity(words)
    diversity_lower = lexical_diversity([w.lower() for w in words])
    results[genre] = (diversity_normal, diversity_lower)

print(f"{'Genre':<15}{'Normal Case':>15}{'Lower Case':>15}")
for genre, (norm, low) in results.items():
    print(f"{genre:<15}{norm:15.4f}{low:15.4f}")
