# AI DevOps Log Analyzer

A powerful tool to analyze logs from DevOps pipelines using AI techniques. This project helps in detecting errors, warnings, and performance bottlenecks automatically.

## Features

- Parse and analyze log files from multiple sources
- Detect errors, warnings, and anomalies
- Generate summarized reports
- AI-powered insights for faster debugging
- Configurable for custom log formats

## Project Structure

ai-devops-log-analyzer/
├── backend/ # Backend API and log analyzer scripts
│ ├── app/
│ │ ├── analyzer.py
│ │ ├── main.py
│ │ └── requirements.txt
│ └── Dockerfile
├── frontend/ # (Optional) Web dashboard for visualizing logs
├── github-actions.yml # CI/CD workflow
└── README.md


## Installation

1. Clone the repository:

```bash
git clone https://github.com/mohsin786-sudo/ai-devops-log-analyzer.git
cd ai-devops-log-analyzer


2. Create a virtual environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3.Install dependencies:

pip install -r backend/app/requirements.txt

Run the backend analyzer:

cd backend/app
python main.py

Build and run using Docker:

docker build -t ai-log-analyzer .
docker run -p 8000:8000 ai-log-analyzer
