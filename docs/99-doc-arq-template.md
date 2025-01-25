# Documento Arquitetural para Plataforma de Dados

## Histórico de Mudança

| Data       | Versão | Descrição              | Status      |
|------------|--------|------------------------|-------------|
| 2023-11-28 | 1.0    | Criação do Documento   | Realizado   |
| 2023-11-30 | 1.0    | Revisão do Documento   | Realizado   |
| 2023-12-07 | 1.0    | Validação Técnica      | Realizado   |
| 2023-12-13 | 1.0    | Validação do Cliente   | Em processo |

---


## Levantamento de Requisitos

Requisitos levantados por meio de reuniões focadas em:
- Ambiente Atual e Infraestrutura
- Fontes de Dados e Sistemas
- Processamento e Transformação de Dados
- Expectativas do Negócio

Objetivo: identificar problemas de disponibilidade de dados e oportunidades de valor.

---

## Ambiente Atual e Infraestrutura

- **Banco de Dados**: 
  - Volume de X
- **Linguagens**: 
- **Sistemas**: 

---

## Cenário Atual de Arquitetura de Dados

### Lambda
- Dividido em:
  - **Cold Layer**: Processos batch para dados históricos.
  - **Hot Layer**: Processos streaming para dados em tempo real.
- Suporta ingestão, armazenamento e processamento em data warehouses modernos.

### Kappa
- Simplificação da Lambda com uma única camada de ingestão.
- Uso de tecnologias como Apache Kafka para dados em batch e streaming.
- Armazenamento em data lakes para histórico.

### Data Lakehouse
- Combinação de recursos de Data Lakes e Data Warehouses.
- Modelo de camadas Medallion:
  - **Bronze**: Dados brutos.
  - **Silver**: Dados tratados e organizados.
  - **Gold**: Dados prontos para consumo.

### Data Mesh
- Governança distribuída com domínios autônomos:
  - **Domínios**: Responsáveis pelos dados operacionais e analíticos.
  - **Governança Federada**: Garantia de políticas, segurança e compliance.
  - **Dados como Produto**: Entregas analíticas específicas.

### Modern Data Stack
- Utiliza DBT para processamento e modelagem.
- Data Warehouse como componente central para dados analíticos e brutos.

---

## Nova Arquitetura de Dados

### Arquitetura Atual

Exemplo

Desafios identificados:
- Baixa latência para análise de dados.
- Unificação dos dados para machine learning e analytics.
- Advanced Analytics e cruzamento de informações entre fontes.

### Propostas de Arquitetura Gerenciada

#### Microsoft Azure
**Kappa**:
- **Ingestão**: Confluent Cloud (Apache Kafka).
- **Armazenamento**: Azure Blob Storage, Delta Lake.
- **Processamento**: Databricks.
- **Entrega de Dados**: Databricks SQL.
- **Orquestração**: Databricks Workflows.

**Lambda**:
- Similar ao modelo Kappa, mas inclui Azure Event Hubs e Azure Functions.

#### Amazon AWS
**Kappa**:
- **Ingestão**: Confluent Cloud.
- **Armazenamento**: Amazon S3, Delta Lake.
- **Processamento**: Databricks.
- **Entrega de Dados**: Databricks SQL.
- **Orquestração**: Databricks Workflows.

**Lambda**:
- **Ingestão**: AWS Lambda, AWS Kinesis.
- **ETL**: AWS Glue.

#### Google GCP
**Kappa**:
- **Ingestão**: Confluent Cloud.
- **Armazenamento**: Google Cloud Storage, Delta Lake.
- **Processamento**: Databricks.
- **Entrega de Dados**: Databricks SQL.
- **Orquestração**: Databricks Workflows.

**Lambda**:
- **Ingestão**: Google Functions, Google Pub/Sub.
- **ETL**: Google Data Fusion.

---

## Estimativa de Custos

Estimativas de custo para cada provedor de nuvem baseadas em requisitos e serviços sob demanda. 

Exemplo para **Microsoft Azure - Kappa**:
- **Confluent Cloud**: $1,580.00/mês.
- **Databricks**: $490.56/mês (cluster).
- **Armazenamento**: $53.00/mês.
- **Custo anual total**: ~$61,400.00.

---

## Plano de Ação

### Atividades Estimadas
1. **Infraestrutura**: Configuração via Terraform - XXX horas.
2. **Desenvolvimento**: Implementação de pipelines e regras de negócio - XXX horas.
3. **Orquestração**: Configuração de workflows - XX horas.
4. **Documentação e Treinamento**: XX horas.

### Ambiente de Desenvolvimento
Início com ambiente de desenvolvimento para maior liberdade e validação.

---

## Considerações Finais

- **Modelos Kappa & Lambda**: Ambas as arquiteturas oferecem flexibilidade para ingestão e processamento em batch e streaming.
- **Cloud Providers**: Comparações realizadas entre Azure, AWS e GCP.
- **Benefícios**:
  - Aplicações orientadas a eventos.
  - Integração com modelos LLM para inteligência generativa.
  - Modernização com tecnologias de ponta.

---

**Nota:** Este documento é genérico e pode ser adaptado para diversas organizações.