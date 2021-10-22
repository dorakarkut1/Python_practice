import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./miasta.csv')
df.loc[10,:] = [2010,460,555,405]
print(df)
x = df['Rok']
y = df['Gdansk']

plt.plot(x,y, color='red', marker='o', fillstyle='none')
plt.show()

y2 = df['Poznan']
y3 = df['Szczecin']
plt.plot(x,y,'r:',x,y2,'b',x,y3,'g')
plt.legend(('Gdansk','Poznan', 'Szczecin'))
plt.xlabel('Lata')
plt.ylabel('Liczba ludnosci')
plt.title('Wykres ')
plt.grid(True)
plt.show()