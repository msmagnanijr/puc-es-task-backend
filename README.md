# MVP - Aplicação para Gerenciamento de Tarefas

Este é um projeto Python que usa Flask e sqlite para criar uma API para gerenciar tarefas. A API permite criar, atualizar, remover e listar tarefas. Possui também uma rota de integração com outra API que para consumior informações da em https://newsapi.org. 
Além disso, a API inclui documentação interativa gerada pelo Swagger.

## Pré-requisitos

Para executar este projeto, você precisa ter o Python 3.8 ou superior instalado, além Docker caso seja necessário.

## Como usar

1. Para instalar as dependências, execute o seguinte comando:

```
pip install -r requirements.txt
```

2. Crie as tabelas e Inicie a aplicação:

```
flask db migrate                                                                                                                                                                                                 х INT Py service-c
flask db upgrade
python app.py
```

Agora você pode acessar a documentação da API em http://localhost:5000/apidocs/

É possível também utilizar o Docker já que a aplicação foi dockerizada. Para isso será necessário construir e depois executar:

 docker build -t  task-api .
 docker run -p 5000:5000 task-api `
