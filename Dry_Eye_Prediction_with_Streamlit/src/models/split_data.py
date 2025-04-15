from sklearn.model_selection import train_test_split
import pandas


def split_data(df,dry_eye_features,dry_eye_target):
    # Split data for Dry Eye Disease Prediction
    x_train_de, x_test_de, y_train_de, y_test_de = train_test_split(
    df[dry_eye_features], df[dry_eye_target], test_size=0.2, random_state=42, stratify=df[dry_eye_target])
    
    return x_train_de, x_test_de, y_train_de, y_test_de