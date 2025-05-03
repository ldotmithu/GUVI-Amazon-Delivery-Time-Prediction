# 🚚 Amazon Delivery Time Prediction ⏱️

A machine learning project to predict Amazon delivery times with 78% accuracy based on various factors like agent details, location, weather conditions, and more.

---

## ✨ Key Features

- **🔁 End-to-End ML Pipeline**: Data ingestion → validation → transformation → training → evaluation
- **🖥️ Interactive Web App**: Beautiful Streamlit interface with real-time predictions
- **⚡ XGBoost Model**: High-performance regression model (R²: 0.78)
- **🔄 One-Click Retraining**: Automated pipeline with progress tracking

---

## 🛠️ Installation Guide

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ldotmithu/GUVI-Amazon-Delivery-Time-Prediction.git
   cd GUVI-Amazon-Delivery-Time-Prediction

2. Create and activate a virtual environment:
   ```bash 
   conda create -n ml_project python=3.10 -y  
   conda activate ml_project
   ```
3. Install dependencies:
   ```bash 
   pip install -r requirements.txt
   ``` 
4. 🏗️ Project Structure

    ```bash
    📦 GUVI-Amazon-Delivery-Time-Prediction
├── 📂 artifacts/               # Pipeline outputs
├── 📂 src/
│   ├── 📂 Config/              # Configuration classes
│   ├── 📂 Pipeline/            # Pipeline stages
│   ├── 📂 Utility/             # Helper functions
│   └── 📂 components/          # Pipeline components
├── 📜 app.py                   # 🖥️ Streamlit app
├── 📜 main.py                  # ⚙️ Main pipeline
├── ⚙️ params.yaml              # Model parameters
├── 📐 schema.yaml              # Data schema
└── 📝 requirements.txt         # Dependencies

    ```  

5. 🖥️ Usage
   Run the Streamlit App:
   ```bash
    streamlit run app.py
   ```    
   ### The app provides two main functionalities:

    **Model Training:**
    - Click "Run Full Training Pipeline" to execute all pipeline stages

    **Delivery Time Prediction:**

    - Fill in delivery details in the sidebar

    - Click "Predict Delivery Time" to get estimated delivery time

    **Run Pipeline Directly:**
    ```bash
    python main.py
    ```
6. 📊 Model Performance
    - *The model provides the following metrics (example values):*
        ```bash 
        RMSE: 23.86764682160196 minutes
        MAE: 18.66434552778323 minutes
        R² Score: 0.7833827610591204

        ```  
---        
### 👨‍💻 Contributor: 

    L. Mithurshan 
---

## 📜 License
    This project is licensed under the **Apache-2.0 license**.
---

## **Glance of the Project**

![image](https://github.com/ldotmithu/Dataset/blob/main/Screenshot%202025-05-03%20180829.png)
---

Happy coding! 😊        

  
