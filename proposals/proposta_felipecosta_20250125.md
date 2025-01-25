# Proposta de Arquitetura de Dados

Desenvolver a suas habilidades usando os documentos presentes nesse repo.


1.	Qual Arquitetura de Dados você escolheria para esse projeto?

Resposta: Lambda Architecture

Justificativa: A necessidade de processamento real-time foi identificada para disponilizar insights real-time principalmente de transactions e digital activities. Entretanto existem muitos datasets que podem ser processados em batch.
Dessa forma podemos utlizar Lambda e aproveitar o conhecimento já existente do time em ETL e batch processing o que pode agilizar o TTM e construir uma layer de streaming para processamento real-time.

2.	Quais tecnologias você utilizaria dentro da sua arquitetura?


Resposta:

Data Lake: Azure Data Lake Generation 2
Data Ingestion and Orchestration: ADF
Data Processing: Databricks (SQL Notebooks)
Real-Time: Event Hub (Kafka)
DW: Databricks SQL
Data Catalog: Unity

Justificativa sua resposta: ADF para batch ingestion no Data Lake para facilitar a adoção pelo time com previa experiência em SSIS.
Event Hub para real time ingestion mais fácil de gerenciar.
Databricks para processamento Batch e Real Time
Databricks SQL para self-service analytics e Unity catalog para Data Governance


3.	Explique como as tecnologias escolhidas irão se integrar na sua arquitetura de dados.

Resposta:

Hot Layer: Data chega nos tópicos do Event Hub e é consumido através de um DLT pipeline no Databricks.
Dados são processados e disponibilizados no Databricks SQL.
Cold-Layer: Dados são extraídos usando ADF e inseridos no lake. A dlt pipeline faz o processamento a partir daí.