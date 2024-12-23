# Build the Docker image
docker build -t fastapi-small-model .

# Run the container
docker run -p 8000:8000 fastapi-small-model
