# Featureform API Server

This is a FastAPI server that provides HTTP endpoints to interact with Featureform for feature management and serving.

## Setup

1. Create and activate a virtual environment:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
python3 -m pip install --upgrade pip
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start Featureform using Docker Compose:
```bash
docker-compose up -d
```
This will start Featureform on `localhost:7878`

4. Create a `.env` file with your Featureform configuration:
```bash
FEATUREFORM_HOST=localhost
FEATUREFORM_PORT=7878
```

## Running the Server

Start the FastAPI server:
```bash
python main.py
```

The server will start on `http://localhost:8000`

## API Endpoints

1. Create Feature
   - POST `/features/`
   - Body: Feature definition with name, variant, type, entity, and source

2. Apply Feature
   - POST `/features/{name}/{variant}/apply`
   - Applies a feature definition

3. Serve Feature
   - GET `/features/{name}/{variant}/serve?entity_id={entity_id}`
   - Returns feature value for a given entity

4. List Features
   - GET `/features/`
   - Returns list of all registered features

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Stopping the Services

To stop Featureform:
```bash
docker-compose down
```

To stop the FastAPI server, press Ctrl+C in the terminal where it's running.

To deactivate the virtual environment when you're done:
```bash
deactivate
``` # feature-form-server
