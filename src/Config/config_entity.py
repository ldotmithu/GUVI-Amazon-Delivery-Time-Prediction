from dataclasses import dataclass
import os 
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir :Path = "artifacts/data_ingestion"
    URL:str="https://github.com/ldotmithu/Dataset/raw/refs/heads/main/amazon_delivery.zip"
    local_data_path:Path = "artifacts/data_ingestion/data.zip"
    unzip_dir :Path = "artifacts/data_ingestion"
    
@dataclass
class DataValidationConfig:
    root_dir:Path = "artifacts/data_validation"
    data_path:Path = "artifacts/data_ingestion/amazon_delivery.csv"
    status_path:Path = "status.txt"
    