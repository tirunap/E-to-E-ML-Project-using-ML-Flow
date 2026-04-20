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




## ML Flow

[Documentation](FILE'S LINK)


##### cmd

### dagshub
[dagshub](https://dagshub.com)

MLFLOW_TRACKING_URI=https://dagshub.com/tirunap/E-to-E-ML-Project-using-ML-Flow.mlflow
MLFLOW_TRACKING_USERNAME=tirunap
MLFLOW_TRACKING_PASSWORD=*******
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

