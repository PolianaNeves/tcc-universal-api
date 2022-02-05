# **PUC Minas - Pós Graduação Inteligência Artificial**
## **Trabalho de Conclusão de Curso - Poliana Neves**
### Universal Studios Reviews - *Analysis*


---


API desenvolvida para consumo da aplicação de dashboard. Desenvolvida em `python`, usando o framework `fastapi`.

**Instalação**

Alguns pacotes usados no projeto não estão contidos no requirements.txt e devem ser instalados manualmente, de acordo 
com a instância que estiver utilizando (MacOs, Linux ou Windows). São eles: `prophet` e `pystan`

Para instruções de intalação destes pacotes específicos, consulte a [documentação aqui](https://facebook.github.io/prophet/docs/installation.html#python).

Para os demais pacotes:

Requisitos: `python 3.8 ou superior`

1. Clone o repo para sua máquina
2. Crie um ambiente virtual `python -m venv venv`
3. Ative o ambiente virtual de acordo com sua instância `cd venv/scripts/activate` ou `source venv/bin/activate`
4. Instale os pacotes específicos
5. Instale os pacotes de requirements `pip install -r requirements.txt`

Para executar a api, use o comando `uvicorn main:app --reload`

**Erros de instalação dos pacotes específicos no Windows**

Existem alguns erros que podem ser obtidos com estes pacotes, visto que a bilbioteca `pystan` não tem suporte para este OS.
Entretanto, a execução da api em máquina Windows pode ser realizada de outras formas, como por exemplo, usando `wsl`.
Segue link com explicação útil para execução da api neste OS: [Lasse Schmidt](https://lasse-schmidt90.medium.com/how-to-install-pystan-on-windows-a9918f51111)

**ATENÇÃO**

Os arquivos da pasta assets foram gerados com os dados obtidos através dos datasets atualizados no momento. O primeiro processamento é muito demorado devido aos modelos de machine learning que são executados. Caso queira gerá-los novamente, exclua os arquivos de imagem da pasta assets.
