from fastapi import FastAPI, Query
import os
import uvicorn
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def print_colored(text, color):
    """Print text in color"""
    if color == "red":
        print("\033[91m {}\033[00m" .format(text))
    elif color == "green":
        print("\033[92m {}\033[00m" .format(text))
    elif color == "yellow":
        print("\033[93m {}\033[00m" .format(text))
    elif color == "blue":
        print("\033[94m {}\033[00m" .format(text))
    elif color == "magenta":
        print("\033[95m {}\033[00m" .format(text))
    elif color == "cyan":
        print("\033[96m {}\033[00m" .format(text))
    elif color == "white":
        print("\033[97m {}\033[00m" .format(text))
    elif color == "black":
        print("\033[98m {}\033[00m" .format(text))
    else:
        print("\033[99m {}\033[00m" .format(text))


class DummyModel:
    def predict(self, X):
        return "dummy prediction"

def load_model():
    predictor = DummyModel()
    return predictor

app = FastAPI()
app.predictor = load_model()

# http://10.103.0.19:8888/query?query=myquery

@app.get("/")
def read_hello():
    return {"message": "hello world"}

@app.get("/query")
def query_route(query: str = Query(..., description="Search query")):
    # pegar musicas.csv e transformar em um DataFrame:
    route = "../data/musicas.csv"
    df = pd.read_csv(route, delimiter='|')
    
    # criar um vetorizador TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['Letra'])
    
    # transformar a query em um vetor
    target_music_lyric = query
    Q = vectorizer.transform([target_music_lyric])
    
    # R = X * transpose(Q)
    R = np.dot(X, Q.T).toarray()
    
    # Adicionando a coluna Relevance ao DataFrame
    df['Relevance'] = R
    sorted_df = df.sort_values(by='Relevance', ascending=False)
    
    # filter sorted_df to get only Relevance is > 0.1 and return a maximum of 10 songs
    sorted_df = sorted_df[sorted_df['Relevance'] > 0.1]
    top_10_songs = sorted_df.head(10)
    
    retorno = []
    for i in range(len(top_10_songs)):
        retorno.append({
            'title': top_10_songs.iloc[i]['Titulo-Artista'], 
            'content': top_10_songs.iloc[i]['Letra'], 
            'relevance': top_10_songs.iloc[i]['Relevance']
        })
    
    return {"results": retorno, "message": "OK"}

def run():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    run()