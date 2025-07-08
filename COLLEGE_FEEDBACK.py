

# 1. Install Required Libraries (if running on Colab)
!pip install ibm-watson-machine-learning pandas scikit-learn --upgrade

# 2. Import Required Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from collections import Counter
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning import APIClient

# 3. IBM Cloud Credentials Setup (User Input)
api_key = input("Enter your IBM Cloud API Key: ")
project_id = input("Enter your IBM Cloud Project ID: ")

wml_credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": api_key
}

client = APIClient(wml_credentials)
client.set.default_project(project_id)

# 4. Load Feedback Dataset (CSV file)
df = pd.read_csv("/content/college_feedback.csv")  # Ensure the file path is correct
df.dropna(inplace=True)
print(df.head())

# 5. Split Data
X = df['feedback']
y = df['category']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Prepare Few-shot Examples
few_shot_examples = ""
categories = df['category'].unique()

for cat in categories:
    example = df[df['category'] == cat].iloc[0]['feedback']
    few_shot_examples += f"Feedback: {example}\nCategory: {cat}\n\n"

# 7. Initialize Foundation Model (FLAN-T5 or Mistral)
model_id = "google/flan-t5-xxl"
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 50,
    "stop_sequences": []
}

gen_model = Model(
    model_id=model_id,
    params=parameters,
    credentials=wml_credentials,
    project_id=project_id
)

# 8. Perform Classification
def classify_feedback(feedback_text):
    prompt = few_shot_examples + f"Feedback: {feedback_text}\nCategory:"
    try:
        result = gen_model.generate(prompt)
        if 'generated_text' in result:
            return result['generated_text'].strip()
        else:
            print("Missing 'generated_text' field:", result)
            return "Unknown"
    except Exception as e:
        print("Generation error:", str(e))
        return "Error"

# 9. Run Predictions on Test Set
y_pred = [classify_feedback(text) for text in X_test]

# 10. Evaluation
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# 11. Analyze Distribution
distribution = Counter(y_pred)
print("\nPredicted Category Distribution:", distribution)

# 12. Save Output
output_df = pd.DataFrame({'Feedback': X_test, 'Actual': y_test, 'Predicted': y_pred})
output_df.to_csv("classified_feedback_output.csv", index=False)
print("\nOutput saved to 'classified_feedback_output.csv'")