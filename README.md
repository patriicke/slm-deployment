# Deploy Smart, Not Large: Small Language Model Deployment

This repository demonstrates how to deploy a **Small Language Model (SML)** for tasks like sentiment analysis using **FastAPI**. You can choose between deploying with Docker or using a Python virtual environment.

## Features

- **FastAPI** for quick and efficient API creation.
- **Small Language Model** using Hugging Face's `distilbert-base-uncased-finetuned-sst-2-english` for sentiment analysis.
- **Docker** setup for easy deployment.
- **Optional venv** setup for those not using Docker.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/patriicke/slm-deployment.git
cd sml-deployment
```

### 2. Choose Your Deployment Method

#### Option 1: Docker Deployment

1. Build the Docker image:

   ```bash
   sh run-docker.sh
   ```

2. Access the API at:

   ```url
   http://localhost:8000
   ```

#### Option 2: Virtual Environment Deployment

1. Create a Python virtual environment:

   ```bash
   ./run-venv.sh
   ```

2. Access the API at:

   ```url
   http://localhost:8000
   ```

---

## Testing the API

### Curl

```bash
curl -X POST -H "Content-Type: application/json" \
    -d '{"text": ["I love this!", "This is awful."]}' \
    http://localhost:8000/predict/
```

Expected Response:

```json
{
    "predictions": [
        {"label": "POSITIVE", "score": 0.9998},
        {"label": "NEGATIVE", "score": 0.9986}
    ]
}
```

### Swagger UI

Visit `http://localhost:8000/docs` to test the API graphically using the auto-generated Swagger documentation.

---

## Repository Structure

```folder
.
├── app.py             # FastAPI application
├── Dockerfile         # Docker setup
├── requirements.txt   # Python dependencies
├── run-docker.sh      # Docker deployment script
├── run-venv.sh        # Venv setup and run script
├── .gitignore         # Avoid pushing unnecessary files
```

---

## License

This project is for study purposes. Feel free to use it anywhere.

---

**Enjoyed this project?** Feel free to star the repo, submit an issue, or reach out with suggestions!
