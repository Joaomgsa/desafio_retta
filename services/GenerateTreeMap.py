import os
import requests
import plotly.express as px
import pandas as pd


class GenerateTreeMap():

    def __init__(self):
        pass
    
    def medals() -> dict:
        try:
            api_url = os.getenv('API_BASE_URL')
            response = requests.get(api_url)
            
            if response.status_code == 200:
                data = response.json()
            if response.status_code >= 300:
                return None
            
            return data
        
        except Exception as e:
            return str(e)
    
    def handle(self):
        
        medals = GenerateTreeMap.medals()
                
        if medals is None:
            return "Erro ao acessar a API"
        
        df = pd.DataFrame(medals['data'])
        
        
        
        fig = px.treemap(df, 
                         path=['id', 'total_medals'],
                         values='total_medals',
                         color='total_medals',
                         color_continuous_scale='RdBu',
                         hover_data=['gold_medals','silver_medals','bronze_medals'],
                         title='Quadro de Medalhas - Paris 2024')
        fig.update_layout(margin=dict(t=50, l=25, r=25), title_x=0.5)

        treemap = fig.to_html(full_html=False)
        return treemap
