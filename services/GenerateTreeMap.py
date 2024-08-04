import os
import requests
import plotly.express as px
import pandas as pd


class GenerateTreeMap:
    """
    Classe para gerar um treemap a partir de dados de medalhas.
    """

    def __init__(self):
        pass

    def medals(self) -> dict:
        """
        Obtém os dados de medalhas a partir de uma API.

        Returns:
            dict: Dados de medalhas em formato de dicionário.
            None: Se a resposta da API não for bem-sucedida.
        """
        try:
            api_url = os.getenv('API_BASE_URL')
            if not api_url:
                raise ValueError("API_BASE_URL não está definida nas variáveis de ambiente.")
            
            response = requests.get(api_url)
            response.raise_for_status()  # Levanta um erro para códigos de status 4xx/5xx

            data = response.json()
            print(data)
            return data

        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API: {e}")
            return None
        except ValueError as e:
            print(f"Erro de configuração: {e}")
            return None
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return None