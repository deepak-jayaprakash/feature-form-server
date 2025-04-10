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

## Storage Layer

### PostgreSQL

To connect to the PostgreSQL database running inside Docker:

```bash
PGPASSWORD="password" psql -h localhost -p 5432 -U postgres -d postgres
```

#### Useful Commands

- List all tables: `\dt`
- Transformations are persisted as tables with names like: `featureform_transformation__average_user_transaction__2025-04-0`

#### Sample Transformations Data

```sql
SELECT * FROM "featureform_transformation__average_user_transaction__2025-04-0";
```

| user_id  | avg_transaction_amt |
|----------|---------------------|
| C2421688 | 650                 |

### Inference Store: Redis

To connect to Redis running inside Featureform Docker:

```bash
redis-cli -h 127.0.0.1 -p 6379
```

#### Sample Inference Data

List all keys:
```
keys *
```

Example output:
```
1) "{\"Prefix\":\"Featureform_table__\",\"Feature\":\"avg_transactions\",\"Variant\":\"quickstart\"}"
2) "Featureform_table____tables"
```

Get table metadata:
```
hgetall Featureform_table____tables
```

Example output:
```
1) "{\"Prefix\":\"Featureform_table__\",\"Feature\":\"avg_transactions\",\"Variant\":\"quickstart\"}"
2) "{\"ValueType\":\"float32\"}"
```

Get feature value for a specific user:
```
hget "{\"Prefix\":\"Featureform_table__\",\"Feature\":\"avg_transactions\",\"Variant\":\"quickstart\"}" "C8029825"
```

Example output:
```
"150"
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
