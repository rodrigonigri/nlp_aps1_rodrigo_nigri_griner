from fastapi import FastAPI, Query
import uvicorn
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import os

app = FastAPI()

# http://10.103.0.19:8888/query?query=myquery

@app.get("/")
def read_hello():
    return {"message": "hello world"}

@app.get("/query")
def query_route(query: str = Query(..., description="Search query")):

    # pegar musicas.csv e transformar em um DataFrame:
    current_dir = os.path.dirname(__file__)
    route = os.path.join(current_dir, "../data/musicas.csv")

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
    uvicorn.run("main:app", host="0.0.0.0", port=1530, reload=True)

if __name__ == "__main__":
    run()