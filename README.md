Projeto django
python 3.7 venv pode ser reproduzido com arquivo env.yml usando o conda

Proof-of-concept project for estats.com.br website

# Configuração geral

## Instalando Python
* instalar o [anaconda](https://www.anaconda.com/distribution/) python para seu sistema e **python 3.7**
  Ao instalar **não** escolher para instalar no PATH ou criar varíavel de ambiente.

* Abrir o *Anaconda Prompt* e criar um ambiente virtual, idealmente a partir do arquivo .yml distribuído aqui. Para tal,
  procurar o diretório que clonou o objeto e dar `cd C:/caminho/para/diretorio/do/projeto/estats` depois `conda env create -f  env.yml`. Um ambiente virtual com as dependências do projeto django deve ser criado com o nome **webDev**

* **Sempre** que for mexer no projeto django, deve-se ativar o ambiente primeiro, ou seja,
    1. Abrir o *Anaconda Prompt*
    2. Entrar no diretório do projeto django *estats*
    3. Ativar o ambiente *webDev* com `activate webdev` (Windows) ou `source activate webdev` (OSX/Linux)
  
  
# Rodar servidor de testes

Usar comando `python manage.py runserver`. No browser entrar em localhost:8000/estats.com (home) ou localhost:8000/admin para página do administrador (precisa ter usuário admin cadastrado, entrar em contato colonese para receber um).

# Em desenvolvimento

## App - Cartola
App para gerenciamento e manuseio de dados referentes ao CartolaFC
### Modelos e BD
- [x] Configuração banco de dados PostGRE
- [x] Modelos para Banco de dados de estatísticas e Dados relativos ao Cartola
- [x] Carregamento inicial de dados de Jogadores
- [x] Carregamento inicial de dados de Clubes
- [ ] Carregamento inicial de relações entre Clubes e Jogadores (Contrato)
- [x] Carregamento inicial de dados de Partidas do BR18 
- [ ] Carregamento inicial de Scouts com relações com Clube, Jogadores e Partidas
### Views
- [ ] Páginas de perfil de Jogador, Clube e Partidas usando Django.GenericViews
- [ ] Usar django-tables2 para criar view tabela de scouts com bootstrap
### Templates
- [ ] Outros templates

## App - Sócio
App para gerenciamento de usuários, cadastro e restrições de acesso a conteúdo
### Modelos
- [ ] Usar django.auth para criar modelos de usuários para cadastro e futuro plano pago
### Views
- [ ] Criar view para Formulário de Cadstro e acesso 
### Templates
- [ ] Formulário de cadastro
- [ ] Página Perfil

## App - Blog
App para gerenciamento de postagens tipo blog
### Modelos
- [ ] Criar modelos típicos de um Blog: Artigo, Autor, etc
### Views
- [ ] Criar Views típicas: ultiamas postagens, filtragem por data/tag/assunto/autor
- [ ] View própria de uma Postagem, imagem + texto
### Templates
- [ ] Templates associados
