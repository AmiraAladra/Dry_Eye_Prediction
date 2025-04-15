
from src.data.make_dataset import load_data
from src.features.build_features import features_engineering
from src.models.train_model import train_RFmodel
from src.models.predict_model import evaluate_model
from src.models.split_data import split_data

if __name__ == "__main__":
   try:
      
      # Load and preprocess the data
      data_path = "data/raw/Dry_Eye_Dataset_Phase1.csv"
      df = load_data(data_path)
      
      if df is None or df.empty:
               raise ValueError("Error: The dataset could not be loaded or is empty.")

      # Create dummy variables and separate features and target
      df_cleaned = features_engineering(df)
      
      if df_cleaned is None or df_cleaned.empty:
               raise ValueError("Error: Data preprocessing failed or resulted in an empty dataset.")
            
      dry_eye_features = ['Smart device before bed', 'Discomfort Eye-strain', 'Redness in eye',
         'Itchiness/Irritation in eye', 'Gender_F', 'Gender_M', 'Stress level_1',
         'Stress level_2', 'Stress level_3','Stress level_4', 'Stress level_5']
      
      # Define target variable
      dry_eye_target = 'Dry Eye Disease'
      
      
      x_train_de, x_test_de, y_train_de, y_test_de = split_data(df_cleaned,dry_eye_features,dry_eye_target)

      # Train the Random Forest Classifier model
      model= train_RFmodel(x_train_de, y_train_de)

      # Evaluate the model
      accuracy, confusion_mat = evaluate_model(model, x_test_de,  y_test_de)
      print(f"Accuracy: {accuracy}")
      print(f"Confusion Matrix:\n{confusion_mat}")
   
   except FileNotFoundError as e:
        print(f"File Error: {e}")
   except ValueError as e:
        print(f"Value Error: {e}")
   except Exception as e:
        print(f"An unexpected error occurred: {e}")
