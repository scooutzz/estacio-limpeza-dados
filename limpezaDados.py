import pandas as pd
import numpy as np

# 1. Leitura do CSV
df = pd.read_csv("dados.csv", sep=";", engine="python")

# 2. Informações gerais
print("\n-> Informações gerais:")
print(df.info())

# 3. Exibir primeiras e últimas 5 linhas
print("\n-> Primeiras linhas:")
print(df.head())
print("\n-> Últimas linhas:")
print(df.tail())

# 4. Criar cópia do DataFrame original
df_limpo = df.copy()

# 5. Substituir valores nulos da coluna 'Calories' por 0
df_limpo['Calories'] = df_limpo['Calories'].fillna(0)
print("\n-> Nulos em 'Calories' substituídos por 0:")

# 6. Substituir valores nulos da coluna 'Date' por '1900/01/01'
df_limpo['Date'] = df_limpo['Date'].fillna('1900/01/01')
print("\n-> Nulos em 'Date' substituídos por '1900/01/01':")

# 7. Tentar converter 'Date' para datetime (gera erro por causa de '1900/01/01')
try:
  df_limpo['Date'] = pd.to_datetime(df_limpo['Date'], format="%Y/%m/%d")
except Exception as e:
  print(f"\nXXX -> Erro na conversão: {e}")

# 8. Substituir '1900/01/01' por NaN
df_limpo['Date'] = df_limpo['Date'].replace('1900/01/01', np.nan)

# 9. Corrigir o valor '20201226' manualmente
df_limpo['Date'] = df_limpo['Date'].replace('20201226', '2020/12/26')

# 10. Tentar novamente converter para datetime
df_limpo['Date'] = pd.to_datetime(df_limpo['Date'], format="%Y/%m/%d", errors='coerce')

# 11. Remover linhas com valores nulos (restante)
df_limpo.dropna(inplace=True)

# 12. Mostrar resultado final
print("\n-> DataFrame final após limpeza:")
print(df_limpo)
