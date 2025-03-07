# logger_config.py
import logging
import os
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

def setup_logger():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    # Nombre del archivo con la fecha actual
    log_filename = os.path.join(log_dir, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

    # Configurar el logger
    logger = logging.getLogger("simpleExample")
    logger.setLevel(logging.DEBUG)

    # Configurar el handler para escribir en archivo, rotando diariamente
    file_handler = TimedRotatingFileHandler(log_filename, when="midnight", interval=1, backupCount=30, encoding="utf-8")
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

    # Agregar handler al logger
    logger.addHandler(file_handler)

    return logger
