

# Banking System Data Requirements

This document specifies the basic requirements for the datasets used in the banking system.

#### Datasets Overview

1. Customers
   * Department Owner: Customer Relationship Management (CRM)
   * System Produces Data: Customer Management System (CMS)
   * Programming Language: Java
   * Expectation of Data Growth: Linear growth (~10% annually) as the customer base expands.
   * Business Tags: CRM, KYC, Customer Onboarding
   * Where is Stored: Database (PostgreSQL)

2. Accounts
   * Department Owner: Core Banking
   * System Produces Data: Core Banking System
   * Programming Language: C#
   * Expectation of Data Growth: Moderate (~8% annually) with the addition of new accounts and savings products.
   * Business Tags: Core Banking, Financial Products, Account Management
   * Where is Stored: Database (MySQL)

3. Transactions
   * Department Owner: Payments & Operations
   * System Produces Data: Payment Gateway
   * Programming Language: Golang
   * Expectation of Data Growth: High (30-50% annually), driven by digital transactions.
   * Business Tags: Payments, Operations, Revenue
   * Where is Stored: Database (Oracle)

4. Loans
   * Department Owner: Lending & Credit
   * System Produces Data: Loan Management System
   * Programming Language: .NET
   * Expectation of Data Growth: Steady (~12% annually), based on loan disbursements and repayments.
   * Business Tags: Lending, Credit Risk, Debt Management
   * Where is Stored: Database (SQL Server)

5. Credit Cards
   * Department Owner: Card Services
   * System Produces Data: Credit Card Processing System
   * Programming Language: TypeScript
   * Expectation of Data Growth: High (~25% annually), fueled by increasing card usage.
   * Business Tags: Card Services, Fraud Detection, Revenue
   * Where is Stored: Database (MongoDB)

6. Branches
   * Department Owner: Branch Network
   * System Produces Data: Branch Management System
   * Programming Language: Java
   * Expectation of Data Growth: Minimal (~3% annually) as branch additions slow down.
   * Business Tags: Branch Operations, Network Management
   * Where is Stored: Database (PostgreSQL)

7. Compliance
   * Department Owner: Compliance & Risk
   * System Produces Data: Compliance Management System
   * Programming Language: Java
   * Expectation of Data Growth: Moderate (~15% annually), driven by new regulatory requirements.
   * Business Tags: Regulatory Compliance, AML, KYC
   * Where is Stored: Database (MySQL)

8. Investments
   * Department Owner: Wealth Management
   * System Produces Data: Investment Management System
   * Programming Language: Golang
   * Expectation of Data Growth: Moderate (~10% annually), aligned with customer portfolio growth.
   * Business Tags: Wealth, Portfolio Management, Revenue
   * Where is Stored: Database (SQL Server)

9. Digital Activity
   * Department Owner: Digital Banking
   * System Produces Data: Digital Banking Platform
   * Programming Language: TypeScript
   * Expectation of Data Growth: High (~50% annually), as digital adoption increases.
   * Business Tags: Digital Banking, Customer Engagement, Fraud Monitoring
   * Where is Stored: Database (MongoDB)


## Summary of Storage Locations

| Dataset          | Department Owner           | System Produces Data          | Programming Language | Storage Location | Technology | Data Growth Expectation          |
|------------------|----------------------------|-------------------------------|----------------------|------------------|------------|-----------------------------------|
| Customers        | Customer Relationship Management (CRM) | Customer Management System (CMS) | Java                 | Database        | PostgreSQL | Linear (~10% annually)           |
| Accounts         | Core Banking               | Core Banking System           | C#                   | Database        | MySQL      | Moderate (~8% annually)          |
| Transactions     | Payments & Operations      | Payment Gateway               | Golang               | Database        | Oracle     | High (30-50% annually)           |
| Loans            | Lending & Credit           | Loan Management System        | .NET                 | Database        | SQL Server | Steady (~12% annually)           |
| Credit Cards     | Card Services              | Credit Card Processing System | TypeScript           | Database        | MongoDB    | High (~25% annually)             |
| Branches         | Branch Network             | Branch Management System      | Java                 | Database        | PostgreSQL | Minimal (~3% annually)           |
| Compliance       | Compliance & Risk          | Compliance Management System  | Java                 | Database        | MySQL      | Moderate (~15% annually)         |
| Investments      | Wealth Management          | Investment Management System  | Golang               | Database        | SQL Server | Moderate (~10% annually)         |
| Digital Activity | Digital Banking            | Digital Banking Platform      | TypeScript           | Database        | MongoDB    | High (~50% annually)             |