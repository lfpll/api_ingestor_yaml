# PoC API ingestion through yaml


Context:


In the data-driven era, one of the most routine tasks performed by data engineering teams is setting up and maintaining data ingestion pipelines. This involves API calls and managing the relationships between parent and child endpoints. For instance, if an API retrieves organization data, subsequent child API calls might be necessary to fetch detailed data about users within each organization.

In the current scenario, when a new API needs to be ingested, data engineers are required to manually write, test, and deploy new code. This process can be time-consuming, error-prone, and act as a bottleneck to the data acquisition process.

We aim to simplify and automate this process by developing an API data ingestion tool. This tool will abstract the complexities of the API data ingestion process and allow non-engineers to add and configure new APIs for ingestion by simply providing a user-friendly YAML configuration file. This file will contain details such as the API endpoints, authentication details, rate limits, child endpoints, and response schemas.

Features of the API Data Ingestion Tool will include:

Centralized Configuration: Consolidate all API ingestion configurations into a single place.
User-Friendly Interface: Enable non-engineers to easily add and configure API ingestions using a YAML configuration file.
Dynamic Child-Parent API Relationships: Configure child API calls which depend on parent API calls, accommodating complex data retrieval processes.
Schema Validation: Validate API responses against predefined schemas to ensure data quality and consistency.
Efficient Data Ingestion: Save API data into BigQuery in batches for efficient data storage and analysis.
The development of this tool will minimize the need for engineering intervention during the API data ingestion process, reducing development time, and allowing for a faster, more dynamic response to data acquisition needs.


What this aim to solve:
- No common code share through api ingestors
    - Both singer taps and airbyte have this issue
- Componetize modules for auth, requests, configs, ...
- One single place to maintain related to code
- Global optimizations since the APIs ingestions will share the same code.
