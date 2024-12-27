# from textSummarizer.logging import logger

# logger.info("welcome to our custom log")

from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from textSummarizer.logging import logger

# data ingestion stage

STAGE_NAME = "Data Ingestion Sateg"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e