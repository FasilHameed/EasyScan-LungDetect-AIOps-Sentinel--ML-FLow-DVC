from ChickenDisease import logger
from ChickenDisease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ChickenDisease.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline



Stage_name = " Stage Data Ingestion"
try:
    logger.info(f">>>>>>>>>>> stage {Stage_name} started     <<<<<<<<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> stage {Stage_name} completed   <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e