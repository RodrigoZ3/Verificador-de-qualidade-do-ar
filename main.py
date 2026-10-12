# cspell:ignore qualidade, qualidade_ar, moderada, ruim, boa
import time 
import random

while True:
    time.sleep(1) 
    qualidade_ar = random.randint(0, 100)
    print(qualidade_ar)
    if qualidade_ar < 50:
            print("A qualidade do ar está ruim.")
    elif qualidade_ar < 80:
            print("A qualidade do ar está moderada.")
    else: 
        print("A qualidade do ar está boa.")
    

