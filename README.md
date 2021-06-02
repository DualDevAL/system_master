'''
SYSTEM_MASTER:

.Primeiramente precisa ter o docker e o postgreSQL instalado na máquina.
.No diretório do projeto execute pelo terminal:

docker-compose up 

.Ele vai instalar todas as bibliotecas necessárias e criará um container.
.Após a instalação e execução da aplicação, interrompa o servidor local com o comando ctrl + c. 
.Agora execute a aplicação em segundo plano com o seguinte comando:

docker-compose up -d

.Com a aplicação rodando em segundo plano execute o comando seguinte para subir as informações e vincular ao banco de dados: 

docker-compose exec web python manage.py migrate

.Uma vez concluido a etapa acima, execute: 

docker-compose exec web python manage.py makemigrations

.E depois novamente: 

docker-compose exec web python manage.py migrate

.Enfim pode ir ao navegador e executar a aplicação no navegador atraves da url localhost:8000

.obs: Para interromper a aplicação em segundo plano, verifique o ID do container com o comando: 

docker ps 

.Uma vez tendo o ID do container, execute: 

docker stop id_do_container

.Para acessar o admin, crie um super usuário com o seguinte comando: 

docker-compose exec web python manage.py createsuperuser


