# ScrapeChainService

**ScrapeChainService** is a Python application designed to automate the scraping of chain-related data from websites
using Selenium WebDriver. This service periodically performs web scraping tasks and saves the results in CSV format.

## Features

- **Web Scraping**: Uses Selenium WebDriver (Chrome) to interact with web pages and extract data.
- **Configurable Scheduling**: Supports various scheduling configurations to run scraping tasks at regular intervals or
  specific times.
- **CSV Export**: Saves the scraped data into CSV files for easy analysis and storage.
- **Docker Support**: Includes a Dockerfile for easy containerization and deployment.
- **Poetry for Dependency Management**: Uses Poetry for managing project dependencies, ensuring a clean and isolated
  environment.

## Configuration

The scheduling of scraping tasks can be customized using the `.env` file. You can set the following environment
variables:

- **CHAIN_SCHEDULE_INTERVAL**: Specifies the interval for recurring tasks. For example, `30d23h59m59s` or `5m`.
- **LOG_LEVEL**: The log level for the application. The default value is `INFO`.

## Installation

### Using Docker

1. **Build the Docker Image**:
   ```bash
   docker build -t defillama-scrape .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -it --rm defillama-scrape
   ```

### Without Docker

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/HELSSIUS/deffillama-scrape.git
   cd deffillama-scrape
   ```

2. **Install Dependencies**:
   ```bash
   poetry install
   ```

3. **Run the Application**:
   ```bash
   poetry run python src/main.py
   ```

## Usage

To start the service with custom configuration, you need to create a `.env` file in the root directory of your project.
Example configuration:

```env
# SCHEDULE_INTERVAL can be 30d23h59m59s
# if SCHEDULE_INTERVAL equals 100s it's same to 1m40s
CHAIN_SCHEDULE_INTERVAL=10s
# Log level
LOG_LEVEL=INFO
```

## CSV Output example
Output example: [chains.csv](docs/chains.csv)

```csv
Ethereum,1136,56813000000.000
Tron,34,8074000000.000
Solana,151,5095000000.000
BSC,779,4718000000.000
Arbitrum,672,3093000000.000
Base,323,1679000000.000
Blast,135,1138000000.000
Avalanche,394,907910000.00
Polygon,564,892630000.00
TON,19,760220000.00
```
