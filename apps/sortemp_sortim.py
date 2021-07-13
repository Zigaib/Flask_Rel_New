import pandas as pd


import timeit
pd.set_option('mode.chained_assignment', None)

def main():
        print('ok')


def sortim(df):

        new_cols = ['PERFIL','BANDEIRA','LOCAL_NOVO','LOCAL','TAMANHO','REGIÃO','REGIAO 2','CONCATENADO','CONCATENADO 2','CONCATENADO 3','CONCATENADO 4','CONCATENADO 5']
        for i in new_cols:
                df[i] = ''

        print('computado!')
        for i in range(len(df)):
                if 'RUA' in df["DESCTAMANHO"][i]:
                        df['LOCAL_NOVO'][i] = "CONVENCIONAL"
                        df['LOCAL'][i] = "RUA"
                elif 'SHOPPING' in df["DESCTAMANHO"][i]:
                        df['LOCAL_NOVO'][i] = "CONVENCIONAL"
                        df['LOCAL'][i] = "SHOPPING"
                elif 'QUIOSQUE' in df["DESCTAMANHO"][i]:
                        df['LOCAL_NOVO'][i] = "QUISOQUE"
                        df['LOCAL'][i] = "QUISOQUE"
                else:
                        df['LOCAL_NOVO'][i] = "COMPACTA"
                        df['LOCAL'][i] = "COMPACTA"

                if '-CB-' in df["DESCTAMANHO"][i]:
                        df['BANDEIRA'][i] = "CB"
                else:
                        df['BANDEIRA'][i] = "PF"

                if '-CB-' in df["DESCTAMANHO"][i]:
                        df['BANDEIRA'][i] = "CB"
                else:
                        df['BANDEIRA'][i] = "PF"

                if '-PERFIL 1-' in df["DESCTAMANHO"][i]:
                        df['PERFIL'][i] = "PERFIL 1"
                elif '-PERFIL 2-' in df["DESCTAMANHO"][i]:
                        df['PERFIL'][i] = "PERFIL 2"
                elif '-PERFIL 3-' in df["DESCTAMANHO"][i]:
                        df['PERFIL'][i] = "PERFIL 3"
                elif '-PERFIL 4-' in df["DESCTAMANHO"][i]:
                        df['PERFIL'][i] = "PERFIL 4"
                else:
                        df['PERFIL'][i] = "PERFIL 5"

                if '-PP-' in df["DESCTAMANHO"][i]:
                        df['TAMANHO'][i] = "PP"
                elif '-P-' in df["DESCTAMANHO"][i]:
                        df['TAMANHO'][i] = "P"
                elif '-M-' in df["DESCTAMANHO"][i]:
                        df['TAMANHO'][i] = "M"
                elif '-G-' in df["DESCTAMANHO"][i]:
                        df['TAMANHO'][i] = "G"
                elif '-GG-' in df["DESCTAMANHO"][i]:
                        df['TAMANHO'][i] = "GG"
                else:
                        df['TAMANHO'][i] = "MEGA"

                if '-RJ/ES' in df["DESCTAMANHO"][i]:
                        df['REGIÃO'][i] = "RJ/ES"
                        df['REGIAO 2'][i] = "RJ/ES"
                elif '-SPI' in df["DESCTAMANHO"][i]:
                        df['REGIÃO'][i] = "SPI"
                        df['REGIAO 2'][i] = "SPI"
                elif '-MG' in df["DESCTAMANHO"][i]:
                        df['REGIÃO'][i] = "MG"
                        df['REGIAO 2'][i] = "MG"
                elif '-SUL' in df["DESCTAMANHO"][i]:
                        df['REGIÃO'][i] = "SUL"
                        df['REGIAO 2'][i] = "SUL"
                elif '-GDE SP' in df["DESCTAMANHO"][i]:
                        df['REGIÃO'][i] = "GDE SP"
                        df['REGIAO 2'][i] = "GDE SP"
                elif '-CO/N' in df["DESCTAMANHO"][i]:
                        df['REGIÃO'][i] = "CO/N"
                        df['REGIAO 2'][i] = "CON/N"
                else:
                        df['REGIÃO'][i] = "NE"
                        df['REGIAO 2'][i] = "NE"
                df['CONCATENADO'][i] = f"{df['LOCAL_NOVO'][i]}-{df['PERFIL'][i]}-{df['TAMANHO'][i]}"
                df['CONCATENADO 2'][i] = f"{df['LOCAL_NOVO'][i]}-{df['PERFIL'][i]}-{df['REGIÃO'][i]}-{df['TAMANHO'][i]}"

                df['CONCATENADO 3'] = df['LOCAL_NOVO'].map(str) + '-' + df['PERFIL'].map(str) + '-' + df['REGIÃO'].map(
                        str)
                df['CONCATENADO 4'] = df['LOCAL'].map(str) + '-' + df['TAMANHO'].map(str)
                df['CONCATENADO 5'] = df['LOCAL_NOVO'].map(str) + '-' + df['PERFIL'].map(str) + '-' + df['BANDEIRA'].map(
                        str) + '-' + df['TAMANHO']
                df['CONCATENADO 6'] = df['PERFIL'].map(str) + '-' + df['BANDEIRA'].map(str) + '-' + df['LOCAL'].map(
                        str) + '-' + df['REGIÃO']

        colorder=['CODPUBLICO','DESCPUBLICO','CODSECAO','DESCSECAO','CODSORTIMENTO','CODTAMANHO','DESCTAMANHO','PERFIL','BANDEIRA','LOCAL_NOVO','LOCAL','TAMANHO','REGIÃO','REGIAO 2','CONCATENADO','CONCATENADO 2','CONCATENADO 3','CONCATENADO 4','CONCATENADO 5','CONCATENADO 6','EMPRESA','FILIAL','TIPOPUBLICO','SOLICVOLTDIF']
        df = df[colorder]

        return df



def sortemp(df):
        new_cols = ['PERFIL', 'BANDEIRA', 'LOCAL_NOVO', 'LOCAL', 'TAMANHO', 'REGIÃO', 'REGIAO 2', 'CONCATENADO',
                    'CONCATENADO 2']
        start = timeit.default_timer()
        for i in new_cols:
                df[i] = ' '

        df = df.reindex()

        print('novas colunas')

        df['LOCAL_NOVO'] = df['DESCTAMANHO'].apply(lambda x: 'CONVENCIONAL' if 'RUA' in x else x)
        df['LOCAL_NOVO'] = df['LOCAL_NOVO'].apply(lambda x: 'CONVENCIONAL' if 'SHOPPING' in x else x)
        df['LOCAL_NOVO'] = df['LOCAL_NOVO'].apply(lambda x: 'QUIOSQUE' if 'QUIOSQUE' in x else x)
        df['LOCAL_NOVO'] = df['LOCAL_NOVO'].apply(lambda x: 'COMPACTA' if 'COMPACTA' in x else x)
        df['LOCAL_NOVO'] = df['LOCAL_NOVO'].apply(lambda x: 'DIGITAL' if 'DIGITAL' in x else x)

        df['LOCAL'] = df['DESCTAMANHO'].apply(lambda x: 'RUA' if 'RUA' in x else x)
        df['LOCAL'] = df['LOCAL'].apply(lambda x: 'SHOPPING' if 'SHOPPING' in x else x)
        df['LOCAL'] = df['LOCAL'].apply(lambda x: 'QUIOSQUE' if 'QUIOSQUE' in x else x)
        df['LOCAL'] = df['LOCAL'].apply(lambda x: 'COMPACTA' if 'COMPACTA' in x else x)
        df['LOCAL'] = df['LOCAL'].apply(lambda x: 'DIGITAL' if 'DIGITAL' in x else x)

        df['BANDEIRA'] = df['DESCTAMANHO'].apply(lambda x: 'CB' if '-CB-' in x else x)
        df['BANDEIRA'] = df['BANDEIRA'].apply(lambda x: 'PF' if '-PF-' in x else x)

        df['PERFIL'] = df['DESCTAMANHO'].apply(lambda x: 'PERFIL 1' if '-PERFIL 1-' in x else x)
        df['PERFIL'] = df['PERFIL'].apply(lambda x: 'PERFIL 2' if '-PERFIL 2-' in x else x)
        df['PERFIL'] = df['PERFIL'].apply(lambda x: 'PERFIL 3' if '-PERFIL 3-' in x else x)
        df['PERFIL'] = df['PERFIL'].apply(lambda x: 'PERFIL 4' if '-PERFIL 4-' in x else x)
        df['PERFIL'] = df['PERFIL'].apply(lambda x: 'PERFIL 5' if '-PERFIL 5-' in x else x)

        df['TAMANHO'] = df['DESCTAMANHO'].apply(lambda x: 'PP' if '-PP-' in x else x)
        df['TAMANHO'] = df['TAMANHO'].apply(lambda x: 'P' if '-P-' in x else x)
        df['TAMANHO'] = df['TAMANHO'].apply(lambda x: 'M' if '-M-' in x else x)
        df['TAMANHO'] = df['TAMANHO'].apply(lambda x: 'G' if '-G-' in x else x)
        df['TAMANHO'] = df['TAMANHO'].apply(lambda x: 'GG' if '-GG-' in x else x)
        df['TAMANHO'] = df['TAMANHO'].apply(lambda x: 'MEGA' if '-MEGA-' in x else x)

        df['REGIÃO'] = df['DESCTAMANHO'].apply(lambda x: 'RJ/ES' if '-RJ/ES' in x else x)
        df['REGIÃO'] = df['REGIÃO'].apply(lambda x: 'SPI' if '-SPI' in x else x)
        df['REGIÃO'] = df['REGIÃO'].apply(lambda x: 'MG' if '-MG' in x else x)
        df['REGIÃO'] = df['REGIÃO'].apply(lambda x: 'SUL' if '-SUL' in x else x)
        df['REGIÃO'] = df['REGIÃO'].apply(lambda x: 'GDE SP' if '-GDE SP' in x else x)
        df['REGIÃO'] = df['REGIÃO'].apply(lambda x: 'CO/N' if '-CO/N' in x else x)
        df['REGIÃO'] = df['REGIÃO'].apply(lambda x: 'NE' if '-NE' in x else x)

        df['REGIAO 2'] = df['DESCTAMANHO'].apply(lambda x: 'RJ/ES' if '-RJ/ES' in x else x)
        df['REGIAO 2'] = df['REGIAO 2'].apply(lambda x: 'SPI' if '-SPI' in x else x)
        df['REGIAO 2'] = df['REGIAO 2'].apply(lambda x: 'MG' if '-MG' in x else x)
        df['REGIAO 2'] = df['REGIAO 2'].apply(lambda x: 'SUL' if '-SUL' in x else x)
        df['REGIAO 2'] = df['REGIAO 2'].apply(lambda x: 'GDE SP' if '-GDE SP' in x else x)
        df['REGIAO 2'] = df['REGIAO 2'].apply(lambda x: 'CO/N' if '-CO/N' in x else x)
        df['REGIAO 2'] = df['REGIAO 2'].apply(lambda x: 'NE' if '-NE' in x else x)

        df['CONCATENADO'] = df['LOCAL_NOVO'].map(str) + '-' + df['PERFIL'].map(str) + '-' + df['TAMANHO']
        df['CONCATENADO 2'] = df['LOCAL_NOVO'].map(str) + '-' + df['PERFIL'].map(str) + '-' + df['REGIÃO'].map(
                str) + '-' + df['TAMANHO']

        colorder = ['CODSORTIMENTO', 'CODSECAO', 'DESCSECAO', 'CODTAMANHO', 'DESCTAMANHO', 'CODPUBLICO',
                    'DESCPUBLICO',
                    'CODMERCADORIA', 'DESCMERCADORIA', 'MERCCONJ', 'PRIORIDADE', 'QTDE', 'VOLTAGEM',
                    'VIGENCIAINICIO',
                    'VIGENCIAFIM', 'PERFIL', 'BANDEIRA', 'LOCAL', 'LOCAL_NOVO', 'TAMANHO', 'REGIÃO', 'STATUS',
                    'DESCMARCA', 'DESCESPECIE', 'CONCATENADO', 'CONCATENADO 2']
        df = df[colorder]

        return df
