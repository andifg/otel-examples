import os
os.environ.setdefault("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4317")
os.environ.setdefault("OTEL_EXPORTER_OTLP_PROTOCOL", "grpc")
os.environ.setdefault("OTEL_SERVICE_NAME", "dice-roller-fastapi")
os.environ.setdefault("OTEL_TRACES_EXPORTER", "otlp")
os.environ.setdefault("OTEL_METRICS_EXPORTER", "otlp")
os.environ.setdefault("OTEL_LOGS_EXPORTER", "otlp,console")
os.environ.setdefault("OTEL_LOG_LEVEL", "DEBUG")
os.environ.setdefault("OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED", "TRUE")
import uvicorn
from otel_example.dice_roller import app



def main():
    uvicorn.run("otel_example.dice_roller:app", host="0.0.0.0", port=8000, reload=False, use_colors=True, workers=1)
