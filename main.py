import os
from CnnClassifier import logger
from CnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline

Stage_Name="Data Ingestion stage"

try:
        logger.info(f">>>>>>>>>>>> stage {Stage_Name} started<<<<<<<<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {Stage_Name} completed<<<<<<<<")

except Exception as e:

        logger.exception(e)

        raise e


Stage_Name="Prepare Base Model"

try:
        logger.info(f">>>>>>>>>>>> stage {Stage_Name} started<<<<<<<<<<<<<")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()

        logger.info(f">>>>>>>>>>> stage {Stage_Name} completed<<<<<<<<")

except Exception as e:

        logger.exception(e)

        raise e


Stage_Name="Training"
try:
        logger.info(f">>>>>>>>>>>> stage {Stage_Name} started<<<<<<<<<<<<<")
        obj=ModelTrainingPipeline()
        obj.main()

        logger.info(f">>>>>>>>>>> stage {Stage_Name} completed<<<<<<<<")

except Exception as e:

        logger.exception(e)

        raise e
