# Live Global Weather Analytics Tracker

A lightweight Python data pipeline that aggregates multi-city climate data by executing dynamic queries against a public REST API. The system performs real-time data ingestion, structural filtering, and matrix presentation inside a centralized terminal dashboard.

## Technical Architecture
The script operates as a highly optimized, automated data aggregation utility:
1. **Configuration Matrix:** Coordinates for diverse target locations are maintained inside a nested data configuration structure, enabling fast dimensional scaling.
2. **Dynamic Query Engineering:** Formatted string interpolation (`f-strings`) compiles targeted request queries on-the-fly, dynamically injecting geographic parameters into real-time API request buffers.
3. **Columnar Aggregation:** Raw JSON payloads are processed, mapped into uniform data dictionary frames, and compiled into a single unified `Pandas` DataFrame while suppressing indexing indicators for maximum reporting clarity.

## Core Tech Stack
* **Language:** Python 3.13+
* **Libraries:** Requests, Pandas

## How To Run Locally

### 1. Clone the Project Workspace
```bash
git clone [https://github.com/YOUR_USERNAME/live-data-api-pipeline.git](https://github.com/YOUR_USERNAME/live-data-api-pipeline.git)
cd live-data-api-pipeline