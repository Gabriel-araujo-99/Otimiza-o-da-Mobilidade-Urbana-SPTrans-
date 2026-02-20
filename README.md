# Otimização da Mobilidade Urbana - SPTrans (Projeto Semantix)
Este projeto visa analisar os dados de transporte público da cidade de São Paulo (SPTrans) para identificar gargalos operacionais e propor melhorias na mobilidade urbana utilizando técnicas de Big Data e Engenharia de Dados.

## 1. Dissertação sobre o Problema: Variabilidade do Tempo de Viagem
### Descrição do Problema
O sistema de transporte de São Paulo enfrenta grandes desafios com a discrepância entre o horário planejado e o executado. Fatores como congestionamentos e alta densidade de paradas em determinadas linhas geram atrasos sistêmicos. O objetivo deste projeto é identificar as linhas críticas através da análise de dados de telemetria e itinerários.

### Relevância
Resolver o problema da variabilidade do tempo de viagem impacta diretamente na produtividade da cidade e na qualidade de vida de milhões de usuários. Para empresas como a Semantix, este projeto demonstra a capacidade de transformar dados brutos de cidades inteligentes em inteligência de negócio.

## 2. Levantamento das Fontes de Dados
Para este projeto, utilizamos o padrão internacional GTFS (General Transit Feed Specification) fornecido pela SPTrans.
### API Olho Vivo (HTTPS)
Tipo de dados : Semiestruturado (JSON)

Método de coleta : Coleta de telemetria em tempo real.

### Arquivos GTFS
Tipo de dados : Estruturado (CSV/.txt)

Método de coleta: Dados estáticos de rotas, paradas e horários.

## 3. Análise Exploratória de Dados (EDA)
Utilizei Python e a biblioteca Pandas no ambiente VS Code para realizar o processamento dos dados.

### 3.1. Limpeza e Pré-processamento
* Normalização: Tratamento dos arquivos .txt e conversão para DataFrames.

* Integridade: Cruzamento das tabelas de rotas e horários para garantir a consistência dos dados.

* Filtros: Limpeza de registros duplicados e validação de campos obrigatórios.

## 3.2. Análise Descritiva e Padrões
* Volume Analisado: 1.347 rotas únicas.

* Média do Sistema: A média de paradas por itinerário em São Paulo é de 43,65.

* Padrão Detectado: As linhas noturnas apresentam as maiores extensões e maior número de paradas, saindo significativamente da média do sistema.

### 3.3. Variáveis e Correlações
A variável mais importante identificada foi a quantidade de paradas por viagem, que apresenta correlação direta com o risco de atrasos acumulados.

## 4. Relatório de Insights (Tomada de Decisão)
Após a análise técnica, extraímos os seguintes insights estratégicos:

* Gargalos Logísticos: Identificamos as 5 linhas com maior número de paradas (Outliers), lideradas pela linha N137-11-0 (146 paradas).

* Risco Operacional: Linhas com mais de 100 paradas possuem uma "janela de erro" elevada. Recomendamos o monitoramento prioritário com sensores IoT nessas rotas.

* Sugestão de Melhoria: Implementação de faixas exclusivas ou paradas expressas nos trechos críticos dessas linhas para reduzir a variabilidade do tempo de viagem.

## 5. Visualização de Dados (Dashboard)
A visualização geográfica foi desenvolvida no Looker Studio, utilizando os dados de latitude e longitude das paradas para mapear a cobertura do sistema.

* Ferramenta: Google Looker Studio.

* Visualização: Mapa de densidade de paradas.

## 🛠️ Tecnologias Utilizadas
* Linguagem: Python 3.13

* Bibliotecas: Pandas

* IDE: Visual Studio Code (VS Code)

* Visualização: Looker Studio

---
## 📩 Contato

---
## 📩 Contato

Gostou do projeto ou tem alguma dúvida? Entre em contato comigo:

* **LinkedIn:** [Gabriel Araujo](https://www.linkedin.com/in/gabriel-araujo-a99a833a4/)
* **E-mail:** Gabrielaraujobr99@gmail.com
* **Portfólio GitHub:** [Gabriel-araujo-99](https://github.com/Gabriel-araujo-99)
