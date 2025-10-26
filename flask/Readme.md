# Python Flask with mixed instrumentation


## Setup 

```bash
python3 -m venv venv
source .venv/bin/activate
```

## Run App

Run with local print:
```bash
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument \
    --traces_exporter console \
    --metrics_exporter console \
    --logs_exporter console \
    --service_name dice-server \
    flask run -p 8080
```

Run with otel collector:
```bash
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument \
    --traces_exporter otlp  \
    --metrics_exporter otlp \
    --logs_exporter otlp \
    --service_name dice-server \
    flask run -p 8080
```

## Run Telemetry Compose

```bash
podman-compose up 
```