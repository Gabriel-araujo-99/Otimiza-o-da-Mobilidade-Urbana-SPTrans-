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

## 3. 3. Análise Exploratória de Dados (EDA) 
Com a execução do script final, os seguintes marcos foram alcançados:

### 3.1. Limpeza e Pré-processamento
* Limpeza de Dados: Foram tratados 9 valores nulos e removidas duplicatas, garantindo a integridade da análise.

## 3.2. Análise Descritiva e Padrões
* Volume Analisado: 1.347 rotas únicas.

* Média Operacional: A média do sistema integrado analisado é de 43,65 paradas por itinerário.

### 3.3. Variáveis e Correlações
* Análise de Correlação: O resultado nan na correlação matemática automatizada revelou que o route_id não é uma variável puramente numérica, indicando que a nomenclatura das linhas segue uma lógica categórica (regional/modal) e não sequencial.

## 4. Relatório de Insights (Tomada de Decisão)
Com base no TOP 5 gerado pelo código, extraímos os seguintes insights:

* Eficiência dos Estruturais: As linhas com maior densidade de paradas no dataset processado são o Metrô L1 (23 paradas) e a CPTM L08 (22 paradas).

* Divergência de Dados: Note que, embora essas linhas tenham "muitas paradas" no contexto de trilhos, elas são extremamente eficientes comparadas à média de ônibus (43,65). Isso indica que o sistema sobre trilhos em São Paulo é o pilar de estabilidade do tempo de viagem.

* Decisão Estratégica: Recomendamos focar a integração tarifária e física nos pontos de alta densidade (Tucuruvi, Jabaquara e Luz), pois são os nós críticos onde a maior quantidade de passageiros realiza transferências.

## 5. Visualização de Dados (Dashboard)
A visualização geográfica foi desenvolvida no Looker Studio, utilizando os dados de latitude e longitude das paradas para mapear a cobertura do sistema.

* Ferramenta: Google Looker Studio.

* Visualização: Mapa de densidade de paradas.

## 🛠️ Tecnologias Utilizadas
* Linguagem: Python 3.13

* Bibliotecas: Pandas

* IDE: Visual Studio Code (VS Code)

* Visualização: Looker Studio
  
## 🏁 Conclusão
Este projeto demonstrou como a aplicação de técnicas de Data Engineering e EDA (Exploratory Data Analysis) pode transformar arquivos brutos do sistema SPTrans em insights acionáveis para a gestão pública.

Através do processamento de mais de 1.300 rotas, foi possível identificar que o sistema sobre trilhos (Metrô/CPTM) atua como o esqueleto de estabilidade da cidade, enquanto as linhas de superfície (ônibus) enfrentam o desafio da alta densidade de paradas. A capacidade de limpar dados inconsistentes e cruzar diferentes fontes de informação é o que permite a criação de soluções inteligentes para cidades mais conectadas.

---
## 📩 Contato

Gostou do projeto ou tem alguma dúvida? Entre em contato comigo:

* **LinkedIn:** [Gabriel Araujo](https://www.linkedin.com/in/gabriel-araujo-a99a833a4/)
* **E-mail:** Gabrielaraujobr99@gmail.com
* **Portfólio GitHub:** [Gabriel-araujo-99](https://github.com/Gabriel-araujo-99)
