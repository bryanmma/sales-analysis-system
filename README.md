# Sales Analysis System

Automated system for sales data analysis, statistical reporting, and visualization using **Python (Pandas, Matplotlib, MySQL Connector)** and **MySQL**.

## Overview
This project is a comprehensive tool designed to process, analyze, and visualize sales data. It automates the generation of statistical reports and creates data-driven visualizations to support decision-making. 

*Note: This system was originally developed for use within a Peruvian context. As a result, some labels, currency formats (S/.), and data categories appear in Spanish.*

## Features
- **Secure Configuration:** Uses environment variables (.env) for database credential management.
- **Data Analysis:** Calculates total revenue, units sold, top-performing products, and sales distribution by payment method and type.
- **Automated Reporting:** Generates clean CSV exports for all analytical insights.
- **Data Visualization:** Automatically creates and saves professional-grade charts (bar, line, horizontal bars) using Matplotlib.

## Prerequisites
To run this project, you need to have **Python** installed and the following dependencies:

```bash
pip install pandas mysql-connector-python matplotlib python-dotenv
```

## Setup
1. Create a `.env` file in the root directory.
2. Add your database credentials in the `.env` file:

```text
DB_HOST=127.0.0.1
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database_name
```

## Usage
Run the main script to generate reports and graphics:

```bash
python main.py
```

## Project Structure
- `main.py`: Main entry point and orchestration.
- `analisis.py`: Data processing logic.
- `graficos.py`: Visualization engine.
- `reportes.py`: Exporting logic for CSV files.
- `conexion.py`: Database connection handling.
- `utils.py`: Console formatting and output management.
