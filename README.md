# Live Financial Data ETL Pipeline & Visualizer

A lightweight Python data pipeline that performs an automated **ETL (Extract, Transform, Load)** workflow to fetch, clean, and visualize real-time cryptocurrency asset metrics via a public REST API.

## Project Architecture
The script operates as a synchronized single-day automated reporting system:
1. **Data Ingestion (Extract):** Leverages the `requests` library to fetch live JSON market data from the CoinGecko REST API endpoint.
2. **Data Manipulation (Transform):** Utilizes `pandas` to filter out background noise, normalize high-precision floats, and structure data into a tabular vector schema.
3. **Analytical Reporting (Load):** Deploys `matplotlib` engines to render and export an automated statistical distribution bar chart.

## Core Tech Stack
* **Language:** Python 3.13
* **Libraries:** Requests, Pandas, Matplotlib

## How To Run Locally

### Prerequisites
Ensure you have Python installed on your local environment. 

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/live-data-api-pipeline.git](https://github.com/YOUR_USERNAME/live-data-api-pipeline.git)
cd live-data-api-pipeline