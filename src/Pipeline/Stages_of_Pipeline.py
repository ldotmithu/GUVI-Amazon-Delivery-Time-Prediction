from src.components.data_ingestion import DataIngestion
import os 


class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        ingestion = DataIngestion()
        ingestion.download_zipfile()
        ingestion.unzip_operation()