import pandas as pd

df = pd.read_csv('Agregados_por_setores_basico_BR_20250417.csv', encoding='latin1', sep=';')

print(df.head(10))
