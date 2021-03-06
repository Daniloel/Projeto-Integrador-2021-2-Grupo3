import matplotlib.pyplot as plt
import pandas as pd
from unidecode import unidecode

co = pd.read_csv('caso_full.csv')
co = co.drop("epidemiological_week", axis=1)
co = co.drop("city_ibge_code", axis=1)
co = co.drop("is_last", axis=1)
co = co.drop("is_repeated", axis=1)
co = co.drop("last_available_confirmed_per_100k_inhabitants", axis=1)
co = co.drop("order_for_place", axis=1)
co = co.drop("estimated_population_2019", axis=1)
co = co.drop("last_available_date", axis=1)

colSP = co.loc[co["state"] == ("SP")]

def removeA(s):
    return unidecode(s.lower())

print("\033[0;32mShark-Cov protótipo: filtro e procura de dados sobre a covid 19 no estado de SP;\033[m")
print("\033[0;32mFaça sua pesquisa conforme é pedido;\033[m")

x = str('')

while x != ("cidade", "estado"):

    x = str(input(
        "\033[0;34mDigite:(cidade) para as cidades, (estado) para estadoSP e (X) para finalizar pesquisa: \033[m")).lower()

    if x == "estado":

        colSP1 = colSP.loc[colSP["place_type"] == "state"]

        plpl = str("")
        while plpl !=("90"):
            print('''[ 1 ] dado específico
                        [ 2 ] comparações
                            [ x ] Voltar a escolha das cidades/estado''')
            F = input("Digite a sua escolha: ")

            if F == "1":
                print("escolha entre os dados disponíveis(abaixo):")
                print('''[ 1 ] Casos confirmados
                                             [ 2 ] Óbitos confirmados''')
                FF = input("Digite a sua escolha: ")

                if FF == "1":

                    print('''\033[0;35mEscolha uma das opçoes
                                                [ 1 ] data expecifica
                                                [ 2 ] última data disponível
                                                [ 3 ] Ano de 2020
                                                [ 4 ] Ano de 2021
                                                [ 5 ] 1ºSemestre 2020
                                                [ 6 ] 2ºSemestre 2020
                                                [ 7 ] 1ºSemestre 2021
                                                [ 8 ] 2ºSemestre 2021
                                                [ 9 ] Range inputável\033[m''')
                    esc = str("")

                    while esc != ("1", "2", "3", "4", "5", "6", "7", "8"):

                        esc = str(input('Digite a sua escolha(1, 2, 3, 4, 5 ,6, 7, 8, 9): '))

                        if esc == "1":
                            dt2 = input("\033[0;35mDigite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:\033[m")

                            colDT2 = colSP1.loc[colSP1["date"] == dt2]

                            while colDT2.empty:
                                print("\033[0;31mData não encontrada\n Digite novamente\033[m")
                                dt2 = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")
                                colDT2 = colSP1.loc[colSP1["date"] == dt2]

                            colDT2 = colDT2.drop("state", axis=1)
                            colDT2 = colDT2.drop("place_type", axis=1)

                            plt.bar(colDT2['date'], colDT2['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = colDT2.sum()
                            print("Casos de Covid no dia:")
                            print(xxxx["new_confirmed"])
                            plt.show()
                            break
                        elif esc == "2":
                            dts2 = colSP1.loc[colSP1["date"] == "2021-05-10"]

                            dts2 = dts2.drop("state", axis=1)
                            dts2 = dts2.drop("place_type", axis=1)

                            plt.bar(dts2['date'], dts2['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = dts2.sum()
                            print("Casos de Covid no dia:")
                            print(xxxx["new_confirmed"])
                            plt.show()
                            break
                        elif esc == "3":
                            Y = colSP1[colSP1["date"].between("2020-01-01", "2020-12-31")]
                            Y = Y.drop("state", axis=1)
                            Y = Y.drop("place_type", axis=1)

                            plt.plot(Y['date'], Y['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = Y.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()

                            break

                        elif esc == "4":
                            y = colSP1[colSP1["date"].between("2021-01-01", "2021-12-31")]
                            y = y.drop("state", axis=1)
                            y = y.drop("place_type", axis=1)

                            plt.plot(y['date'], y['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = y.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()
                            break

                        elif esc == "5":
                            s = colSP1[colSP1["date"].between("2020-01-01", "2020-06-30")]
                            s = s.drop("state", axis=1)
                            s = s.drop("place_type", axis=1)
                            plt.plot(s['date'], s['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = s.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()

                            break

                        elif esc == "6":

                            oi = colSP1[colSP1["date"].between("2020-07-01", "2020-12-31")]
                            oi = oi.drop("state", axis=1)
                            oi = oi.drop("place_type", axis=1)
                            plt.plot(oi['date'], oi['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = oi.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()

                            break

                        elif esc == "7":
                            s1 = colSP1[colSP1["date"].between("2021-01-01", "2021-06-30")]
                            s1 = s1.drop("state", axis=1)
                            s1 = s1.drop("place_type", axis=1)

                            plt.plot(s1['date'], s1['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = s1.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()
                            break

                        elif esc == "8":
                            S1 = colSP1[colSP1["date"].between("2021-07-01", "2021-12-31")]
                            S1 = S1.drop("state", axis=1)
                            S1 = S1.drop("place_type", axis=1)

                            plt.plot(S1['date'], S1['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = S1.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()
                            break


                        elif esc == "9":

                            XX = input("\033[0;34mData 1 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                            XXX = input("\033[0;34mData 2 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                            S1 = colSP1[colSP1["date"].between(f"{XX}", f"{XXX}")]

                            while S1.empty:
                                print("\033[0;31mData(s) inválida(s)\nDigite novamente\033[m")

                                XX = input(

                                    "\033[0;34mData 1 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                                XXX = input("\033[0;34mData 2 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                                S1 = colSP1[colSP1["date"].between(f"{XX}", f"{XXX}")]

                            plt.plot(S1['date'], S1['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = S1.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()

                            break
                elif FF == "2":
                    print('''\033[0;35mEscolha uma das opçoes
                                                                    [ 1 ] data expecifica
                                                                    [ 2 ] última data disponível
                                                                    [ 3 ] Ano de 2020
                                                                    [ 4 ] Ano de 2021
                                                                    [ 5 ] 1ºSemestre 2020
                                                                    [ 6 ] 2ºSemestre 2020
                                                                    [ 7 ] 1ºSemestre 2021
                                                                    [ 8 ] 2ºSemestre 2021
                                                                    [ 9 ] Range inputável\033[m''')
                    esc = str("")

                    while esc != ("1", "2", "3", "4", "5", "6", "7", "8"):

                        esc = str(input('Digite a sua escolha(1, 2, 3, 4, 5 ,6, 7, 8, 9): '))

                        if esc == "1":
                            dt2 = input("\033[0;35mDigite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:\033[m")

                            colDT2 = colSP1.loc[colSP1["date"] == dt2]

                            while colDT2.empty:
                                print("\033[0;31mData não encontrada\n Digite novamente\033[m")
                                dt2 = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")
                            colDT2 = colDT2.drop("state", axis=1)
                            colDT2 = colDT2.drop("place_type", axis=1)
                            plt.bar(colDT2['date'], colDT2['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = colDT2.sum()
                            print("Óbitos por Covid no dia:")
                            print(xxxx["new_deaths"])
                            plt.show()
                            break
                        elif esc == "2":
                            dts2 = colSP1.loc[colSP1["date"] == "2021-11-10"]

                            dts2 = dts2.drop("state", axis=1)
                            dts2 = dts2.drop("place_type", axis=1)
                            plt.bar(dts2['date'], dts2['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = dts2.sum()
                            print("Óbitos por Covid no dia:")
                            print(xxxx["new_deaths"])
                            plt.show()
                            break
                        elif esc == "3":
                            Y = colSP1[colSP1["date"].between("2020-01-01", "2020-12-31")]
                            Y = Y.drop("state", axis=1)
                            Y = Y.drop("place_type", axis=1)
                            plt.plot(Y['date'], Y['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = Y.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()


                            break

                        elif esc == "4":
                            y = colSP1[colSP1["date"].between("2021-01-01", "2021-12-31")]
                            y = y.drop("state", axis=1)
                            y = y.drop("place_type", axis=1)

                            plt.plot(y['date'], y['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = y.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()
                            break

                        elif esc == "5":
                            s = colSP1[colSP1["date"].between("2020-01-01", "2020-06-30")]
                            s = s.drop("state", axis=1)
                            s = s.drop("place_type", axis=1)
                            plt.plot(s['date'], s['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = s.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()

                            break

                        elif esc == "6":

                            oi = colSP1[colSP1["date"].between("2020-07-01", "2020-12-31")]
                            oi = oi.drop("state", axis=1)
                            oi = oi.drop("place_type", axis=1)
                            plt.plot(oi['date'], oi['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = oi.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()

                            break

                        elif esc == "7":
                            s1 = colSP1[colSP1["date"].between("2021-01-01", "2021-06-30")]
                            s1 = s1.drop("state", axis=1)
                            s1 = s1.drop("place_type", axis=1)

                            plt.plot(s1['date'], s1['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = s1.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()
                            break

                        elif esc == "8":
                            S1 = colSP1[colSP1["date"].between("2021-07-01", "2021-12-31")]
                            S1 = S1.drop("state", axis=1)
                            S1 = S1.drop("place_type", axis=1)

                            plt.plot(S1['date'], S1['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = S1.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()
                            break


                        elif esc == "9":

                            XX = input("\033[0;34mData 1 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                            XXX = input("\033[0;34mData 2 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                            S1 = colSP1[colSP1["date"].between(f"{XX}", f"{XXX}")]

                            while S1.empty:
                                print("\033[0;31mData(s) inválida(s)\nDigite novamente\033[m")

                                XX = input(

                                    "\033[0;34mData 1 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                                XXX = input("\033[0;34mData 2 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                                S1 = colSP1[colSP1["date"].between(f"{XX}", f"{XXX}")]

                            plt.plot(S1['date'], S1['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = S1.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()

                            break
            elif F == "2":
                print('''\033[0;35mEscolha uma das opçoes
                                                                                                [ 1 ] data expecifica
                                                                                                [ 2 ] última data disponível
                                                                                                [ 3 ] Ano de 2020
                                                                                                [ 4 ] Ano de 2021
                                                                                                [ 5 ] 1ºSemestre 2020
                                                                                                [ 6 ] 2ºSemestre 2020
                                                                                                [ 7 ] 1ºSemestre 2021
                                                                                                [ 8 ] 2ºSemestre 2021
                                                                                                [ 9 ] Range inputável\033[m''')
                esc = str("")

                while esc != ("1", "2", "3", "4", "5", "6", "7", "8"):

                    esc = str(input('Digite a sua escolha(1, 2, 3, 4, 5 ,6, 7, 8, 9): '))

                    if esc == "1":
                        dt2 = input("\033[0;35mDigite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:\033[m")

                        colDT2 = colSP1.loc[colSP1["date"] == dt2]

                        while colDT2.empty:
                            print("\033[0;31mData não encontrada\n Digite novamente\033[m")
                            dt2 = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")
                            colDT2 = colSP1.loc[colSP1["date"] == dt2]
                        colDT2 = colDT2.drop("state", axis=1)
                        colDT2 = colDT2.drop("place_type", axis=1)
                        plt.plot(colDT2["date"], colDT2["new_deaths"], label="Óbitos confirmados")
                        plt.plot(colDT2["date"], colDT2["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel(f"{dt2}")
                        xxxx = colDT2.sum()
                        print("Óbitos por Covid no dia:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no dia:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

                    elif esc == "2":
                        dts2 = colSP1.loc[colSP1["date"] == "2021-11-10"]
                        dts2 = dts2.drop("state", axis=1)
                        dts2 = dts2.drop("place_type", axis=1)
                        plt.plot(dts2["date"], dts2["new_deaths"], label="Óbitos confirmados")
                        plt.plot(dts2["date"], dts2["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("2021-11-10")
                        xxxx = dts2.sum()
                        print("Óbitos por Covid no dia:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no dia:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

                    elif esc == "3":
                        Y = colSP1[colSP1["date"].between("2020-01-01", "2020-12-31")]
                        Y = Y.drop("state", axis=1)
                        Y = Y.drop("place_type", axis=1)
                        plt.plot(Y["date"], Y["new_deaths"], label="Óbitos confirmados")
                        plt.plot(Y["date"], Y["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("01/01/2020 à 31/12/2020")
                        xxxx = Y.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()

                        break

                    elif esc == "4":
                        y = colSP1[colSP1["date"].between("2021-01-01", "2021-12-31")]
                        y = y.drop("state", axis=1)
                        y = y.drop("place_type", axis=1)
                        plt.plot(y["date"], y["new_deaths"], label="Óbitos confirmados")
                        plt.plot(y["date"], y["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("2021-01-01 à 2021-12-31")
                        xxxx = y.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

                    elif esc == "5":
                        s = colSP1[colSP1["date"].between("2020-01-01", "2020-06-30")]
                        s = s.drop("state", axis=1)
                        s = s.drop("place_type", axis=1)
                        plt.plot(s["date"], s["new_deaths"], label="Óbitos confirmados")
                        plt.plot(s["date"], s["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("2020-01-01 à 2020-06-30")
                        xxxx = s.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

                    elif esc == "6":

                        oi = colSP1[colSP1["date"].between("2020-07-01", "2020-12-31")]
                        oi = oi.drop("state", axis=1)
                        oi = oi.drop("place_type", axis=1)
                        plt.plot(oi["date"], oi["new_deaths"], label="Óbitos confirmados")
                        plt.plot(oi["date"], oi["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("2020-07-01 à 2020-12-31")
                        xxxx = oi.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

                    elif esc == "7":
                        s1 = colSP1[colSP1["date"].between("2021-01-01", "2021-06-30")]
                        s1 = s1.drop("state", axis=1)
                        s1 = s1.drop("place_type", axis=1)
                        plt.plot(s1["date"], s1["new_deaths"], label="Óbitos confirmados")
                        plt.plot(s1["date"], s1["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("2021-01-01 à 2021-06-30")
                        xxxx = s1.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

                    elif esc == "8":
                        S1 = colSP1[colSP1["date"].between("2021-07-01", "2021-12-31")]
                        S1 = S1.drop("state", axis=1)
                        S1 = S1.drop("place_type", axis=1)
                        plt.plot(S1["date"], S1["new_deaths"], label="Óbitos confirmados")
                        plt.plot(S1["date"], S1["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("2021-07-01 à 2021-12-31")
                        xxxx = S1.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break



                    elif esc == "9":

                        XX = input("\033[0;34mData 1 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                        XXX = input("\033[0;34mData 2 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                        S1 = colSP1[colSP1["date"].between(f"{XX}", f"{XXX}")]

                        while S1.empty:
                            print("\033[0;31mData(s) inválida(s)\nDigite novamente\033[m")

                            XX = input(

                                "\033[0;34mData 1 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                            XXX = input("\033[0;34mData 2 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                            S1 = colSP1[colSP1["date"].between(f"{XX}", f"{XXX}")]
                        S1 = S1.drop("state", axis=1)
                        S1 = S1.drop("place_type", axis=1)
                        plt.plot(S1["date"], S1["new_deaths"], label="Óbitos confirmados")
                        plt.plot(S1["date"], S1["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel(f"{XX} à {XXX}")
                        xxxx = S1.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

            elif F == "x":
                break




    elif x == "cidade":

        colSP1 = colSP.loc[colSP["place_type"] == "city"]

        cd = input(
            "\033[0;34mDigite o nome da cidade(escreva com letras maiusculas, minusculas e com acento)ex:São Paulo: \033[m")

        colCD = colSP1.loc[colSP1["city"].apply(removeA) == removeA(cd)]
        while colCD.empty:
            print("\033[0;31mCidade não encontrada\nDigite o nome da cidade novamente\033[m")
            cd = input(
                "\033[0;34mDigite o nome da cidade(escreva com letras maiusculas, minusculas e com acento)ex:São Paulo: \033[m")
            colCD = colSP1.loc[colSP1["city"].apply(removeA) == removeA(cd)]

        plpl = str("")
        while plpl != ("90"):
            print('''[ 1 ] dado específico
            [ 2 ] comparações
                [ x ] Voltar a escolha das cidades/estado''')
            F = input("Digite a sua escolha: ")

            if F == "1":
                print("escolha entre os dados disponíveis(abaixo):")
                print('''[ 1 ] Casos confirmados
                                 [ 2 ] Óbitos confirmados''')
                FF = input("Digite a sua escolha: ")

                if FF == "1":

                    print('''\033[0;35mEscolha uma das opçoes
                                    [ 1 ] data expecifica
                                    [ 2 ] última data disponível
                                    [ 3 ] Ano de 2020
                                    [ 4 ] Ano de 2021
                                    [ 5 ] 1ºSemestre 2020
                                    [ 6 ] 2ºSemestre 2020
                                    [ 7 ] 1ºSemestre 2021
                                    [ 8 ] 2ºSemestre 2021
                                    [ 9 ] Range inputável\033[m''')
                    esc = str("")

                    while esc != ("1", "2", "3", "4", "5", "6", "7", "8"):

                        esc = str(input('Digite a sua escolha(1, 2, 3, 4, 5 ,6, 7, 8, 9): '))

                        if esc == "1":
                            dt2 = input("\033[0;35mDigite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:\033[m")

                            colDT2 = colCD.loc[colCD["date"] == dt2]

                            while colDT2.empty:
                                print("\033[0;31mData não encontrada\n Digite novamente\033[m")
                                dt2 = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")
                                colDT2 = colCD.loc[colCD["date"] == dt2]

                            colDT2 = colDT2.drop("state", axis=1)
                            colDT2 = colDT2.drop("place_type", axis=1)

                            plt.bar(colDT2['date'], colDT2['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = colDT2.sum()
                            print("Casos de Covid no dia:")
                            print(xxxx["new_confirmed"])
                            plt.show()
                            break
                        elif esc == "2":
                            dts2 = colCD.loc[colCD["date"] == "2021-11-10"]

                            dts2 = dts2.drop("state", axis=1)
                            dts2 = dts2.drop("place_type", axis=1)

                            plt.bar(dts2['date'], dts2['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = dts2.sum()
                            print("Casos de Covid no dia:")
                            print(xxxx["new_confirmed"])
                            plt.show()
                            break
                        elif esc == "3":
                            Y = colCD[colCD["date"].between("2020-01-01", "2020-12-31")]
                            Y = Y.drop("state", axis=1)
                            Y = Y.drop("place_type", axis=1)

                            plt.plot(Y['date'], Y['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = Y.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()

                            break

                        elif esc == "4":
                            y = colCD[colCD["date"].between("2021-01-01", "2021-12-31")]
                            y = y.drop("state", axis=1)
                            y = y.drop("place_type", axis=1)

                            plt.plot(y['date'], y['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = y.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()
                            break

                        elif esc == "5":
                            s = colCD[colCD["date"].between("2020-01-01", "2020-06-30")]
                            s = s.drop("state", axis=1)
                            s = s.drop("place_type", axis=1)
                            plt.plot(s['date'], s['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = s.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()

                            break

                        elif esc == "6":

                            oi = colCD[colCD["date"].between("2020-07-01", "2020-12-31")]
                            oi = oi.drop("state", axis=1)
                            oi = oi.drop("place_type", axis=1)
                            plt.plot(oi['date'], oi['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = oi.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()

                            break

                        elif esc == "7":
                            s1 = colCD[colCD["date"].between("2021-01-01", "2021-06-30")]
                            s1 = s1.drop("state", axis=1)
                            s1 = s1.drop("place_type", axis=1)

                            plt.plot(s1['date'], s1['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = s1.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()
                            break

                        elif esc == "8":
                            S1 = colCD[colCD["date"].between("2021-07-01", "2021-12-31")]
                            S1 = S1.drop("state", axis=1)
                            S1 = S1.drop("place_type", axis=1)

                            plt.plot(S1['date'], S1['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = S1.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()
                            break


                        elif esc == "9":

                            XX = input("\033[0;34mData 1 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                            XXX = input("\033[0;34mData 2 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                            S1 = colCD[colCD["date"].between(f"{XX}", f"{XXX}")]

                            while S1.empty:
                                print("\033[0;31mData(s) inválida(s)\nDigite novamente\033[m")

                                XX = input(

                                    "\033[0;34mData 1 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                                XXX = input("\033[0;34mData 2 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                                S1 = colCD[colCD["date"].between(f"{XX}", f"{XXX}")]

                            plt.plot(S1['date'], S1['new_confirmed'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de casos por dia')  # Título do gráfico
                            xxxx = S1.sum()
                            print("Casos de Covid no período:")
                            print(xxxx["new_confirmed"])
                            plt.show()

                            break
                elif FF == "2":
                    print('''\033[0;35mEscolha uma das opçoes
                                                        [ 1 ] data expecifica
                                                        [ 2 ] última data disponível
                                                        [ 3 ] Ano de 2020
                                                        [ 4 ] Ano de 2021
                                                        [ 5 ] 1ºSemestre 2020
                                                        [ 6 ] 2ºSemestre 2020
                                                        [ 7 ] 1ºSemestre 2021
                                                        [ 8 ] 2ºSemestre 2021
                                                        [ 9 ] Range inputável\033[m''')
                    esc = str("")

                    while esc != ("1", "2", "3", "4", "5", "6", "7", "8"):

                        esc = str(input('Digite a sua escolha(1, 2, 3, 4, 5 ,6, 7, 8, 9): '))

                        if esc == "1":
                            dt2 = input("\033[0;35mDigite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:\033[m")

                            colDT2 = colCD.loc[colCD["date"] == dt2]

                            while colDT2.empty:
                                print("\033[0;31mData não encontrada\n Digite novamente\033[m")
                                dt2 = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")
                                colDT2 = colCD.loc[colCD["date"] == dt2]

                            colDT2 = colDT2.drop("state", axis=1)
                            colDT2 = colDT2.drop("place_type", axis=1)

                            plt.bar(colDT2['date'], colDT2['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = colDT2.sum()
                            print("Óbitos por Covid no dia:")
                            print(xxxx["new_deaths"])
                            plt.show()
                            break
                        elif esc == "2":
                            dts2 = colCD.loc[colCD["date"] == "2021-05-10"]

                            dts2 = dts2.drop("state", axis=1)
                            dts2 = dts2.drop("place_type", axis=1)

                            plt.bar(dts2['date'], dts2['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = dts2.sum()
                            print("Óbitos por Covid no dia:")
                            print(xxxx["new_deaths"])
                            plt.show()
                            break
                        elif esc == "3":
                            Y = colCD[colCD["date"].between("2020-01-01", "2020-12-31")]
                            Y = Y.drop("state", axis=1)
                            Y = Y.drop("place_type", axis=1)

                            plt.plot(Y['date'], Y['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = Y.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()

                            break

                        elif esc == "4":
                            y = colCD[colCD["date"].between("2021-01-01", "2021-12-31")]
                            y = y.drop("state", axis=1)
                            y = y.drop("place_type", axis=1)

                            plt.plot(y['date'], y['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = y.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()
                            break

                        elif esc == "5":
                            s = colCD[colCD["date"].between("2020-01-01", "2020-06-30")]
                            s = s.drop("state", axis=1)
                            s = s.drop("place_type", axis=1)
                            plt.plot(s['date'], s['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = s.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()

                            break

                        elif esc == "6":

                            oi = colCD[colCD["date"].between("2020-07-01", "2020-12-31")]
                            oi = oi.drop("state", axis=1)
                            oi = oi.drop("place_type", axis=1)
                            plt.plot(oi['date'], oi['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = oi.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()

                            break

                        elif esc == "7":
                            s1 = colCD[colCD["date"].between("2021-01-01", "2021-06-30")]
                            s1 = s1.drop("state", axis=1)
                            s1 = s1.drop("place_type", axis=1)

                            plt.plot(s1['date'], s1['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = s1.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()
                            break

                        elif esc == "8":
                            S1 = colCD[colCD["date"].between("2021-07-01", "2021-12-31")]
                            S1 = S1.drop("state", axis=1)
                            S1 = S1.drop("place_type", axis=1)

                            plt.plot(S1['date'], S1['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Data')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = S1.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()
                            break


                        elif esc == "9":

                            XX = input("\033[0;34mData 1 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                            XXX = input("\033[0;34mData 2 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                            S1 = colCD[colCD["date"].between(f"{XX}", f"{XXX}")]

                            while S1.empty:
                                print("\033[0;31mData(s) inválida(s)\nDigite novamente\033[m")

                                XX = input(

                                    "\033[0;34mData 1 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                                XXX = input("\033[0;34mData 2 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                                S1 = colCD[colCD["date"].between(f"{XX}", f"{XXX}")]

                            plt.plot(S1['date'], S1['new_deaths'], label='Casos', color='g', ls='--',
                                    lw='2')  # Caso queira grafico de barras colocar - plt.bar()
                            plt.legend(loc=2, fontsize='15')  # Personalização da legenda
                            plt.ylabel('Casos Confirmados')  # Nome do Eixo Y
                            plt.xlabel('Datas')  # Nome do Eixo X
                            plt.title('Gráfico situação de óbitos por dia')  # Título do gráfico
                            xxxx = S1.sum()
                            print("Óbitos por Covid no período:")
                            print(xxxx["new_deaths"])
                            plt.show()

                            break
            elif F == "2":
                print('''\033[0;35mEscolha uma das opçoes
                                                                                    [ 1 ] data expecifica
                                                                                    [ 2 ] última data disponível
                                                                                    [ 3 ] Ano de 2020
                                                                                    [ 4 ] Ano de 2021
                                                                                    [ 5 ] 1ºSemestre 2020
                                                                                    [ 6 ] 2ºSemestre 2020
                                                                                    [ 7 ] 1ºSemestre 2021
                                                                                    [ 8 ] 2ºSemestre 2021
                                                                                    [ 9 ] Range inputável\033[m''')
                esc = str("")

                while esc != ("1", "2", "3", "4", "5", "6", "7", "8"):

                    esc = str(input('Digite a sua escolha(1, 2, 3, 4, 5 ,6, 7, 8, 9): '))

                    if esc == "1":
                        dt2 = input("\033[0;35mDigite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:\033[m")

                        colDT2 = colCD.loc[colCD["date"] == dt2]

                        while colDT2.empty:
                            print("\033[0;31mData não encontrada\n Digite novamente\033[m")
                            dt2 = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")
                            colDT2 = colCD.loc[colCD["date"] == dt2]
                        colDT2 = colDT2.drop("state", axis=1)
                        colDT2 = colDT2.drop("place_type", axis=1)
                        plt.plot(colDT2["date"], colDT2["new_deaths"], label="Óbitos confirmados")
                        plt.plot(colDT2["date"], colDT2["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel(f"{dt2}")
                        xxxx = colDT2.sum()
                        print("Óbitos por Covid no dia:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no dia:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

                    elif esc == "2":
                        dts2 = colCD.loc[colCD["date"] == "2021-11-10"]
                        dts2 = dts2.drop("state", axis=1)
                        dts2 = dts2.drop("place_type", axis=1)
                        plt.plot(dts2["date"], dts2["new_deaths"], label="Óbitos confirmados")
                        plt.plot(dts2["date"], dts2["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("2021-11-10")
                        xxxx = dts2.sum()
                        print("Óbitos por Covid no dia:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no dia:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

                    elif esc == "3":
                        Y = colCD[colCD["date"].between("2020-01-01", "2020-12-31")]
                        Y = Y.drop("state", axis=1)
                        Y = Y.drop("place_type", axis=1)
                        plt.plot(Y["date"], Y["new_deaths"], label="Óbitos confirmados")
                        plt.plot(Y["date"], Y["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("01/01/2020 à 31/12/2020")
                        xxxx = Y.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()

                        break

                    elif esc == "4":
                        y = colCD[colCD["date"].between("2021-01-01", "2021-12-31")]
                        y = y.drop("state", axis=1)
                        y = y.drop("place_type", axis=1)
                        plt.plot(y["date"], y["new_deaths"], label="Óbitos confirmados")
                        plt.plot(y["date"], y["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("2021-01-01 à 2021-12-31")
                        xxxx = y.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

                    elif esc == "5":
                        s = colCD[colCD["date"].between("2020-01-01", "2020-06-30")]
                        s = s.drop("state", axis=1)
                        s = s.drop("place_type", axis=1)
                        plt.plot(s["date"], s["new_deaths"], label="Óbitos confirmados")
                        plt.plot(s["date"], s["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("2020-01-01 à 2020-06-30")
                        xxxx = s.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

                    elif esc == "6":

                        oi = colCD[colCD["date"].between("2020-07-01", "2020-12-31")]
                        oi = oi.drop("state", axis=1)
                        oi = oi.drop("place_type", axis=1)
                        plt.plot(oi["date"], oi["new_deaths"], label="Óbitos confirmados")
                        plt.plot(oi["date"], oi["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("2020-07-01 à 2020-12-31")
                        xxxx = oi.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

                    elif esc == "7":
                        s1 = colCD[colCD["date"].between("2021-01-01", "2021-06-30")]
                        s1 = s1.drop("state", axis=1)
                        s1 = s1.drop("place_type", axis=1)
                        plt.plot(s1["date"], s1["new_deaths"], label="Óbitos confirmados")
                        plt.plot(s1["date"], s1["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("2021-01-01 à 2021-06-30")
                        xxxx = s1.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

                    elif esc == "8":
                        S1 = colCD[colCD["date"].between("2021-07-01", "2021-12-31")]
                        S1 = S1.drop("state", axis=1)
                        S1 = S1.drop("place_type", axis=1)
                        plt.plot(S1["date"], S1["new_deaths"], label="Óbitos confirmados")
                        plt.plot(S1["date"], S1["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel("2021-07-01 à 2021-12-31")
                        xxxx = S1.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break



                    elif esc == "9":

                        XX = input("\033[0;34mData 1 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                        XXX = input("\033[0;34mData 2 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                        S1 = colCD[colCD["date"].between(f"{XX}", f"{XXX}")]

                        while S1.empty:
                            print("\033[0;31mData(s) inválida(s)\nDigite novamente\033[m")

                            XX = input(

                                "\033[0;34mData 1 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                            XXX = input("\033[0;34mData 2 - digite a data nesse formato(yyyy-mm-dd): \033[m")

                            S1 = colCD[colCD["date"].between(f"{XX}", f"{XXX}")]
                        S1 = S1.drop("state", axis=1)
                        S1 = S1.drop("place_type", axis=1)
                        plt.plot(S1["date"], S1["new_deaths"], label="Óbitos confirmados")
                        plt.plot(S1["date"], S1["new_confirmed"], label="Casos confirmados")
                        plt.legend()
                        plt.title('Comparações')
                        plt.xlabel(f"{XX} à {XXX}")
                        xxxx = S1.sum()
                        print("Óbitos por Covid no período:")
                        print(xxxx["new_deaths"])
                        print("Casos de Covid no período:")
                        print(xxxx["new_confirmed"])
                        plt.show()
                        break

            elif F == "x":
                break
    elif x == "x":
        break
