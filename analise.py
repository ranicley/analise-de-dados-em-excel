import pandas as pd

# lendo os dados (nesse código, o arquivo Excel precisa estar na mesma pasta)
dados = pd.read_excel("")

dados.head()

dados.tail()


dados.shape

dados.info()

dados.describe()

dados['loja']

dados.loja

dados['loja'].unique()

dados['loja'].value_counts()

dados['loja'].value_counts(normalize=True)

# faturamento por loja
dados.groupby('loja').sum()

# média de faturament por loja (ticket médio)
dados.groupby('loja').mean()