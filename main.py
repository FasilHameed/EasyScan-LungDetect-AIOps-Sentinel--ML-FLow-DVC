from ChickenDisease import logger
from ChickenDisease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


Stage_name = " Stage Data Ingestion"
try:
    logger.info(f">>>>>>>>>>> stage {Stage_name} started     <<<<<<<<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {Stage_name} completed   <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e