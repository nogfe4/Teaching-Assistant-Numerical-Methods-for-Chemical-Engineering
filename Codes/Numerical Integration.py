
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import integrate 

"Códigos em python para integração numérica usando os métodos abordados nas disciplinas  de "
"Introdução à Engenharia Química II e Métodos Computacionais Aplicados a Engenharia Química da UERJ" 

"Author: Fernando Nogueira - @Nogfe4"

# Integrando a função y = x² tendo como os limites: a= 0 e b = 1 

x = np.linspace(0,1,100) # De zero a 1 plotando 1000 pontos
y = x**2 

integral_Simpson = integrate.simpson(y,x) 
#Função Integrate do SciPy que une os métodos 3/8 e 1/3 de Simpson
plt.fill_between(x, y, color='lightblue', alpha=0.4, label=f'Área integrada = {integral_Simpson:.4f}') 
# Deixando marcado a área que integramos
plt.plot(x, y, 'b')
plt.show()