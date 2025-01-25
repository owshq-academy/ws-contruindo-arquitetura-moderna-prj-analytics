# Proposta de Arquitetura de Dados

Desenvolver a suas habilidades usando os documentos presentes nesse repo.

*crie um novo arquivo a partir deste com o nome proposta_nome_20250125.md*


1.	Qual Arquitetura de Dados você escolheria para esse projeto?

Resposta:
Medallion Mesh Architecture


Justificativa:
O Medallion Mesh Architecture vai beneficiar com controles por boundaries. Cada domínio
(composto por pessoa do negócio + TI) tem o conhecimento melhor do seu próprio dado.
Também aumenta o controle de quem vai ter acesso ao dado ou não e exige a criação de 
data contracts, que documenta bem o produto de dados criado em como utiliza-lo, para o que 
serve e para o que não serve.

2.	Quais tecnologias você utilizaria dentro da sua arquitetura?

Resposta:
- Cloud: 
- Azure ou AWS
- ADLS Gen2 ou S3

Tools
- Debezium ou outra ferramenta que consuma CDC dos DB's
- Databricks
- Unity Catalog

Serving:
- Power Bi
- Tableau

Justificativa sua resposta:

3.	Explique como as tecnologias escolhidas irão se integrar na sua arquitetura de dados.

Resposta:

O Databricks com o Unity Catalog traz benefícios como ser friendly user para times técnicos que tem mais domínio sobre SQL e desenvolvimento de pipelines low-code. O Unity Catalog traz a vantagem para Governaça, Linhagem, Data Quality e documentação, garantindo os boundaries propostos pelo Data Mesh. E a modelagem em camadas do Medallion, garante um SSOT dentro do domínio. 