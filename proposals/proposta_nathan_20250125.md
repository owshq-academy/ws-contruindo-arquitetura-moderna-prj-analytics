# Proposta de Arquitetura de Dados

Desenvolver a suas habilidades usando os documentos presentes nesse repo.


1.	Qual Arquitetura de Dados você escolheria para esse projeto?

Resposta: Kappa + Lakehouse

Justificativa: Pois na maioria dos requisitos de negócio foram identificados a necessidade de processamento em streaming de dados, alta taxa de crescimento do dado para algumas fontes e nível de complexidade não ser alta, envolvendo várias camadas.


2.	Quais tecnologias você utilizaria dentro da sua arquitetura?

Resposta: Kafka, Spark, Object Storage

Justificativa sua resposta:

3.	Explique como as tecnologias escolhidas irão se integrar na sua arquitetura de dados.

Resposta: Kafka (Integração) > Spark (Processamento) > Object Storage (Bronze) > Spark > OS (Silver) > Spark > OS (Gold)
