from src.Pipeline.Stages_of_Pipeline import DataIngestionPipeline
import os 

try:
    print("Enter the Data Ingeston")
    ingestion = DataIngestionPipeline()
    ingestion.main()
    print("-------------------------")
except Exception as e:
    raise e     
    
    