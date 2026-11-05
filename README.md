# Sistema de Cadastro de Usuários em Python (JSON)

Este projeto é uma aplicação Back-end desenvolvida em Python com foco em lógica de programação, manipulação de estruturas de dados e persistência de dados utilizando arquivos JSON.

## 🚀 Funcionalidades
- **Persistência de Dados:** Lê, atualiza e guarda os dados de forma automática num arquivo JSON (`armazem_de_usuarios.json`).
- **Cadastro Múltiplo Interativo:** Utiliza laços de repetição (`while True`) para permitir o registo contínuo de vários utilizadores até que o operador decida encerrar.
- **Tratamento de Erros:** Aplica blocos `try/except` para gerir cenários onde o arquivo de base ainda não existe (`FileNotFoundError`).
- **Listagem Dinâmica:** Exibe todos os registos formatados no terminal utilizando `enumerate` e `f-strings`.

## 🛠️ Tecnologias e Ferramentas Utilizadas
- **Python 3**
- **Módulo Nativo `json`**
- **Controlo de Versão:** Git e GitHub
- **Padrão de Código:** Validação com Flake8

## 💻 Como Executar o Projeto
1. Certifique-se de que tem o **Python** instalado no seu computador.
2. Descarregue ou clone os arquivos do projeto para a sua máquina.
3. Abra o terminal na pasta do projeto e execute o comando:
   ```bash
   python sistema_de_cadstro_Json.py