import pandas as pd
import numpy as np
import openpyxl as op

cv19p1= pd.read_csv('caso_full.csv')
cv19p1= cv19p1.drop("epidemiological_week", axis=1)
cv19p1= cv19p1.drop("city_ibge_code", axis=1)

colSP= cv19p1.loc[cv19p1["state"]== "SP"]

colNC= colSP.loc[colSP["city"]== input("Digite o nome da cidade(escreva com letras maiusculas e acento):")]

print(colNC)