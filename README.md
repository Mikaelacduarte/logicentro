# logicentro
# Projeto de Logística

Este projeto é um sistema de gerenciamento de logística desenvolvido em Django. Ele permite o cadastro e a gestão de veículos, motoristas, empresas e usuários, facilitando o controle e a operação logística.

## Funcionalidades

- **Cadastro de Usuários**: Permite criar e gerenciar usuários do sistema.
- **Cadastro de Veículos**: Registro e gerenciamento de veículos disponíveis para transporte.
- **Cadastro de Motoristas**: Gerenciamento de motoristas e suas informações.
- **Cadastro de Empresas**: Registro de empresas envolvidas nas operações logísticas.
- **Autenticação de Usuários**: Implementação de autenticação e geração de tokens para acesso seguro.

## Tecnologias Utilizadas

- Django
- Django REST Framework
- SQLite (ou outro banco de dados, se aplicável)

## Estrutura do Projeto

- **models.py**: Define os modelos de dados (Usuário, Veículo, Motorista, Empresa).
- **serializers.py**: Serializadores que transformam os dados dos modelos em formatos JSON e vice-versa.
- **views.py**: Define as visões que controlam a lógica do aplicativo e interagem com as requisições HTTP.
- **urls.py**: Configura as rotas da API para acesso aos recursos do aplicativo.


