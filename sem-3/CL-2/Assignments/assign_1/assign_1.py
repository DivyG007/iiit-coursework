import string
import nltk
# nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import math
import numpy as np
import unicodedata

text_1 = []

with open("dataset/pg10.txt", "r") as filereader_1:
    text_1 = filereader_1.read()

text_2 = []

with open("dataset/pg35997.txt", "r") as filereader_2:
    text_2 = filereader_2.read()

text = text_1 + text_2

# conversion to lowercase
tokens = word_tokenize(text.lower())

# removing punctuations
# tokens = list(filter(lambda token: token not in string.punctuation, tokens))

# Removing tokens that consist only of punctuation (including non-standard punctuation)
# tokens = list(filter(lambda token: not all(unicodedata.category(char).startswith('P') for char in token), tokens))
# tokens = [token for token in tokens if any(ch.isalnum() for ch in token)]
tokens = [
    token for token in tokens
    if not all(unicodedata.category(char).startswith('P') for char in token)
]


# task 1
for i in tokens:
    print(i,":",len(i))

# task 2
word_length = {}

for i in tokens:
    word_length[len(i)] = word_length.get(len(i), 0) + 1 

word_length = dict(sorted(word_length.items()))

for key, value in word_length.items():
    print(key,':',value)

# task 4

x = list(word_length.keys())
y = list(word_length.values())

plt.plot(x, y)
plt.xlabel("Word Length")
plt.ylabel("Frequency")
plt.title("Word Length vs Frequency")
plt.show()

# task 5
# to Ensure no zero or negative values for log10
x_log = [val for val in x if val > 0]
y_log = [y[i] for i in range(len(y)) if x[i] > 0]

# Apply log10 to filtered values
x_log = np.log10(x)
y_log = np.log10(y)

# Plot the log-log graph
plt.plot(x_log, y_log)
plt.xlabel("Log10(Word Length)")
plt.ylabel("Log10(Frequency)")
plt.title("Log-Log Plot of Word Length vs Frequency")
plt.show()

# task 6

x = np.array(x)
y = np.array(y)
n = len(x)
sigma_x = np.sum(x)
sigma_y = np.sum(y)
sigma_xy = np.sum(x*y)
sigma_of_x_square = np.sum(x**2)
sigma_of_y_square = np.sum(y**2)
square_of_sigma_x = sigma_x**2
square_of_sigma_y = sigma_y**2

# Pearson's coefficient of correlation
r = (n*sigma_xy - sigma_x*sigma_y)/math.sqrt((n*sigma_of_x_square - square_of_sigma_x)*(n*sigma_of_y_square - square_of_sigma_y))
print(r)
