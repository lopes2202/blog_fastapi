# O que é desenvolvimento web?
é o processo de criação de websites e aplicações para internet ou uma intranet, abrange uma variedade de tarefas, incluindo web design, programação web, gestão de banco de dados e engenharia de servidores
intranet (rede privada)

# Componentes Principais
Frontend: é onde os usuários interagem direteamente, envolve a criação de interfaces de usuário e exp

Backend: "bastidor de um website", onde ocorre o processamento de dados, gerenciamento de banco de dados e controle de servidor

# Internet vs. Web
Internet -> rede global de computadores inteconectados 
A Web ou World Wide Web, é um sistema de informação construído sobre a internet que utiliza o protocolo HTTP para transmitir dados

FTP -> protocolo que faz transferencia de arquivos
Telnet -> protocolo que gerencia maquinas remotamente

# Protocolo HTTP
protocolo fundamental usado na web para transferencia de dados, 

usuário acessa o site -> navegador envia solicitação para servidor -> servidor responde com os dados do site -> devolvendo para o cliente

# Guia de como um funcionamento de um website
1 - Solicitação do Usuário -> insere um url no navegador ou clicando num link
2 - Resolução de DNS -> URL é traduzido para um IP através do DNS
3 - Conexão do servidor -> navegador utiliza endereço IP para estabelecer uma conexão com o servidor que hospeda o site
4 - Resposta do servidor: servidor processa a solicitação HTTP e envia de volta os arquivos geralmente em HTML, CSS e JS
5 - Renderização no navegador -> navegador interpreta esses arquivos e exibe o site aos usuários 

# Tecnologias envolvidas 
HTML, CSS e JavaScript
SSL/TLS -> direcionadas a segurança
APIs para interatividade e banco de dados para armazenamento de dados

# Frontend: interface do usário 
é a parte do desenvolvimento web que lida com a interface do usuário
Objetivo: apresentar informações de forma interativa e acessível para o user

# Backend: lógica por trás dos bastidores
é a parte do site que o user não ve, inclui servidor, aplicação e banco de dados
Objetivo: responsável por gerenciar e processar os dados

# Dev FullStack
são profissionais que tem habilidade tanto em front-end e back-end

# API 
conjunto de regras e definições que permite que diferentes aplicações de software ou componentes se comuniquem entre si

frontend(cliente) -> interage com a API -> que faz uma requisição pro backend -> backend processa os dados e envia de volta para o cliente

# APIs no contexto da Web
APIs são usadas para permitir a interação entre diferentes serviços e aplicações

# Importancia das APIs
cruciais para a construção de aplicações modernas e escaláveis, permite flexibilidade para integrar e expandir funcionalidades sem reinventar a moda  

# Tipos de API

## Api RESTful: 
seguem os principios do REST, são baseadas em padrões http e utilizadas para interações web

## Caracteristicas de API RESTful:
Uso dos métodos HTTP(GET, POST, PUT, DELETE) para operações CRUD
curva de aprendizado menor, facil de entender e implementar

## API SOAP
SOAP é um protocolo que define um opadrão para a troca de mensagens baseadas  em XML

## Caracteristicas de API SOAP:
Protocolo baseado em XML 
Independente de linguagem e plataforma de transporte
Suporte para operações complexas e segurança avançada

## API GraphQL
Uma linguagem de consulta para sua API, e um servidor capaz de executar essas consultas, retornando apenas os dados especificados 

## Características de APIs GraphQL
Permite que os clientes especifiquem exatamente quais dados querem
eficiente na redução de solicitações e no tamanho dos dados transferidos
flexível e fortmente tipada, facilitando a evolução de APIs

# Qual tipo de API é o certo?
Depende dos requisitos especificos do projeto, dos recursos dispponiveis e da expertise da equipe

RESTful -> simplicidade
SOAP -> preferido para segurança e transações complexas
GraphQL -> ideal para aplicações que requerem dados dinamicos personalizados 

# Verbos HTTP: GET, POST, PATCH, PUT, DELETE
Get: lista os dados (leitura das requisições)
Post: criação de dados
Put: atualização dos dados
Patch: atualização dos dados parcialmente 
Delete: Remoção



