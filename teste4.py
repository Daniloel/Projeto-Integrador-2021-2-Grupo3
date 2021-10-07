import pandas as pd

cv19 = pd.read_csv('caso_full.csv')

cv19 = cv19.drop("epidemiological_week", axis=1)
cv19 = cv19.drop("city_ibge_code", axis=1)
cv19 = cv19.drop("is_last", axis=1)
cv19 = cv19.drop("is_repeated", axis=1)
cv19 = cv19.drop("last_available_confirmed_per_100k_inhabitants", axis=1)
cv19 = cv19.drop("order_for_place", axis=1)
cv19 = cv19.drop("estimated_population_2019", axis=1)
cv19 = cv19.drop("last_available_date", axis=1)

colSP = cv19.loc[cv19["state"] == ("SP")]

cs= input("digite(city) para as cidades e (state) para o estadoSP:")

colSP1 = colSP.loc[colSP["place_type"] == cs]

if cs == "state":
    css= input("Digite a data nesse formato(ano-mês-data)ex:2021-04-25:")

    colDTS = colSP1.loc[colSP1["date"]== css]

    display(colDTS)

else:
    cd = input("Digite o nome da cidade(escreva com letras maiusculas e acento):")

    colCD = colSP1.loc[colSP1["city"] == cd]

    dt = input("Digite a data nesse formato(ano-mês-data)ex:2021-04-25:")
    colDT = colCD.loc[colCD["date"] == dt]
    display(colDT)
