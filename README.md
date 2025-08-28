# Webser Project (Azure DevOps + Docker + Python)

This project is a sample Python web application deployed using **Azure DevOps CI/CD pipelines**.  
It demonstrates containerization with **Docker** and automation with **Azure Pipelines**.

---

## 🚀 Features
- Python 3.12 based web application
- Unit testing with `unittest`
- CI/CD pipeline on Azure DevOps
- Docker image build & push to container registry
- Deployment-ready setup for Kubernetes / Docker

---

## 📂 Project Structure
├── app/ # Application source code
│ └── main.py # Sample Python app entry point
├── tests/ # Unit tests
│ └── test_dummy.py # Example test
├── Dockerfile # Docker image definition
├── requirements.txt # Python dependencies
└── azure-pipelines.yml # Azure DevOps pipeline definition


---

## 🛠️ Setup & Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/gaurav2311gehu/Webser-Project-Azure.git
   cd Webser-Project-Azure

2. Create virtual environment & install dependencies:
   python3 -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows

    pip install -r requirements.txt


3. Run the app: python app/main.py

4. Run tests: python -m unittest discover -s tests

🐳Docker

Build and run the application using Docker:
  docker build -t webser-app .
  docker run -p 5000:5000 webser-app

🔄 Azure DevOps Pipeline

Install dependencies in a virtual environment
Run unit tests
Build & push Docker image
(Optional) Deploy to AKS / Azure Web App

Pipeline is defined in azure-pipelines.yml
.

📌 Requirements

Python 3.12+
Docker
Azure DevOps account
GitHub repository

👨‍💻 Author
Gaurav Saini
