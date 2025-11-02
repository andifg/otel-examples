# """
# Logging configuration for the OpenTelemetry example application.
# """

# import logging

# def setup_logging(level: str = "INFO") -> None:
#     """
#     Set up logging configuration for the application.
    
#     Args:
#         level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
#     """
#     # Configure logging format
#     log_format = "%(name)s - %(levelname)s - %(message)s"
    
#     # Configure basic logging
#     logging.basicConfig(
#         level=getattr(logging, level.upper()),
#         format=log_format
#     )
    
#     logging.info(f"Logging configured with level: {level}")
