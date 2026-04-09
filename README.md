# deploy_streamlite_fifa2023
# ⚽ Dashboard FIFA 23

Um aplicativo web interativo para explorar os dados oficiais, estatísticas e curiosidades dos jogadores de futebol da temporada de 2023.

## 📌 Sobre o Projeto

Este projeto foi construído para transformar uma base de dados gigante (com mais de 17.000 jogadores) em um painel visual fácil de usar. O objetivo principal é permitir que qualquer pessoa pesquise seus times e jogadores favoritos, analisando desde informações físicas (idade, altura, peso) até dados financeiros (valor de mercado, salário e multas rescisórias).

Além de ser uma ferramenta de consulta, este projeto aplica boas práticas de organização de código e separação de responsabilidades, garantindo que o aplicativo seja rápido e fácil de manter.

## 🛠️ O que você vai encontrar aqui

* **Página Principal:** Um resumo sobre a base de dados oficial do FIFA 23.
* **Visão de Jogadores:** Um painel detalhado do atleta escolhido, trazendo sua foto oficial, nacionalidade e uma barra de progresso com sua nota geral (Overall).
* **Visão de Times:** Uma tabela completa com o elenco do clube selecionado, exibindo o escudo do time e comparando as estatísticas de todos os atletas lado a lado.

## 🚀 Como rodar o projeto no seu computador

Para testar o aplicativo na sua máquina, você precisará ter o Python instalado. Siga os passos abaixo:

**1. Instale as ferramentas necessárias**
Abra o seu terminal (linha de comando) e instale as bibliotecas que o projeto utiliza:
```bash
pip install pandas streamlit requests
```

**2. Inicie o aplicativo**
No terminal, navegue até a pasta onde o projeto está salvo e rode o comando principal:
```bash
streamlit run main.py
```
O aplicativo abrirá automaticamente no seu navegador de internet!

## 📂 Como organizamos a estrutura

Para manter o código limpo, o projeto foi dividido em partes menores, cada uma com uma função específica:

* **`main.py`**: É o maestro do projeto. Ele não tem visual próprio, serve apenas para configurar o menu lateral e direcionar você para as páginas corretas.
* **`data_loader.py`**: É o motor de dados. Ele lê a planilha do FIFA, limpa as informações de dinheiro e formata as datas, entregando tudo pronto para a tela usar.
* **`paginas/`**: Uma pasta que guarda os arquivos visuais (1_Home, 2_Players e 3_Teams). Elas focam apenas em desenhar a tela e buscar as imagens na internet.

## Referência tutoriais do AsimovAcademy 

## 👨‍💻 Autor

Desenvolvido por **Alessandro França**  Desenvolvedor de Automação RPA | Desenvolvedor Python & .NET  
🔗 [Conecte-se comigo no LinkedIn](https://www.linkedin.com/in/alessandro-franca-rpa-developer/)
