import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plik = 'Spotify-2000.csv'
data = pd.read_csv(plik)



data_gatunek = data["Top Genre"]
data_rok = data["Year"]
data_subset = data[["Top Genre", "Year"]]

# #LISTA GATUNKÓW I ILE RAZY WYSTĘPUJĄ
# print([data_gatunek.groupby(data_gatunek).count()])

# #COS WYSZŁO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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


# Lata i głosnosc ROCK
print(data['Year'])

lista_rock_loud = []

for i in range(1970,2020):
    data_lata = data[(data['Year'] == i)]
    print('ROK',i)
    data_rock = data_lata[(data_lata['Top Genre'] == 'rock')]
    print(data_rock)
    mean_rock = data_rock['Loudness (dB)'].mean()
    lista_rock_loud.append(mean_rock)
print(lista_rock_loud)

arr_rock_loud = np.array(lista_rock_loud)
x = np.arange(1970,2020)
y = arr_rock_loud
plt.plot(x,y)
plt.title('Srednia głosnosc piosenek rockowych w czasie')
plt.xlabel('Rok')
plt.ylabel('Głosnosc')
plt.show()

