import pandas as pd


##Cargamos el archivo CSV con pandas como indice la columna IDENTIFICADOR y limitando la lectura a 10,000 filas
df = pd.read_csv(r'file/PEATONES_2020.csv', encoding="ISO-8859-1", delimiter=";", index_col="IDENTIFICADOR", nrows=10000)

##Mostramos la informacion del DataFrame
print(df.info())

##Mostramos las primeras filas del DataFrame
print(df.head())