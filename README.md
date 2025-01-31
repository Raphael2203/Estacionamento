Gerenciamento de Estacionamento com Flask 🚗

Descrição do Projeto

Este projeto é um sistema de gerenciamento de estacionamento desenvolvido utilizando Flask, Python, SQLite e outras tecnologias. Ele permite registrar a entrada e saída de veículos, calcular automaticamente o tempo de permanência e o valor a ser cobrado, listar os veículos presentes no estacionamento, e muito mais.

Funcionalidades Principais

Registro de Entrada e Saída de Veículos: Permite registrar a entrada e saída de veículos no estacionamento.

Listagem de Veículos Presentes: Exibe todos os veículos que estão atualmente dentro do estacionamento.

Interface Amigável: Interface simples e intuitiva para facilitar o uso.

Fuso Horário: Implementação de fuso horário para garantir a precisão dos registros de horários.

Tecnologias Utilizadas

Flask: Framework web em Python para construir aplicações rápidas e escaláveis.

SQLite: Banco de dados leve e eficiente.

HTML/CSS/JavaScript: Para criar uma interface de usuário atraente e responsiva.

pytz: Biblioteca para gerenciamento de fusos horários.

Como Executar o Projeto

Pré-requisitos

Python 3.6 ou superior
Git
Flask e outras dependências listadas no arquivo requirements.txt

Passos para Execução

Clone o repositório:

git clone https://github.com/Raphael2203/Estacionamento.git

Navegue até o diretório do projeto:
cd Estacionamento

Crie um ambiente virtual:
python -m venv venv

Ative o ambiente virtual:

No Windows:
venv\Scripts\activate

No macOS/Linux:
source venv/bin/activate

Instale as dependências:
pip install -r requirements.txt

Execute a aplicação:
python app.py

Acesse a aplicação no navegador:
Acesse http://localhost:5000 para visualizar a interface do sistema de gerenciamento de estacionamento.

Endpoints da API
POST /entrar: Registra a entrada de um veículo.

Parâmetros: placa (string)

POST /sair: Registra a saída de um veículo e calcula o tempo de permanência e o valor.

Parâmetros: placa (string)

GET /vagas: Exibe o número de vagas disponíveis.

GET /listar: Lista todos os veículos presentes no estacionamento.

Contribuição
Sinta-se à vontade para contribuir com o projeto. Para isso:

1.Faça um fork do repositório.

2.Crie uma branch para sua feature ou correção: git checkout -b minha-feature

3.Commit suas mudanças: git commit -m 'Adicionar nova feature'

4.Envie para o repositório remoto: git push origin minha-feature

5.Abra um pull request.
