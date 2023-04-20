
 '''------------------------------------------- 
Um exemplo de barra de progresso em python   
para o terminal. Execute pelo menos em  
python3.6.x, pois, função chr(x); x fica     
limitado a 0<=x<=256 nas versões anteriores. 
Mas, você pode usar outro caractere, exemplo:"#" 
B="["+("#"*(percentual))+"]"; (Qualquer Versão) 
----------------------------------------------''' 
def ProgressBar(percentual): 
  if(percentual>=0 or percentual<=100): 
     B="["+(chr(9632)*(percentual))+"]"; 
     print("\n",percentual,"%"+B); 
'''-------------------------------------------'''     
 
'''-------------------------------------------''' 
''' Simulando de 0 a 50%                      ''' 
'''-------------------------------------------''' 
import time 
Max = 50; 
for percentual in range(0,Max+1,1): 
    ProgressBar(percentual); 
    time.sleep(0.5); 
'''-------------------------------------------''' 
