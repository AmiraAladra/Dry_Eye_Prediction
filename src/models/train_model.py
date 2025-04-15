from sklearn.ensemble import RandomForestClassifier
import pickle

# Function to train the model
def train_RFmodel(x_train_de, y_train_de):
    
    # Random Forest for Dry Eye
    rf_de = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    rf_de.fit(x_train_de, y_train_de)
    
    # Save the trained model as a pickle file
    with open("models/rf_de.pkl", "wb") as model_file:
        pickle.dump(rf_de, model_file) 

    return rf_de
