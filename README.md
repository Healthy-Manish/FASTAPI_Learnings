# Insurance Premium Pridiction model

## Description
A full-stack Machine Learning web application that predicts ***Insurance Premium Category (Low / Medium / High)*** based on user health and lifestyle attributes.
The app is fully deployed on AWS and containerized using Docker for production-grade reliability.
# This application is build over streamlit to create frontend 

### 🧠 Project Overview
***Machine Learning–powered web application*** that predicts the Insurance Premium Category (Low / Medium / High) based on user health and lifestyle attributes.<br>
### The project includes:
  - A FastAPI backend for ML inference
  - A Streamlit frontend for user interaction
  - ### Full Docker containerization 
  - ### AWS EC2 deployment
  <br>
This application predicts the insurance premium category using the following features:
  - Age
  - Weight
  - Height
  - Income (LPA)
  - Smoking status
  - City
  - Occupation

<img src="insurance_premium/Screenshot from 2025-11-21 11-16-33.png"></img>
### The ML model returns:
  
  - predicted_category
  - confidence score
  - class_probabilities for each class

### The entire workflow is automated from model inference → FastAPI API → Streamlit UI.
## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Healthy-Manish/FASTAPI_Learnings.git
    cd insurance_premium
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r backend/requirements.txt
    ```

3. **Run the API at:**

    ```bash
    http://13.235.246.150:8000/predict
    ```
Opitional **Run  backend locally :**

    ```bash
      uvicorn app:app --reload --host 0.0.0.0 --port 8000
    ```
4. **Frontend--Streamlit :**

      ```bash
         streamlit run frontend.py
      ```

   
5. **Docker setup :**
    1. Install Docker
    2. Create account on Dockerhub

    - Step 1: Create Dockerfile
    - Step 2: Build the docker image
    ```bash
     docker build -t dockername/insurance-premium-api
    ```
    - step 4: docker login:
     ```bash
      docker login
    ```
    - Step 3: push image to dockerhub:
      ```bash
        docker push dockername/insurance-premium-api:latest
      ```
    - step 4: Run image locally:
    ```bash
      docker run -p 8000:8000 dockername/insurance-premium-api:latest
    ```
OPTIONAL **You can pull my image :**
     ```bash
        docker push healthymanish/insurance-premium-api:latest
    ```
6. **API request example :**
```json
  {
  "age": 30,
  "weight": 65,
  "height": 1.7,
  "income_lpa": 10.0,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```
7. **API response :**
```json
 {
  "predicted_category": "high",
  "confidence": 0.8432,
  "class_probabilities": {
    "high": 0.84,
    "medium": 0.15,
    "low": 0.01
  }
}

```
### 🛠 Tech Stack
Frontend: 
  - Streamlit
  - Python 3.11

Backend:
  - FastAPI
  - Uvicorn
  - Pydantic
  - Scikit-Learn

Deployment:
  - Docker
  - AWS EC2
  - NGINX (optional reverse proxy)
