import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt 


plik = 'Spotify-2000.csv'
data = pd.read_csv(plik)

# data.info()
# print(data.iloc[14])
# print(data.columns)

# queen = data[(data.Artist == 'Queen')]
# print(queen)

# beatles = data[(data.Artist == 'The Beatles')]
# print(beatles)

# coldplay = data[(data.Artist == 'Coldplay')]
# print(coldplay)


# print(queen['Energy'].mean())
# print(beatles['Energy'].mean())
# print(coldplay['Energy'].mean())

# x = ['Queen','Coldplay','The Beatles']
# y = [queen['Energy'].mean(),coldplay['Energy'].mean(),beatles['Energy'].mean()]

# plt.bar(x,y,color='teal')
# plt.title('Porównanie sredniej energetycznosci piosenek najpopularniejszych zespołów z listy')
# plt.xlabel('Zespół')
# plt.ylabel('Srednia energetycznosć piosenek')
# plt.show()


# print(data['Loudness (dB)'].max())
# print(data['Loudness (dB)'].min())
# max_loud = data[(data['Loudness (dB)'] == -2)]
# print(max_loud)

# min_loud = data[(data['Loudness (dB)'] == -27)]
# print(min_loud)

# max_loud_genre = max_loud['Top Genre']
# min_loud_genre = min_loud['Top Genre']

# print(max_loud_genre)
# print('..................')
# print(min_loud_genre)

#ZMIENNE GARUNEK I ROK
data_gatunek = data["Top Genre"]
data_rok = data["Year"]
data_subset = data[["Top Genre", "Year"]]

#LISTA GATUNKÓW I ILE RAZY WYSTĘPUJĄ
print([data_gatunek.groupby(data_gatunek).count()])

#COS WYSZŁO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

data_gatunek_rock = data_gatunek.str.contains("rock")
data_gatunek_pop = data_gatunek.str.contains("pop")
data_gatunek_hiphop = data_gatunek.str.contains("hip hop")
data_gatunek_metal = data_gatunek.str.contains("metal")
data_gatunek_indie = data_gatunek.str.contains("indie")
data_gatunek_soul = data_gatunek.str.contains("soul")
data_gatunek_reggae = data_gatunek.str.contains("reggae")
data_gatunek_jazz = data_gatunek.str.contains("jazz")
data_gatunek_folk = data_gatunek.str.contains("folk")
data_gatunek_country = data_gatunek.str.contains("country")
data_gatunek_punk = data_gatunek.str.contains("punk")
data_gatunek_house = data_gatunek.str.contains("house")
data_gatunek_latin = data_gatunek.str.contains("latin")
data_gatunek_dance = data_gatunek.str.contains("dance")



pusta_lista=[]
for i in range(len(data_gatunek)):
    if data_gatunek_rock[i] == True:
        pusta_lista.append("rock")
    elif data_gatunek_pop[i] == True:
        pusta_lista.append("pop")
    elif data_gatunek_hiphop[i] == True:
        pusta_lista.append("hip hop")
    elif data_gatunek_metal[i] == True:
        pusta_lista.append("metal")
    elif data_gatunek_indie[i] == True:
        pusta_lista.append("indie")
    elif data_gatunek_soul[i] == True:
        pusta_lista.append("soul")
    elif data_gatunek_reggae[i] == True:
        pusta_lista.append("reggae")
    elif data_gatunek_jazz[i] == True:
        pusta_lista.append("jazz")
    elif data_gatunek_folk[i] == True:
        pusta_lista.append("folk")
    elif data_gatunek_country[i] == True:
        pusta_lista.append("country")
    elif data_gatunek_punk[i] == True:
        pusta_lista.append("punk")
    elif data_gatunek_house[i] == True:
        pusta_lista.append("house")
    else:
        pusta_lista.append(data_gatunek[i])
    
        
#print(pusta_lista)
data["Top Genre"] = pusta_lista
print(data_gatunek)

# print([data_gatunek.groupby(data_gatunek).count()])


# Lata i głosnosc
print(data['Year'])

lista_max_loud = []
lista_min_loud = []


for i in range(1958,2020):
    data_lata = data[(data['Year'] == i)]
    print('ROK',i)
    maximum = data_lata['Loudness (dB)'].max()
    max_song = data_lata[(data_lata['Loudness (dB)'] == maximum)]
    minimum = data_lata['Loudness (dB)'].min()
    min_song = data_lata[(data_lata['Loudness (dB)'] == minimum)]
    most_freq_genre_min = min_song['Top Genre'].value_counts()
    most_freq_genre_max = max_song['Top Genre'].value_counts()
    print('Minimum:', minimum, '\n', min_song['Top Genre'])
    print('Czestosc gatunków w minimum:', most_freq_genre_min)
    print('Maximum:', maximum, '\n', max_song['Top Genre'])
    print('Czestosc gatunków w maximum:', most_freq_genre_max)
    lista_max_loud.append(maximum)
    lista_min_loud.append(minimum)

arr_min = np.array(lista_min_loud)
arr_max = np.array(lista_max_loud)

x1 = np.arange(1958,2020)
y1 = arr_max
y2 = arr_min

plt.plot(x1,y1, label = 'maksymalna głosnosc')
plt.plot(x1,y2, label = 'minimalna glosnosc')
plt.legend()
plt.title('głosnosc piosenek w czasie')
plt.xlabel('Rok')
plt.ylabel('Głosnosc')
plt.show()
    




