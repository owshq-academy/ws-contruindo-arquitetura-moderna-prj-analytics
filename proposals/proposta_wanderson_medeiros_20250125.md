# Proposta de Arquitetura de Dados

Desenvolver a suas habilidades usando os documentos presentes nesse repo.

*crie um novo arquivo a partir deste com o nome proposta_wanderson_20250125.md*


1.	Qual Arquitetura de Dados você escolheria para esse projeto?

Resposta: LAMBDA

Justificativa: De acordo com a visao de negocio, existe datasets que podem usados de forma analitica e outras de online principalmente movimentacao bancaria. 


2.	Quais tecnologias você utilizaria dentro da sua arquitetura?

Resposta: Kafka, data lake (com ingestao do airbyte), processamento com spark e data Warehouse (redshift ou outras)

Justificativa sua resposta: pensamento de manter este ambiente de forma onde podemos crescer e facil ajustes futuros

3.	Explique como as tecnologias escolhidas irão se integrar na sua arquitetura de dados.

Resposta: airbyte inserir os dados dentro da datalake e com isso realizar todo o processo curared e analise dos dados e quanto isso o kafka fara
	      todo o processo de ingestao ou online para podemos trabalhar a analise do dado e sua gestao.

