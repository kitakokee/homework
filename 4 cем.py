
# 1 упр

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig = plt.figure(figsize = (16,9)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(111) 
x = [63.47, 71.66, 85.3, 97.73, 107.56, 110.4]
y = [320, 360, 428, 492, 540, 556]


# ставим точки функцией scatter, точки будем ставить крестиком
ax1.scatter(x, y, marker='x')
plt.plot(x,y, 'b^-', label='2x')

# поставим кресты погрешностей, linestyle = None, чтобы кресты не соединялись прямыми
ax1.errorbar(x, y, yerr=5, xerr =0.8 , color = 'k', linestyle = 'None')
# Добавим заголовок (в fontdict нужен словарь, шрифт должен поддерживаться matplotlib'ом)
plt.title('Our First Graph!', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

# Подпишем оси
plt.xlabel('Сила тока I, Амперы')
plt.ylabel('Напряжение U, Вольт')

plt.title('Зависимость напряжения от силы тока', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

ax1.grid() # делаем сетку

plt.show()
# для готового графика для лабы по общефизу не хватает только названия, подписанных осей и легенды, но это вы уже умеете
# успехов!

# 2

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(8,5), dpi=100)
#fig = plt.figure(figsize = (16,9)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(221) 
ax2 = fig.add_subplot(222) 
ax3 = fig.add_subplot(223) 
ax4 = fig.add_subplot(224) 

# сгенерируем данные для какой-нибудь гистограммы
values1 = np.random.normal(0, 10, 50)
values2= np.random.normal(0, 10, 100)
values3 = np.random.normal(0, 10, 1000)
values4 = np.random.normal(0, 10, 10000)
 
# строим гистограмму с 50 блоками
ax1.hist(values1, 50)
ax1.grid() # делаем сетку на графике ax1
ax1.set_title('50 блоков') # назвние графика ax1

# строим гистограмму с 100 блоками
ax2.hist(values2, 100)
ax2.grid() # делаем сетку на графике ax2
ax2.set_title('100 блоков') # назвние графика ax2

# строим гистограмму с 1000 блоками
ax3.hist(values3, 1000)
ax3.grid() # делаем сетку на графике ax3
ax3.set_title('1000 блоков') # назвние графика ax3

# строим гистограмму с 10000 блоками
ax4.hist(values4, 10000)
ax4.grid() # делаем сетку на графике ax4
ax4.set_title('10000 блоков') # назвние графика ax4

plt.show()


#3 упр


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris_data.csv') # Загрузка данных из файла iris_data.csv

species_percentage = df['Species'].value_counts(normalize=True) # Подсчет доли разных видов ирисов в датасете

petal_large = (df['PetalLengthCm'] > 1.2).mean() # Подсчет доли ирисов с длиной лепестка больше 1.2 см

petal_med = ((df['PetalLengthCm'] > 1.2) & (df['PetalLengthCm'] < 1.5)).mean() # Подсчет доли ирисов с длиной лепестка больше 1.2 см и меньше 1.5 см

petal_large_15 = (df['PetalLengthCm'] > 1.5).mean() # Подсчет доли ирисов с длиной лепестка больше 1.5 см

fig, axs = plt.subplots(1, 2, figsize=(12, 6)) # Построение круговых диаграмм


axs[0].pie(species_percentage, labels=species_percentage.index) # Диаграмма для доли разных видов ирисов
axs[0].set_title('Доля разных видов ирисов в датасете')


axs[1].pie([petal_large, petal_med, petal_large_15], labels=['>1.2см', '1.2-1.5см', '>1.5см']) # Диаграмма для доли ирисов с разной длиной лепестка
axs[1].set_title('Доля ирисов по длине лепестка')

plt.tight_layout()
plt.show()




# 4 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("iris_data.csv") # Загрузка данных из файла iris_data.csv

# Определяем комбинации
combinations = [
    ('SepalLengthCm', 'SepalWidthCm'),
    ('SepalLengthCm', 'PetalLengthCm'),
    ('SepalLengthCm', 'PetalWidthCm'),
    ('SepalWidthCm', 'PetalLengthCm'),
    ('SepalWidthCm', 'PetalWidthCm'),
    ('PetalLengthCm', 'PetalWidthCm')]

# Создание графиков
plt.figure(figsize=(16, 9))
for i, (x_col, y_col) in enumerate(combinations, start=1):
    plt.subplot(3, 2, i)
    plt.scatter(df[x_col], df[y_col], color='blue')
    plt.title(f"{y_col} vs {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    # Подгонка прямой МНК
    A = np.vstack([df[x_col], np.ones(len(df))]).T
    m, c = np.linalg.lstsq(A, df[y_col])[0]  # m - наклон, c - пересечение
    plt.plot(df[x_col], m * df[x_col] + c, color='red')
    plt.legend()

plt.tight_layout() # Для оптимизации расположения элементов графика
plt.show()


# 5(проблема с названиями штрихов по OX, слишом много)

import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
data = pd.read_csv('BTC_data.csv')

# Преобразование столбца с датами в формат datetime
data['time'] = pd.to_datetime(data['time'])

# Извлечение последней цены закрытия для каждой даты
closing_prices = data['close']

# Извлечение дат в формате DD-MM-YY

dates = data['time'].dt.strftime('%d-%m-%Y')
dates_2 =dates[::240]


# Построение графика

plt.plot(dates, closing_prices)
plt.xlabel('Дата')
plt.xticks(dates_2)
plt.ylabel('Цена закрытия')
plt.title('Исторический график цены биткоина')

plt.show()

# 6

import string

text = input()

# Заменяем знаки пунктуации пробелами
for i in string.punctuation:
    text = text.replace(i, " ")

# Приводим все слова к нижнему регистру
text = text.lower()

# Разбиваем текст на слова
words = text.split()

# Создаем словарь для хранения статистики
word_count = {}

# Считаем количество вхождений слов в текст
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Находим десять самых часто употребляемых слов, тем что ревёрсаем sorted =0
most_common_words = sorted(word_count, key=word_count.get, reverse=True)[:10]

# Выводим результат
for word in most_common_words:
    print(word, word_count[word])
