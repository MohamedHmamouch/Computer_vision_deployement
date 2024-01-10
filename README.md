# Computer Vision Deployment
This project not only focuses on the aspects of data science and computer vision but also emphasizes deploying the solution through MLOP tools. The implementation includes utilizing DVC for managing data versions and MLflow for tracking experiments. The ultimate goal is to deploy the solution on a Streamlit web app.

# Source Data:
- The dataset originates from a Kaggle competition in computer vision. The images are not in DICOM format; instead, they are in JPG or PNG format to align with the model's requirements. The data encompass three types of chest cancer: Adenocarcinoma, Large cell carcinoma, and Squamous cell carcinoma, along with a folder for normal cells. The primary data folder contains subfolders for various stages, including test, train, and valid.

- Adenocarcinoma:
Lung adenocarcinoma is the most prevalent form of lung cancer, constituting 30 percent of all cases and around 40 percent of non-small cell lung cancer occurrences. Adenocarcinomas are commonly found in other cancers like breast, prostate, and colorectal. In the lung, they are situated in the outer region, in glands that secrete mucus and assist in breathing. Symptoms may include coughing, hoarseness, weight loss, and weakness.

#  Dagshub:
- Dagshub is a collaborative platform designed for managing and tracking machine learning experiments. It serves as a centralized hub where teams can collaborate on data science projects, version control their code, and seamlessly integrate with popular tools such as DVC and MLflow. With Dagshub, you can efficiently organize your experiments, share insights, and foster collaboration, making it an essential component in the machine learning lifecycle.

# MLflow:
- MLflow is an open-source platform that simplifies the end-to-end machine learning lifecycle. It provides tools for tracking experiments, packaging code into reproducible runs, and sharing and deploying models.

- DVC:


## MLFLOW
    
### cmd 
   - mlflow ui

### Dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/MohamedHmamouch/Computer_vision_deployement.mlflow \
MLFLOW_TRACKING_USERNAME=MohamedHmamouch \
MLFLOW_TRACKING_PASSWORD=200e4b749b0f8260522a65d396b66d9b385e1fd2 \

python script.py

    Run this to export as env variables:
    ```bash
    export MLFLOW_TRACKING_URI=https://dagshub.com/MohamedHmamouch/Computer_vision_deployement.mlflow

    export MLFLOW_TRACKING_USERNAME=MohamedHmamouch
    export 
    MLFLOW_TRACKING_PASSWORD=200e4b749b0f8260522a65d396b66d9b385e1fd2