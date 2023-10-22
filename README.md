# **API em Python para testar CRUD com Postman** 🖥️⚙️

API para estudo do Python e Postman baseada na aula do Canal Dev Aprender | Jhonatan de Souza: https://youtu.be/FBLAV1SbJFk

## Requisitos:
- Python 3.11
- Flask 3.0.0
- Postman (para testar métodos CRUD)

## Como usar (no Windows):
- Após clonar este repositório, no Terminal navegue até a pasta raiz do projeto e instale o Flask no seu ambiente Python com comando:

```
python -m pip -r requirements.txt
```
- Em seguida, ainda no Terminal e na pasta raiz rode o programa (app.py) com comando:

```
py .\app.py 
```
- Com isto, API já estará acessível do endereço base http://localhost:3000 , bastando apenas complementar este endereço com o endpoint que for utilizar para cada método HTTP:

| Endpoint | Métodos disponíveis |
|-----:|---------------|
|/livros|GET, POST|
|/livros/id|GET, PUT, DELETE|
|/livros/consultar_livro_por_id_json|GET|
|/livros/editar_livro_por_id_json|PUT|
|/livros/excluir_livro_por_id_json|DELETE|

- Esta API poderá ser testada em qualquer navegador, mas recomedo usar o [Postman](https://www.postman.com/), onde na request, além do método e endpoint, pode-se também colocar no body o JSON (opções RAW e JSON) no seguinte formato:

```json
{
    "id": 3,
    "titulo": "A Arte Cavalheiresca do Arqueiro Zen",
    "autor": "Eugen Herrigel"
}
```

Ficarei muito feliz se o que estiver aqui for útil para você e ainda mais feliz se puder me ajudar contribuindo com melhorias neste projeto. 😊