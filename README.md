# End-to-end-Machine-Learning-Project-with-MLflow


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml


# How to run?

### STEPS:

Clone the repository

...bash
https://github.com/tirunap/E-to-E-ML-Project-using-ML-Flow
...

### STEP 01- Create a conda environment after opening the respository

...bash
conda create -. mlproj python=(version)
...

### STEP 02 - install the requirements
...bash
pip install -r requirements.txt
...


...bash
#Finally run the following command
python app.py
...

Now,
...bash
open up your local host and port 

### STEP 03 - Run the application

'''bash
python app.py

### STEP 04 - Open your localhost and port (e.g., http://127.0.0.1:5000)



## ML Flow

[Documentation](FILE'S LINK)
'''bash
mlflow ui


##### cmd

### dagshub
[dagshub](https://dagshub.com)

MLFLOW_TRACKING_URI=https://dagshub.com/tirunap/E-to-E-ML-Project-using-ML-Flow.mlflow
MLFLOW_TRACKING_USERNAME=tirunap
MLFLOW_TRACKING_PASSWORD=23Jan@1995
python script.py

Run this to export as env variables 

**For Linux/Mac (bash):**
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/tirunap/E-to-E-ML-Project-using-ML-Flow.mlflow
export MLFLOW_TRACKING_USERNAME=tirunap
export MLFLOW_TRACKING_PASSWORD=23Jan@1995
```

**For Windows (PowerShell):**
```powershell
$env:MLFLOW_TRACKING_URI="https://dagshub.com/tirunap/E-to-E-ML-Project-using-ML-Flow.mlflow"
$env:MLFLOW_TRACKING_USERNAME="tirunap"
$env:MLFLOW_TRACKING_PASSWORD="23Jan@1995"
```




# AWS CI/CD Deployment with GitHub Actions

This repository demonstrates how to set up a **Continuous Integration (CI)** and **Continuous Deployment (CD)** pipeline using **GitHub Actions** and **Amazon Web Services (AWS)**.  
The pipeline automatically runs tests, builds a Docker image, pushes it to **Amazon ECR**, and deploys it to **Amazon ECS**


## 🚀 Workflow Overview

The GitHub Actions workflow (`.github/workflows/main.yaml`) is triggered on every push to the `main` branch. It performs the following steps:

1. **Checkout Code** – Pulls the latest code from GitHub.
2. **Set up Python** – Configures Python 3.8 environment.
3. **Install Dependencies** – Installs packages from `requirements.txt`.
4. **Run Tests** – Executes unit tests with `pytest`.
5. **Authenticate with AWS** – Uses GitHub Secrets for AWS credentials.
6. **Build & Push Docker Image** – Builds the project into a Docker image and pushes it to **Amazon ECR**.
7. **Deploy to ECS** – Updates the ECS service with the new image.

---

## 📂 Project Structure

.
├── src/                # Source code
├── tests/              # Unit tests
├── main.py             # Entry point (tokenization pipeline example)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker build instructions
└── .github/workflows/  # GitHub Actions workflows
└── main.yaml



---

## 🔑 Prerequisites

- **AWS Account** with ECS and ECR set up.
- **ECR Repository** created (035885606553.dkr.ecr.ap-south-1.amazonaws.com/mlproject).
- ** CREATE EC2 mschine(Ubuntu)
- ** Open EC2 and Install docker in EC2 Machine:
    - ### Optional
    'sudo apt-get update -y'
    'sudo apt-get upgrade'
    - ### Docker
    'curl -fsSL https://get.docker.com -o get-docker.sh'
    'sudo sh get.docker.sh
    'sudo usermod -aG docker ubuntu'
    'new grp docker'
    - ### Configure EC@ as self-hosted runner:
    setting-action-runner-new self hosted-choose os- then run command one by one
- **GitHub Secrets** configured:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION` - Asia Pacific (Mumbai)
  - `AWS_ECR_LOGIN_URI`- demo>> 
  - `AWS_REPOSITORY_NAME` - xxxxx
- **Dockerfile** at the root of the repo.
- **ECS Task Definition JSON** (`ecs-task-def.json`) describing how the container runs.

---

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>

2. Create a virtual environment and install dependencies:
    '''bash
    python -m venv .venv
    source .venv/bin/activate   # Linux/Mac
    .venv\Scripts\activate      # Windows
    pip install -r requirements.txt

3. Run locally:
    '''bash
    python main.py --text "Hello AWS CI/CD!"
    
4. Push changes to main branch:
    '''bash
    git add .
    git commit -m "Setup AWS CI/CD pipeline"
    git push origin main


# Deployment Flow
GitHub Actions builds and tests your code.

Docker image is created and pushed to Amazon ECR.

ECS service is updated with the new image.

Your application runs in AWS automatically.