# get folder
1. git clone "app"
2. git branch -a 
3. git checkout "dev"
4. cd apioculto....

# exec db
5. docker-compose up -d
6. testar db dbeaver

# env
7. No Linux e MacOS
python3 -m venv .venv
source .venv/bin/activate
8. No Windows:
python -m venv .venv
.\.venv\Scripts\activate
9. pip install -r requirements_dev.txt
 
# Exec
10. run main.py
11. Testar no /localhost:8003/docs

# Criar api (ms) de usuário
12. Criar repositorio, schema, model e rota
13. Subir no git com gitigone
14. Criar dockerfile⌢愠楰浟彳敤≶ഠ

# Configuração do banco de dados
15. Para configurar o acesso ao banco, insira as credenciais do banco de dados em
app/db/.env.

* POSTGRES_USER=example
* POSTGRES_PASSWORD=example
* POSTGRES_SERVER=localhost
* POSTGRES_PORT=5432
* POSTGRES_DB=postgres

16. Os prints dos testes estão no diretório assets para a correção
