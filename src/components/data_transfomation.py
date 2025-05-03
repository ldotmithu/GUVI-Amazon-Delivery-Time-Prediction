from src.Config.config_entity import DataTransformConfig 
import os 
from src.Utility.common import Create_Folder,Read_yaml
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np
import joblib

schema_path = "schema.yaml" 

class DataTransform:
    def __init__(self):
        self.transform = DataTransformConfig()
        self.schema = Read_yaml(schema_path)
        Create_Folder(self.transform.root_dir)
    
    def preprocess_step(self):
        num_pipeline = Pipeline([
            ('num_pipeline',StandardScaler())
        ])    
        
        cat_pipeline = Pipeline([
            ('cat_pipeline',OneHotEncoder(handle_unknown='ignore'))
        ])
        
        preprocess = ColumnTransformer([
            ('num_pipeline',num_pipeline,self.schema['num-columns']),
            ('cat_pipeline',cat_pipeline,self.schema['cat-columns'])
        ])
        
        return preprocess
    
    def initiate_preprocess(self):
        data = pd.read_csv(self.transform.data_path)
        data.dropna(inplace=True)
        #remove negative value 
        data['Store_Latitude'] = data['Store_Latitude'].abs()
        data['Store_Longitude'] = data['Store_Longitude'].abs()
        # Convert date/time columns
        data['Order_DateTime'] = pd.to_datetime(data['Order_Date'] + ' ' + data['Order_Time'])
        data['Pickup_DateTime'] = pd.to_datetime(data['Order_Date'] + ' ' + data['Pickup_Time'])
        # Calculate time to pickup
        data['Time_to_Pickup'] = (data['Pickup_DateTime'] - data['Order_DateTime']).dt.total_seconds() / 60
        data['Order_Hour'] = data['Order_DateTime'].dt.hour
        data['Order_Day'] = data['Order_DateTime'].dt.day
        data['Order_Month'] = data['Order_DateTime'].dt.month
        data['Order_Weekday'] = data['Order_DateTime'].dt.weekday
        
        data.drop(columns=self.schema['drop-columns'],axis=1, inplace=True)
        
        preprocess_obj = self.preprocess_step()
        
        train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
        
        target_columns = self.schema.get('target',[])
        
        train_data_input_feature = train_data.drop(columns=target_columns, axis=1)
        train_data_target_feature = train_data[target_columns]
        
        test_data_input_feature = test_data.drop(columns = target_columns,axis = 1)
        test_data_target_feature = test_data[target_columns]
        
        train_pre = preprocess_obj.fit_transform(train_data_input_feature)
        test_pre = preprocess_obj.transform(test_data_input_feature)
        
        train_arr = np.c_[train_pre, np.array(train_data_target_feature)]
        test_arr = np.c_[test_pre, np.array(test_data_target_feature)]
        
        np.save(os.path.join(self.transform.root_dir,'train.npy'),train_arr)
        np.save(os.path.join(self.transform.root_dir,'test.npy'),test_arr)
        print("Train and test .npy files saved successfully.")
        
        joblib.dump(preprocess_obj,self.transform.preprocess_path)
        
        
            