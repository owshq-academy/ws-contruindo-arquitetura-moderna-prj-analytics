# **Execution Guide: Generating Datasets**

This guide outlines the steps to generate the synthetic datasets for the banking system.

---

## **Prerequisites**
1. Ensure Python 3.11 or higher is installed.
2. Install required dependencies:
```shell
pip install -r requirements.txt
```
Verify the project directory structure:
```bash
ws-contruindo-arquitetura-moderna-dados-prj-analytics/
├── requirements.txt            # Dependencies for the project
├── data/                       # Data generation and storage directory
│   ├── financial_services/     # Banking datasets and scripts
│   │   ├── datasets/           # Generated datasets in JSON format
│   │   ├── scripts/            # Python scripts for dataset generation
│   │   │   ├── accounts.py
│   │   │   ├── branches.py
│   │   │   ├── compliance.py
│   │   │   ├── credit_cards.py
│   │   │   ├── customers.py
│   │   │   ├── digital_activity.py
│   │   │   ├── investments.py
│   │   │   ├── loans.py
│   │   │   ├── transactions.py
```
Execution Steps

Step 1: Generate Customer Data

Run the customers.py script to generate customer data:
```shell
python scripts/customers.py
```
* Output File: datasets/customers.json
* Purpose: Base dataset containing customer information. Other datasets depend on customer_id from this file.

Step 2: Generate Account Data

Run the accounts.py script:
```shell
python scripts/accounts.py
```
* Output File: datasets/accounts.json
* Purpose: Bank account data linked to customers using customer_id.

Step 3: Generate Transaction Data

Run the transactions.py script:
```shell
python scripts/transactions.py
```
* Output File: datasets/transactions.json
* Purpose: Transaction history linked to account_id.

Step 4: Generate Loan Data

Run the loans.py script:
```shell
python scripts/loans.py
```
* Output File: datasets/loans.json
* Purpose: Loan details linked to customers using customer_id.

Step 5: Generate Credit Card Data

Run the credit_cards.py script:
```shell
python scripts/credit_cards.py
```
* Output File: datasets/credit_cards.json
* Purpose: Credit card accounts linked to customers using customer_id.

Step 6: Generate Branch Data

Run the branches.py script:
```shell
python scripts/branches.py
```
* Output File: datasets/branches.json
* Purpose: Details of bank branches, including branch_id.

Step 7: Generate Compliance Data

Run the compliance.py script:
```shell
python scripts/compliance.py
```
* Output File: datasets/compliance.json
* Purpose: Regulatory compliance data linked to customers using customer_id.

Step 8: Generate Investment Data

Run the investments.py script:
```shell
python scripts/investments.py
```
* Output File: datasets/investments.json
* Purpose: Investment accounts linked to customer_id and account_id.

Step 9: Generate Digital Activity Data

Run the digital_activity.py script:
```shell
python scripts/digital_activity.py
```
* Output File: datasets/digital_activity.json
* Purpose: Logs of digital interactions linked to customers using customer_id.

Execution Order

To ensure proper dependency resolution (e.g., customer_id, account_id), execute the scripts in the following order:
1.	customers.py
2.	accounts.py
3.	transactions.py
4.	loans.py
5.	credit_cards.py
6.	branches.py
7.	compliance.py
8.	investments.py
9.	digital_activity.py

Troubleshooting
	•	If a script fails to find a required file, ensure the previous scripts were executed successfully and the datasets/ folder exists.
	•	Validate file paths in each script if running from a different working directory.
	•	For date-related errors, verify that dateutil is installed:
```shell
pip install python-dateutil
```
Expected Outputs

Once all scripts are executed, the datasets/ folder will contain:
```bash
datasets/
├── accounts.json          # Bank account data linked to customers
├── branches.json          # Information about bank branches
├── compliance.json        # Regulatory compliance data (e.g., KYC, AML)
├── credit_cards.json      # Credit card account data linked to customers
├── customers.json         # Customer information (base dataset)
├── digital_activity.json  # Logs of customer interactions on digital platforms
├── investments.json       # Investment account details linked to customers
├── loans.json             # Loan data linked to customers
├── transactions.json      # Financial transaction history linked to accounts
```
These datasets are now ready for use in the banking system’s data architecture.