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

cs = str(input("digite(city) para as cidades e (state) para estadoSP:")).lower()
# erro a corrigir, memso que vc escreva corretamente, só após a segunda tentativa correta o programa mostra os dados

while cs != ["city", "state"]:

    print("digite(city) para as cidades e (state) para estadoSP:")

    cs = str(input("digite(city) para as cidades e (state) para estadoSP:")).lower()

    if cs == "state":

        colSP1 = colSP.loc[colSP["place_type"] == cs]

        # from datetime import datetime

        css = input("Digite a data nesse formato(dia-mês-ano)ex:dd-mm-yyyy:")

        # data2 = datetime.strptime(css, '%d/%m/%y').date()

        colDTS = colSP1.loc[colSP1["date"] == css]

        colDTS = colDTS.drop("date", axis=1)
        colDTS = colDTS.drop("state", axis=1)
        colDTS = colDTS.drop("place_type", axis=1)

        print(colDTS)
        break

    elif cs == "city":

        colSP1 = colSP.loc[colSP["place_type"] == cs]

        cd = str.title(input("Digite o nome da cidade(escreva com letras maiusculas e acento)ex:São Paulo:"))

        colCD = colSP1.loc[colSP1["city"] == cd]

        dt = input("Digite a data nesse formato(ano-mês-data)ex:dd-mm-yyyy:")

        colDT = colCD.loc[colCD["date"] == dt]

        colDT = colDT.drop("date", axis=1)
        colDT = colDT.drop("state", axis=1)
        colDT = colDT.drop("place_type", axis=1)

        print(colDT)
        break
