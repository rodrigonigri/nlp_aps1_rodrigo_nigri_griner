# NLP APS1 Rodrigo Nigri Griner
## Author
Rodrigo Nigri Griner

## About the Project

This project is part of the Natural Language Processing course at Insper. The goal of this project is to make an API that receives a string and returns the most similar documents in the dataset. The similarity is calculated using TF-IDF.

## How to Run

### Local

To run the project locally, you need to have Python 3.8 installed. Then, you can install the dependencies with the following command:

```bash
pip install -r requirements.txt
```

After that, you can run the project with the following command:

```bash
python app/main.py
```

The API will be available at `http://localhost:1530/query?query="word search"`, where you can replace `"word search"` with the word you want to search.

### Docker

This project can also be run with Docker. To do that, you can run the following commands:

```bash
docker build -t image_name .
docker run -d -p 1530:1530 image_name
```

## Dataset

The dataset used in this project was scraped from the [Letras.mus.br](https://www.letras.mus.br/) website. 

## Tests:

### Test 1: Query yields 10 results
Este teste verifica se a API retorna 10 resultados quando a consulta é uma frase presente no conjunto de dados.

[http://10.103.0.28:1530/query?query=same%20bed%20but%20it%20feels%20just%20a%20little%20bit%20bigger%20now](http://10.103.0.28:1530/query?query=same%20bed%20but%20it%20feels%20just%20a%20little%20bit%20bigger%20now)

### Test 2: Query yields few results
Este teste verifica se a API retorna mais de 1 e menos de 10 resultados.

[http://10.103.0.28:1530/query?query=hello](http://10.103.0.28:1530/query?query=hello)

### Test 3: Query yields non-obvious results
Este teste verifica se a API retorna resultados com relevância maior que 0.9 quando a consulta é uma frase presente no conjunto de dados.

[http://10.103.0.28:1530/query?query=die%20with%20a%20smile](http://10.103.0.28:1530/query?query=die%20with%20a%20smile)
