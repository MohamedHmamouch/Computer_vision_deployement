import os
from CnnClassifier import logger
from CnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

Stage_Name="Data Ingestion stage"

try:
        logger.info(f">>>>>>>>>>>> stage {Stage_Name} started<<<<<<<<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {Stage_Name} completed<<<<<<<<")

except Exception as e:

        logger.exception(e)

        raise e