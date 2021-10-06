import requests
import json

class api_inmet:
    """Classe para consumo da api do INMET
    """

    def __init__(self) -> None:
        pass

    def requisita_estacoes(self, tipo:str ='T') -> json:
        """Requisita todas as estações disponíveis por tipo

        Args:
            tipo (str, optional): Tipo de estação procurada. Aceita "T" ou "M". Por padrão é 'T'.

        Returns:
            json: Todas as estações disponíveis e atributos.
        """
        url_base = 'https://apitempo.inmet.gov.br/estacoes/'
        url = f"{url_base}/{tipo}"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            resp = resposta.content
            return resp
        else:
            return 'ERRO! A requisição encontrou um problema.'


    def requisita_diario(self, data_inicial:str, data_final:str, cod_estacao:str) -> json:
        """Requisita os dados de 1 estação em um intervalo de tempo definido.

        Args:
            data_inicial (str): [Padrão AAAA-MM-DD] Data inicial dos dados procurados. 
            data_final (str): [Padrão AAAA-MM-DD] Data final dos dados procurados.
            cod_estacao (str): Código da estação da ANA procurada.

        Returns:
            json: Estação com seus atributos
        """
        url_base = 'https://apitempo.inmet.gov.br/estacao/diaria'
        url = f'{url_base}/{data_inicial}/{data_final}/{cod_estacao}'

        resposta = requests.get(url)

        if resposta.status_code == 200:
            resp = resposta.content
            return resp
        else:
            return 'ERRO! A requisição encontrou um problema.'
        