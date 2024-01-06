from CnnClassifier.config.configuration import ConfigurationManager
from CnnClassifier.components.model_evaluation_mlflow import Evaluation
from CnnClassifier import logger

Stage_Name="Evaluation Stage"

class EvaluationPipeline:

    def __init__(self):
        pass


    def main(self):

        config=ConfigurationManager()
        eval_config=config.get_evaluation_config()
        evaluation=Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()



if __name__ =="__main__":

    try:
        logger.info(f">>>>>>>>>>>> stage {Stage_Name} started<<<<<<<<<<<<<")
        obj=EvaluationPipeline()
        obj.main()

        logger.info(f">>>>>>>>>>> stage {Stage_Name} completed<<<<<<<<")

    except Exception as e:

        logger.exception(e)

        raise e