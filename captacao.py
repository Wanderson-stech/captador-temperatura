import random
from datetime import datetime

def captar_dados():
    temperatura = round(random.uniform(15.0, 30.0), 1)  # entre 15°C e 30°C
    umidade = round(random.uniform(30.0, 90.0), 1)       # entre 30% e 90%
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return data_hora, temperatura, umidade