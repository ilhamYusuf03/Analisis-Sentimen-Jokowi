from preprocessing import preprocess_text
import joblib

vectorizer = joblib.load('vectorizer.pkl')
svm_model = joblib.load('model_svm.pkl')
lr_model = joblib load('model_logreg.pkl')
