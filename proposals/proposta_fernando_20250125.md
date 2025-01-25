# Proposta de Arquitetura de Dados

Desenvolver a suas habilidades usando os documentos presentes nesse repo.



1.	Qual Arquitetura de Dados você escolheria para esse projeto?

Resposta: Data Lakehouse

Justificativa: Essa arquitetura atende os requisitos da arquitetura e tem as camadas de tratamento 

2.	Quais tecnologias você utilizaria dentro da sua arquitetura?
3.	Explique como as tecnologias escolhidas irão se integrar na sua arquitetura de dados.
Resposta: 
    Kafka
    Data Factory
    (Spark)Azure Databricks
    Power Bi

Justificativa sua resposta:
Como esse projeto necessita ter processamento em Batch e Streaming 
Ingestão: 
Batch: Data Factory enviando os dados para a camada raw / bronze
Stream: Kafka enviando os dados de transações para as análises em tempo real de transações e fraudes que é uma necessidade do negócio
Processamento:
Spark (Spark)Azure Databricks usando pipeline DLT para processamento em tempo real / um
Visualização:
Power Bi para consumir os dados na camada Gold

Governança:
Unity Catalog do Databricks



