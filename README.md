Descrição Detalhada do Problema
O sistema de transporte público da cidade de São Paulo é um dos maiores do mundo, gerenciado pela SPTrans. O desafio reside na variabilidade do tempo de viagem. Embora existam horários planejados, fatores como congestionamentos, incidentes viários e excesso de demanda em horários de pico criam uma discrepância entre o planejado e o executado.

O problema específico que abordaremos é a identificação de gargalos operacionais: trechos onde a velocidade média dos ônibus cai abaixo do esperado, indicando a necessidade de faixas exclusivas ou ajustes na frequência das linhas. Sem análise de dados, essa gestão é reativa; com dados, ela se torna preditiva.

Importância e Relevância
Contexto Social: São Paulo possui milhões de usuários diários. Reduzir o tempo de deslocamento impacta diretamente na produtividade e no bem-estar da população.

Contexto de Negócio (Foco Semantix): Para empresas de tecnologia de dados, resolver problemas de mobilidade demonstra domínio sobre Sistemas de Informação Geográfica (GIS) e processamento de fluxos de dados massivos.

Contexto Econômico: Otimizar rotas significa reduzir o consumo de diesel e o desgaste da frota, gerando economia direta para as operadoras e para o município.

Como a Análise de Dados pode Solucionar o Problema
A solução reside no uso da Engenharia de Dados para transformar sinais brutos em inteligência urbana:

Ingestão de Dados (Big Data): Captura de milhões de registros de GPS enviados pelos ônibus de SP através da API Olho Vivo.

Transformação com PySpark: Limpeza e normalização dos dados. Cálculo da velocidade média instantânea cruzando a variação de distância e tempo entre as coordenadas.

Identificação de Anomalias: Comparação da velocidade real com a velocidade histórica para detectar atrasos sistêmicos em trechos específicos da cidade.

Apoio à Decisão: Fornecimento de métricas claras para que gestores possam decidir onde implementar melhorias de infraestrutura viária.
