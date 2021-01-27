import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display 
import os
os.chdir('C:\\Users\\admin\\Desktop\\Kogni_3\\Analiza i wizualizacja danych')
os.getcwd()
os.listdir()

plik = "Spotify-2000.csv"

pd.set_option('display.expand_frame_repr', False)

#DANE
data = pd.read_csv(plik)


#ZMIENNE
energia = data["Energy"]
aku = data["Acousticness"]
glos = data["Loudness (dB)"]


#KORELACJE
#df = pd.read_csv("Spotify-2000.csv") 
#display(df.corr(method ='pearson'))


#WYKRES - głosnosc a energia (korelacja 0,73)
x = glos
y = energia
plt.plot(x,y, '.')
plt.xlabel("glosnoc")
plt.ylabel("energia")
plt.scatter(x,y)