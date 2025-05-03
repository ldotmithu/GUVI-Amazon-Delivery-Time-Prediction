from src.Config.config_entity import ModelEvaluationConfig
from src.Utility.common import Create_Folder,eval_metrics,save_json
import os 
import numpy as np 
import joblib


class ModelEvaluation:
    def __init__(self):
        self.evaluation = ModelEvaluationConfig()
        
        Create_Folder(self.evaluation.root_dir)
    
    def model_evaluation(self):
        test_data = np.load(self.evaluation.test_data)
        
        test_X = test_data[:,:-1]
        test_y = test_data[:,-1]
        
        model = joblib.load(self.evaluation.model_path)
        predicted_qualitie = model.predict(test_X)
        
        (rmse, mae, r2) = eval_metrics(test_y, predicted_qualitie)
        scores = {"rmse": rmse, "mae": mae, "r2": r2}
        
        save_json(os.path.join(self.evaluation.root_dir,self.evaluation.metrics_path),data=scores)
        
        
        
        