from src.Pipeline.Stages_of_Pipeline import DataIngestionPipeline,DataValidationPipeline
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
    ingestion = DataValidationPipeline()
    ingestion.main()
    print("-------------------------")
except Exception as e:
    raise e  
    
    