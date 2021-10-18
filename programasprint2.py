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

x = str(input("digite:(cidade) para as cidades e (estado) para estadoSP:")).lower()
# for cs in range(0, 1):
# print("")
# print("")
while x != ("cidade","estado"):

    x = str(input("digite:(cidade) para as cidades e (estado) para estadoSP:")).lower()

    if x == "estado":

        colSP1 = colSP.loc[colSP["place_type"] == "state"]

        css = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")

        colDTS = colSP1.loc[colSP1["date"] == css]

        colDTS = colDTS.drop("date", axis=1)
        colDTS = colDTS.drop("state", axis=1)
        colDTS = colDTS.drop("place_type", axis=1)

        print(colDTS)
        break


    elif x == "cidade":

        colSP1 = colSP.loc[colSP["place_type"] == "city"]

        cd = str.title(input("Digite o nome da cidade(escreva com letras maiusculas e acento)ex:São Paulo:"))

        colCD = colSP1.loc[colSP1["city"] == cd]

        dt = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")

        colDT = colCD.loc[colCD["date"] == dt]

        colDT = colDT.drop("date", axis=1)
        colDT = colDT.drop("state", axis=1)
        colDT = colDT.drop("place_type", axis=1)

        print(colDT)
        break
