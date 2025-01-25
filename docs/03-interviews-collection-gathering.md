# Interviews - Collection Gathering

### Day 01: Current Data Architecture & Data Sources

#### Interview with Core Banking Data Owner
* How is data produced?
Data is produced through our Core Banking System. Every transaction, account creation, and update is recorded in the system.
* What would you like to analyze in your data or in other departments?
I’d like to analyze customer spending patterns in conjunction with data from the Credit Cards team to identify cross-sell opportunities for savings products.
* How frequently do you need access to the data?
For transactions, we require real-time access for fraud detection and regulatory compliance. Account-level data can be updated daily.

#### Interview with Compliance Data Owner
* How is data produced?
Data is generated through our Compliance Management System, which captures Know Your Customer (KYC) and Anti-Money Laundering (AML) records.
* What would you like to analyze in your data or in other departments?
I’d like to correlate customer profiles with data from Transactions to flag suspicious activity.
* How frequently do you need access to the data?
KYC updates can be processed monthly, but AML monitoring requires real-time alerts.

#### Data Sources Overview
Technologies: PostgreSQL, MySQL, SQL Server, MongoDB, and some legacy systems like Oracle.
Data Sources:
  * Core Banking System (10TB/year growth)
  * Credit Card Processing System (5TB/year growth)
  * Compliance System (2TB/year growth)
  * Digital Banking Platform (20TB/year growth)

### Day 02: Data Team and Software Team Analysis

#### Interview with Data Engineer
* What are your skills?
I have experience with ETL processes, SQL, and am starting to learn Python for advanced transformations.
* What are the biggest challenges today?
Moving data across legacy systems and modern platforms is a major challenge.
There’s limited automation in reporting pipelines, which delays access to data.
Departments struggle to collaborate due to siloed data.
* What technologies do you use?
We use DataStage, SSIS, and some custom SQL scripts. These tools are functional but outdated for modern requirements.

#### Interview with Software Engineer
* What are your skills?
I specialize in Java and C#, primarily building APIs for data retrieval.
* What are the biggest challenges today?
Integrating real-time data into our systems.
Supporting new features like machine learning or generative AI pipelines.
* What technologies do you use?
We’re mostly using legacy platforms for integration, like SOAP-based web services, which are inefficient for modern data needs.

### Day 03: Data Processing

#### Interview with Data Analyst
* How is data transformed?
Data is processed in batch jobs. For example, transaction data is extracted nightly, joined with customer and account data, and aggregated for daily reports.
* What are the business rules for transformation?
Customer data is deduplicated and validated using CPF/CNPJ.
Transactions are enriched with category tags based on merchant codes.
Compliance data undergoes a series of validation checks against regulatory requirements.

Current State of Processing
* Frequency: Most data is processed daily, except for real-time fraud detection in transactions.
  * Challenges:
    * Long batch processing times due to large data volumes.
    * Lack of standardization in transformation rules across departments.

### Day 04: Data Serving

Interview with Reporting Manager
* How is data presented?
  * Reports are generated using Power BI and Tableau.
  * For executive dashboards, we use Excel, which is manually updated.
* What applications consume the data?
  * Mobile banking apps rely on APIs to fetch customer balances.
  * Fraud detection systems use transaction data streams in real-time.
* What challenges exist in data serving?
  * Latency in real-time dashboards.
  * Limited API capabilities for external integrations.

Interview with Branch Manager
* How do you use data in branches?
  * Customer account and loan data are accessed via our Branch Management System.
  * Reports on branch performance are generated monthly.
* Challenges:
  * Reports are often outdated when we receive them.
  * We lack granular insights into branch-level performance metrics.

### Day 05: Business Expectations

#### Interview with Product Manager
* What are your expectations for new features?
We need real-time insights into customer behavior for personalized marketing.
Integrating machine learning models to predict loan defaults would be beneficial.
A unified data platform to break departmental silos is critical.
* How would you like to consume data?
Through self-service analytics platforms.
APIs for on-demand data integration into our applications.

#### Interview with Marketing Manager
* What are your expectations for data?
We need deeper insights into customer spending patterns for targeted campaigns.
Cross-department collaboration to align marketing efforts with compliance and product data.
* How would you like to consume data?
Pre-built dashboards that combine transaction and demographic data.
Real-time feeds to track campaign performance.

### Summary of Interviews

The interviews revealed key insights:
1. Challenges:
   * Legacy systems hinder scalability and real-time capabilities.
   * Lack of collaboration between departments due to siloed data.
2. Expectations:
   * Real-time reporting, predictive analytics, and a unified data platform.
3. Opportunities:
   * Modernizing data infrastructure with scalable cloud platforms.
   * Empowering teams with self-service tools and democratized data access.