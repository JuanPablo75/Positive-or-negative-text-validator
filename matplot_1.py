
import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv('resulting_data.csv')

df.columns
print(df[['Number of Retweets','Positive Score']])

print('iloc1',df.iloc[:])

#PARA LOCALIZAR ITEM EN FILA:
# df.iloc['numero de fila','columna que quieres']

print('fila 0, columna 0: ',df.iloc[0,0])

#PUEDES LOCALIZAR EN VARIAS FILAS:
#df.iloc['Nºde fila inicial':'Nº de fila final',(coma) columna que quieres(nombre pj)]
dev_x= df['Number of Retweets']
dev_y=df['Positive Score']
dev_ntv=df['Negative Score']
plt.bar(dev_ntv,dev_x)
plt.title('Nº of retweets for negative words in tweet')
plt.xlabel('Negative Words in tweet')
plt.ylabel('Retweets')
plt.bar(dev_y,dev_x)
plt.show()

plt.legend(['Neg words','Postv words'])
plt.bar(dev_y,dev_x)
plt.title('Nº of retweets for positive words in tweet')
plt.xlabel('Positive Words in tweet')
plt.ylabel('Retweeets')
plt.show()
