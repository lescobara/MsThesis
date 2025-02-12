import pandas as pd
import scipy.stats as stats
import argparse

#Cargar el nombre del archivo como parametro
parser = argparse.ArgumentParser(description="Realizar ANOVA en un archivo CSV.")
parser.add_argument('filename', type=str, help='El nombre del archivo CSV que contiene los datos')

# Parsear los argumentos
args = parser.parse_args()

# Leer el archivo CSV
data = pd.read_csv(args.filename, header=None, sep='\t')

print (data)

# Carga de datos
group1 = data.iloc[0].tolist()
group2 = data.iloc[1].tolist()
group3 = data.iloc[2].tolist()
group4 = data.iloc[3].tolist()

# Realizar ANOVA de un solo factor
f_statistic, p_value = stats.f_oneway(group1, group2, group3, group4)

# Mostrar los resultados
print("F-Statistic:", f_statistic)
print("P-Value:", p_value)
