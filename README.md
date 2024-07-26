## Configurações do alembic para microserviço de contracts

O arquivo de configuração está localizado em 'alembic.ini'. Este arquivo define as configurações e o caminho para script de migração.

- 'scrip_location' : Diretorio onde os scripts de migração estão localizados
- 'sqlalchemy.url': URL de conexão com o banco de dados (esta configurado dinamicamente no arquivo 'arc-microservice-contract/env.py')

O arquivo env.py no diretorio de script de migração esta configrado para se conectar ao banco de dados e aplicar as migrações corretamente, ele carrega as configurações do 'alembic.ini'.


## Executando uma migração

Para aplicar as migrações e atualizar o banco de dados para ultima versão, use o comando:

```poetry run alembic upgrade head```

Para Gerar novas migrações após alterar os modelos, use o comando:

```poetry run alembic revision --autogenerate -m "Descrição com detalhes"```

Atenção para arquivo que foi gerado no diretorio alembic/version importante revisar!

Desfazendo migrações:

```poetry run downgrade <versão>```

Verificando o status das migrações:

```poetry run alembic current```


# Nota

A primeira versão de migração já foi gerada e esta incluida no repositorio, certifique-se de revisar o histórico de migrações para entender o estado atual do banco de dados.


# Contribuições

Sinta-se à vontade para contribuir com novas intruções nesse arquivo, que se adeque ao fluxo de trabalho.