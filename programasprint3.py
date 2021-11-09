import pandas as pd

cv19 = pd.read_csv('caso_full3.csv')

cv19 = cv19.drop("epidemiological_week", axis=1)
cv19 = cv19.drop("city_ibge_code", axis=1)
cv19 = cv19.drop("is_last", axis=1)
cv19 = cv19.drop("is_repeated", axis=1)
cv19 = cv19.drop("last_available_confirmed_per_100k_inhabitants", axis=1)
cv19 = cv19.drop("order_for_place", axis=1)
cv19 = cv19.drop("estimated_population_2019", axis=1)
cv19 = cv19.drop("last_available_date", axis=1)

colSP = cv19.loc[cv19["state"] == ("SP")]

x = str('')

while x != ("cidade", "estado"):

    x = str(input("digite:(cidade) para as cidades, (estado) para estadoSP e(X) para finalizar pesquisa:")).lower()

    if x == "estado":

        colSP1 = colSP.loc[colSP["place_type"] == "state"]

        print('''Escolha uma das opçoes
                [ 1 ] data expecifica
                [ 2 ] todas as datas''')
        esc = str("")

        while esc != ("1", "2", "3"):

            esc = str(input('Digite a sua escolha(1 ou 2): '))

            if esc == "1":
                dt2 = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")

                colDT2 = colSP1.loc[colSP1["date"] == dt2]

                while colDT2.empty:
                    print("Data não encontrada\n Digite novamente")
                    dt2 = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")
                    colDT2 = colSP1.loc[colSP1["date"] == dt2]

                colDT2 = colDT2.drop("date", axis=1)
                colDT2 = colDT2.drop("state", axis=1)
                colDT2 = colDT2.drop("place_type", axis=1)
                colDT2.rename(columns={'city': 'cidade', 'estimated_population': 'população',
                                       'last_available_confirmed': 'últimos confirmados',
                                       'last_available_death_rate': 'taxa de óbitos',
                                       'last_available_deaths': 'últimos óbitos',
                                       'new_confirmed': 'casos dia', 'new_deaths': 'óbitos dia'}, inplace=True)

                print(colDT2)
                break
            elif esc == "2":
                dts2 = colSP1.loc[colSP1["date"] == "2021-05-10"]

                dts2 = dts2.drop("date", axis=1)
                dts2 = dts2.drop("state", axis=1)
                dts2 = dts2.drop("place_type", axis=1)
                dts2.rename(columns={'city': 'cidade', 'estimated_population': 'população',
                                     'last_available_confirmed': 'últimos confirmados',
                                     'last_available_death_rate': 'taxa de óbitos',
                                     'last_available_deaths': 'últimos óbitos',
                                     'new_confirmed': 'casos dia', 'new_deaths': 'óbitos dia'}, inplace=True)
                print(dts2)
            else:
                break

    elif x == "cidade":

        colSP1 = colSP.loc[colSP["place_type"] == "city"]

        cd = input("Digite o nome da cidade(escreva com letras maiusculas, minusculas e com acento)ex:São Paulo:")

        colCD = colSP1.loc[colSP1["city"] == cd]
        while colCD.empty:
            print("Cidade não encontrada\nDigite o nome da cidade novamente")
            cd = input("Digite o nome da cidade(escreva com letras maiusculas, minusculas e com acento)ex:São Paulo:")
            colCD = colSP1.loc[colSP1["city"] == cd]

        print('''Escolha uma das opçoes
                        [ 1 ] data expecifica
                        [ 2 ] todas as datas''')
        esc = ""

        while esc != ("1", "2"):
            esc = str(input('Digite a sua escolha(1 ou 2): '))

            if esc == "1":

                dt = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")
                colDT = colCD.loc[colCD["date"] == dt]

                while colDT.empty:
                    print("Data não encontrada\n Digite novamente")
                    dt = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")
                    colDT = colCD.loc[colCD["date"] == dt]

                colDT = colDT.drop("state", axis=1)
                colDT = colDT.drop("place_type", axis=1)
                colDT.rename(columns={'city': 'cidade', 'estimated_population': 'população',
                                      'last_available_confirmed': 'últimos confirmados',
                                      'last_available_death_rate': 'taxa de óbitos',
                                      'last_available_deaths': 'últimos óbitos',
                                      'new_confirmed': 'casos dia', 'new_deaths': 'óbitos dia'}, inplace=True)
                print(colDT)
                break



            elif esc == "2":
                dts = colCD.loc[colSP["date"] == "2021-05-10"]

                dts = dts.drop("date", axis=1)
                dts = dts.drop("state", axis=1)
                dts = dts.drop("place_type", axis=1)
                dts.rename(columns={'city': 'cidade', 'estimated_population': 'população',
                                    'last_available_confirmed': 'últimos confirmados',
                                    'last_available_death_rate': 'taxa de óbitos',
                                    'last_available_deaths': 'últimos óbitos',
                                    'new_confirmed': 'casos dia', 'new_deaths': 'óbitos dia'}, inplace=True)
                print(dts)
                break


    elif x == "x":
        break
