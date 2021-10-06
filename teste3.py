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

#se colocar state no código abaixo não funciona, pois na coluna city não há um nome para os estado SP, apenas as cidades
colSP1 = colSP.loc[colSP["place_type"] == input("digite(city) para as cidades e (state) para o estadoSP:")]

# código abaixo não funciona(marcados com #)
#if colSP1.loc["place_type"== ("state")] 

#   colDTS = colSP1.loc[colSP1["date"]== input("Digite a data nesse formato(ano-mês-data)ex:2021-04-25:")]

#    display(colDTS)

#    else:

colCD = colSP1.loc[colSP1["city"] == input("Digite o nome da cidade(escreva com letras maiusculas e acento):")]

colDT = colCD.loc[colCD["date"] == input("Digite a data nesse formato(ano-mês-data)ex:2021-04-25:")]

display(colDT)
