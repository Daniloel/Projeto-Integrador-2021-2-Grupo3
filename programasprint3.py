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

print("\033[0;32mShark-Cov protótipo: filtro e procura de dados sobre a covid 19 no estado de SP;\033[m")
print("\033[0;32mFaça sua pesquisa conforme é pedido;\033[m")

x = str('')

while x != ("cidade", "estado"):

    x = str(input("\033[0;34mDigite:(cidade) para as cidades, (estado) para estadoSP e (X) para finalizar pesquisa: \033[m")).lower()

    if x == "estado":

        colSP1 = colSP.loc[colSP["place_type"] == "state"]

        print('''\033[0;35mEscolha uma das opçoes
                [ 1 ] data expecifica
                [ 2 ] última data disponível\033[m''')
        esc = str("")

        while esc != ("1", "2", "3"):

            esc = str(input('Digite a sua escolha(1 ou 2): '))

            if esc == "1":
                dt2 = input("\033[0;35mDigite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:\033[m")

                colDT2 = colSP1.loc[colSP1["date"] == dt2]

                while colDT2.empty:
                    print("\033[0;31mData não encontrada\n Digite novamente\033[m")
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

        cd = input("\033[0;34mDigite o nome da cidade(escreva com letras maiusculas, minusculas e com acento)ex:São Paulo: \033[m")

        colCD = colSP1.loc[colSP1["city"] == cd]
        while colCD.empty:
            print("\033[0;31mCidade não encontrada\nDigite o nome da cidade novamente\033[m")
            cd = input("\033[0;34mDigite o nome da cidade(escreva com letras maiusculas, minusculas e com acento)ex:São Paulo: \033[m")
            colCD = colSP1.loc[colSP1["city"] == cd]

        print('''\033[0;35mEscolha uma das opçoes
                        [ 1 ] data expecifica
                        [ 2 ] todas as datas\033[m''')
        esc = ""

        while esc != ("1", "2"):
            esc = str(input('Digite a sua escolha(1 ou 2): '))

            if esc == "1":

                dt = input("\033[0;35mDigite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:\033[m")
                colDT = colCD.loc[colCD["date"] == dt]

                while colDT.empty:
                    print("\033[0;31mData não encontrada\n Digite novamente\033[m")
                    dt = input("\033[0;35mDigite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd: \033[m")
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
