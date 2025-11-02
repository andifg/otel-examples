import os
os.environ.setdefault("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4317")
os.environ.setdefault("OTEL_EXPORTER_OTLP_PROTOCOL", "grpc")
os.environ.setdefault("OTEL_SERVICE_NAME", "dice-roller-fastapi")
os.environ.setdefault("OTEL_TRACES_EXPORTER", "otlp")
os.environ.setdefault("OTEL_METRICS_EXPORTER", "otlp")
os.environ.setdefault("OTEL_LOGS_EXPORTER", "otlp")
os.environ.setdefault("OTEL_LOG_LEVEL", "DEBUG")
os.environ.setdefault("OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED", "true")

import logging
logging.basicConfig(level=logging.INFO)
import random
from contextlib import asynccontextmanager
# from otel_example.logging_config import setup_logging   
from opentelemetry import trace

# Workaround for uvicorn instrumentation
from opentelemetry.instrumentation.auto_instrumentation import initialize
initialize(swallow_exceptions=False)

from fastapi import FastAPI

tracer = trace.get_tracer("diceroller.tracer")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # setup_logging("INFO")
    logging.info("Loading the dice roller")
    yield
    logging.info("Cleaning up the dice roller and releasing the resources")

app = FastAPI(title="Dice Roller", version="1.0.0", lifespan=lifespan)

@app.get("/roll")
async def roll_dice():
    """Roll a single die and return a random number between 1 and 6."""
    logging.info("Test")
    with tracer.start_as_current_span("roll") as rollspan:
        result = random.randint(1, 6)
        logging.info(f"Dice rolled: {result}")
        rollspan.set_attribute("roll.value", result)
        return {"result": result}
