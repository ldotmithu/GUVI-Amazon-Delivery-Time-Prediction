from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
import os 


class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        ingestion = DataIngestion()
        ingestion.download_zipfile()
        ingestion.unzip_operation()
        
class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        validation = DataValidation()
        validation.check_columns()
    