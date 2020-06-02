import pandas as pd

def readCSV(filename, dataNotificacao):
    
    dados = pd.read_csv(filename, sep=',', names=['sexo', 'idade', 'cidade', 'data'], header=0)
    dados['dataNotificacao'] = dataNotificacao
    dados = dados[['data', 'idade', 'sexo', 'cidade', 'dataNotificacao']]
    dados.idade = dados.idade.fillna('NA')
    dados.idade = list(map(lambda x: '{:,.0f}'.format(x) if x != 'NA' else x, dados.idade))
    dados.sexo = list(map(lambda x: 'F' if x == 'Mulher' else 'M', dados.sexo))
    
    return dados

if __name__ == "__main__":
    import sys
    from datetime import datetime
    
    filename = sys.argv[1]
    dataNotificacao = datetime.now().strftime("%Y-%m-%d")
    boletim = readCSV(filename, dataNotificacao)
    
    for caso in boletim.iterrows():
        valor = caso[1]
        idade = valor.idade
        col = valor.data.split("T")
        print(f"{col[0]},{idade},{valor.sexo},{valor.cidade}")
