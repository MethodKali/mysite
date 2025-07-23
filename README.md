# ProjectDjango
Django Personal Blog

## Criando um ambiente virtual python

Para criarmos um ambiente virtual para o python utilizaremos o seguinte comando:

	python3 -m venv env

## Crie uma branch nova para controle do progresso sa aplicação Django

Para criarmos uma branch nova utilizaremos o seguinte comando:

	git checkout -b "NomeBranch"

## Instale o Django

Para a instalação do Django usaremos o seguinte comando:
	
	pip install Django

## Crie um novo projeto em Django

Para criarmos um projeto Django usaremos o seguinte comando:

	django-admin startproject "nomeProjetoGit"

## Crie a aplicação python

Para criarmos um app python usaremos o seguinte comando:

	python3 manage.py startapp "nomeApp"

## Principais arquivos estruturais Django

_init_.py => Indica ao interpretador Python que o diretório é um pacote python

_senttings.py_ => Contém as definições de configuração para projeto Django

_urls.py_ => Contém padrões de URL para projeto Django

_wsgi.py_ => Contém propriedades de configuração WSGI para o projeto python. Basicamente é usado para ajudar a executar seu servidor dedesenvolvimento e implantar seu projeto em um ambiente de produção

_manage.py_ => Utilitário que permite comque você interaja com o seu projeto Django de várias maneiras. Script responsável por todas as tarefas especificas do projeto

 
## Adicione sua aplicação no script de configuração

Para adicionar sua aplicação no script de configuração seguimos o passo a passo:

* Abra o script settings.py em uma IDE
* Na variavel lista _INSTALLED-APPS_ adicione o nome da sua aplicação seguindo o formato dos já inclusos
* Salve o script

## Faça a migração dos modelos pré existentes do Django

Para fazermos as migrações utilizamos o seguinte comando no Terminal:

	python3 manage.py migrate

## Suba a aplicação Django para o servidor WEB

Para subir uma aplicação Django usamos o seguinte comando:

	python3 manage.py runserver