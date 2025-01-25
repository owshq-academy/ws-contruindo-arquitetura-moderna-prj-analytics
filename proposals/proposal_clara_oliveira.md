# Plumbers Bank Architecture Propose 

## Ingestion:

Kafka for real time process 

## Processing :

Databricks spark Data Lake for batch data and for real time in separated layers. 

DBT for modeling data using medallion architecture / start schema

Azure Storage for storage the data 

Process transaction in real time integrating with fraud models and alerts to the envolved teams

## Analytics:

Power BI  updated in batch for the not real time and in near real time for transactions

Powert BI different environemnt for each departament 

## Orchestration:

Airflow to orchestrate the hole pipeline. It means the ingestion, all the dbt transformations and tests and data sources updates.