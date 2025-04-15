# Import accuracy score
from sklearn.metrics import accuracy_score, confusion_matrix

#  Function to predict and evaluate
def evaluate_model(model, x_test_de,  y_test_de):
    # Predict the loan eligibility on the testing set
    y_pred_rf_de = model.predict(x_test_de)

    # Calculate the accuracy score
    accuracy = accuracy_score(y_test_de, y_pred_rf_de)

    # Calculate the confusion matrix
    confusion_mat = confusion_matrix(y_test_de, y_pred_rf_de)

    return accuracy, confusion_mat