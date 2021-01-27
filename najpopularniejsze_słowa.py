import pandas as pd
import os
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt


os.chdir('C:\\Users\\admin\\Desktop\\Kogni_3\\Analiza i wizualizacja danych')
os.getcwd()
os.listdir()
plik = "Spotify-2000.csv"

#WCZYTANIE DANYCH 
data = pd.read_csv(plik)

data_subset = data[["Title"]]


#DEFINIOWANIE
df = pd.DataFrame(data_subset)
a = df.to_string()
text = open("Spotify-2000.csv", encoding="utf8").read()
stopwords = set(STOPWORDS)
stopwords.update(["Remastered", "Remaster", "Version", "version", "Single","Live","De"])


#WYKRES
wordcloud = WordCloud(stopwords = stopwords, background_color="white").generate(a)
plt.imshow(wordcloud, interpolation='bilinear') 
plt.axis("off")
plt.show()
