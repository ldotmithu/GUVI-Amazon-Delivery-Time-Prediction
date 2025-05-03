from src.Pipeline.Stages_of_Pipeline import (DataIngestionPipeline,DataValidationPipeline,DataTransformPipeline,
                                             ModelTrainPipeline,ModelEvaluationPipeline)
import os 

try:
    print("Enter the Data Ingeston")
    ingestion = DataIngestionPipeline()
    ingestion.main()
    print("-------------------------")
except Exception as e:
    raise e     


try:
    print("Enter the Data Validation")
    validation = DataValidationPipeline()
    validation.main()
    print("-------------------------")
except Exception as e:
    raise e  

try:
    print("Enter the Data Transform")
    transform = DataTransformPipeline()
    transform.main()
    print("-------------------------")
except Exception as e:
    raise e  

try:
    print("Enter the Model Trainer")
    train = ModelTrainPipeline()
    train.main()
    print("-------------------------")
except Exception as e:
    raise e 

try:
    print("Enter the Model Evaluation")
    evaluation = ModelEvaluationPipeline()
    evaluation.main()
    print("-------------------------")
except Exception as e:
    raise e 
    
    