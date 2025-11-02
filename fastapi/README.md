# OpenTelemetry Example

A Python package demonstrating OpenTelemetry instrumentation with FastAPI.

## Prerequisites

- Python 3.13+
- uv package manager

## Installation

Install dependencies using uv:

```bash
uv sync
```

## Auto install telemetry packages with uv (this way they are not written to pyproject.toml but just installed within venv): 

```bash
uv run opentelemetry-bootstrap -a requirements | uv pip install --requirement -
```

## Auto instrumentation explained 

Within this application the auto instrumentation happens programatically
within the [dice_roller.py](./otel_example/dice_roller.py) so the startup
command stays the module call.


## Run application

Start external services
```bash
cd deployment && podman-compose up -d 
```
Run application
```bash
uv run python3 -m otel_example
```

Run application via uivicorn library 
```bash
uvicorn otel_example.dice_roller:app
```