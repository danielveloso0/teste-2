import pandas as pd 

tabela = {'país':["Brasil","Rússia",'Argentina','Finlândia'],'valor':[50,150,25,100]}
df = pd.DataFrame(tabela)
print(df.head())
import matplotlib.pyplot as plt
plt.bar(x=df['país'],height=df['valor'])
plt.show()