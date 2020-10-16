# %% Import libraries required
from operator import itemgetter
import nltk
import pandas as pd
from nltk.corpus import stopwords
from matplotlib import pyplot as plt

# %% Initialize frequency, and import all the words in a corpus
frequency = {}
words_doc = nltk.Text(nltk.corpus.gutenberg.words('carroll-alice.txt'))
stop_words = set(stopwords.words('english'))

# %% Convert to lower case and remove stop words
words_doc = [word.lower() for word in words_doc if word.isalpha()]
words_doc = [word for word in words_doc if word not in stop_words]

# %% Calculate the frequency of the words inside
for word in words_doc :
    count = frequency.get(word , 0)
    frequency[ word ] = count + 1

rank = 1
column_header = ['Rank', 'Frequency', 'Frequency * Rank']
df = pd.DataFrame( columns = column_header )
collection = sorted(frequency.items(), key=itemgetter(1), reverse = True)

# %%Creating a table for frequency * rank

for word , freq in collection:
    df.loc[word] = [rank, freq, rank*freq]
    rank = rank + 1
    
print (df)

# %% Python visualization with pyplot
plt.figure(figsize=(20,20))  #had to use this to increase the plot resolution
plt.ylabel("Frequency")
plt.xlabel("Words")
plt.xticks(rotation=90)    #to rotate x-axis values

for word , freq in collection[:30]:
    plt.bar(word, freq)    
plt.show()
# %% End of the program
