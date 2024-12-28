# from textSummarizer.logging import logger

# logger.info("welcome to our custom log")

from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# importing data validation training pipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

from textSummarizer.logging import logger

# data ingestion stage

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# data validation stage

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e