#### Credit Card Analytical Data Contract

This project defines and validates the Credit Card Analytical Data contract, which provides aggregated insights into customer credit card usage. Below are instructions for linting and testing the data contract using the datacontract CLI.

Prerequisites:

Ensure you have the following installed:
* Python 3.11 or higher
* datacontract library installed in your virtual environment.

Activate your virtual environment:

```sh
source .venv/bin/activate
```

Lint the Data Contract

Lint the YAML file to check for syntax errors and ensure it adheres to the expected schema.

Command:
```sh
datacontract lint cc_analytical.yaml
```

Expected Output:
* If there are no errors, the output will indicate the YAML is valid.
* Example:

```sh
Linting cc_analytical.yaml
✅ Data contract linted successfully.
```

* If there are errors, the output will display the issues:

```sh
Linting cc_analytical.yaml
❌ Error: Missing required field 'location' in server configuration.
```


Test the Data Contract

Test the data contract to validate its configuration and verify data quality rules using the provided dataset.

Command:

```sh
datacontract test cc_analytical.yaml
```
Expected Output:
* The output will show the results of each test.
* Example:
```sh
Testing cc_analytical.yaml
✅ All tests passed successfully.
```

* If there are issues, the output will display error details:
```sh
Testing cc_analytical.yaml
❌ Data contract is invalid, found the following errors:
```
1) Test Data Contract: Missing required column 'credit_utilization_rate' in dataset.

Debugging

If you encounter errors, enable debug logging by adding the DEBUG environment variable:
```she
DEBUG=1 datacontract test cc_analytical.yaml
```

This will provide more detailed logs to help identify the root cause.

File Structure

* data/financial_services/datasets/credit_cards.json: Source dataset used to generate analytical data.
* demo/data-mesh/domain/analytical/credit_card_analytical_data.csv: Processed CSV file adhering to the data contract.
* cc_analytical.yaml: Data contract YAML definition.
* README.md: Documentation for the project.


Troubleshooting
* Error: argument of type 'NoneType' is not iterable
  * Ensure the location field in cc_analytical.yaml is correctly set to the path of your dataset file.
* CSV Format Errors
  * Check if the CSV file exists and matches the schema defined in the models section of cc_analytical.yaml.
