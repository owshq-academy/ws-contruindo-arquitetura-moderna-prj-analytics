# Proposta de Arquitetura de Dados

Desenvolver a suas habilidades usando os documentos presentes nesse repo.

*crie um novo arquivo a partir deste com o nome proposta_nome_20250125.md*


1.	Qual Arquitetura de Dados você escolheria para esse projeto?

Resposta:
    Usaria a arqutietura Lakehouse em batch

Justificativa:
    Baseado na expectativa de crescimento dos dados e por ser algo grande eu iria para a arquitetura Lakehouse com Iceberg
Isso iria auxiliar na performance e reduziria o custo relacionado ao DW, podendo utilizar MinIO ou até mesmo  os
armazenamentos das nuvens.

2.	Quais tecnologias você utilizaria dentro da sua arquitetura?

Resposta:
- k8s para arquitetura
- Orquestração: Airflow
- Ingestão: Airbyte
- Formato de arquivos: Iceberg para lakehouse
- Motor de processamento: Trino
- Transformação: DBT
- Armazenamento: MinIO
- Visualização: Apache Superset

Justificativa sua resposta:
    Utilizando essa arquitetura conseguiria ter um escalonamento tanto em processamento quanto no acesso aos dados, pois
dessa forma conseguimos escalar o armazenamento e o motor de processamento

3.	Explique como as tecnologias escolhidas irão se integrar na sua arquitetura de dados.

Resposta:
    A integração seria:
- Airbyte realizando a ingestão dos dados no MinIO na camada bronze.
- Airflow iniciaria a dag chamando o DBT para realizar o processamento dos dados gerando as camadas silver e gold
- Apache Superset conectando no Trino para realizar as visualizações dos dados

