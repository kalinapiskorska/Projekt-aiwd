import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


plik = 'Spotify-2000.csv'
data = pd.read_csv(plik)

# NAJPOPULARNIEJSZE ZESPOŁY A ŚREDNIA ENERGETYCZNOŚĆ ICH PIOSENEK

# Tworzenie nowych df, które zawierają tylko piosenki tych artystów
queen = data[(data.Artist == 'Queen')]
print(queen)

beatles = data[(data.Artist == 'The Beatles')]
print(beatles)

coldplay = data[(data.Artist == 'Coldplay')]
print(coldplay)

# Obliczam średnią energetyczność ich piosenek z listy
print(queen['Energy'].mean())
print(beatles['Energy'].mean())
print(coldplay['Energy'].mean())

# Ustalam osie wykresu
x = ['Queen','Coldplay','The Beatles']
y = [queen['Energy'].mean(),coldplay['Energy'].mean(),beatles['Energy'].mean()]

# Rysuję wykres
plt.bar(x,y,color='teal')
# plt.title('Porównanie średniej energetyczności piosenek najpopularniejszych zespołów')
plt.xlabel('Zespół')
plt.ylabel('Średnia energetyczność piosenek')
plt.show()


# ZMIENNOŚĆ GŁOŚNOŚCI W CZASIE

# Sprawdzam, które lata występują na liście
print(data['Year'])

# Tworzę puste listy, do których będą dodawane skrajne wartości głośności dla każdego roku
lista_max_loud = []
lista_min_loud = []

# Wybieram lata 1958-2020, ponieważ na liście spotify nie ma żadnej piosenki z 1957
# Pętla dodaje do list wartości minimalne i maksymalne głośności i printuje jakie to piosenki
for i in range(1958,2020):
    data_lata = data[(data['Year'] == i)]
    print('ROK',i)
    maximum = data_lata['Loudness (dB)'].max()
    max_song = data_lata[(data_lata['Loudness (dB)'] == maximum)]
    minimum = data_lata['Loudness (dB)'].min()
    min_song = data_lata[(data_lata['Loudness (dB)'] == minimum)]
    print('Minimum:', minimum, '\n', min_song['Title'], min_song['Artist'])
    print('Maximum:', maximum, '\n', max_song['Title'], max_song['Artist'])
    lista_max_loud.append(maximum)
    lista_min_loud.append(minimum)

# Tworzę osie - czas z np.arange, wartości z wcześniej stworzonych list
x1 = np.arange(1958,2020)
y1 = lista_max_loud
y2 = lista_min_loud

# Rysuję wykres z legendą
plt.plot(x1,y1, label = 'maksymalna głosność')
plt.plot(x1,y2, label = 'minimalna glosność')
plt.legend()
# plt.title('Głośność piosenek w dziedzinie czasu')
plt.xlabel('Rok')
plt.ylabel('Głośność')
plt.show()
