import pandas as pd

# 1. Cargar la base de datos
df = pd.read_csv('data/datos_inec_2021.csv', sep=';', encoding='latin-1')

# 2. Filtrar por provincia de Cotopaxi y cantón Latacunga
df_latacunga = df[(df['PROVINCIA'] == 'COTOPAXI') & (df['CANTÓN'] == 'LATACUNGA')]

# 3. Guardar el archivo filtrado
df_latacunga.to_csv('data/latacunga_siniestros_limpio.csv', index=False)

print("¡Procesamiento exitoso!")
print(f"Total de registros nacionales: {len(df)}")
print(f"Total de registros en Latacunga: {len(df_latacunga)}")
