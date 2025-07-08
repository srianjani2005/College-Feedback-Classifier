#  College Feedback Classifier

The College Feedback Classifier is an AI-powered system that automatically classifies open-ended student feedback into categories like Academics, Facilities, and Administration using few-shot learning and IBM watsonx.ai foundation models (e.g., FLAN-T5).

##  Project Motivation

Manually reviewing and organizing student feedback is time-consuming and inconsistent. This project automates the classification process using large language models, allowing institutions to analyze feedback more effectively and take data-driven decisions.

---

##  Features

- Categorizes free-text feedback into predefined themes.
- Uses few-shot prompting for improved contextual classification.
- Connects with IBM watsonx.ai foundation models (FLAN-T5 / Mistral).
- Generates performance reports (precision, recall, F1-score).
- Exports classified results to a CSV file.

---

##  Tech Stack

| Category            | Tools / Technologies                          |
|---------------------|-----------------------------------------------|
| Programming Language| Python                                        |
| Libraries           | `pandas`, `sklearn`, `ibm-watson-machine-learning` |
| AI Models           | FLAN-T5 / Mistral                             |
| Platform            | IBM watsonx.ai                                |
| IDE                 | Google Colab                                  |
| Dataset Format      | CSV (with feedback and category columns)      |

---

##  How It Works

 1. Install Required Libraries
Install the necessary Python packages.




2. Load & Clean Dataset
Read student feedback from a CSV file and drop any rows with missing values.

3. Few-shot Prompt Construction
For each category, provide one sample feedback to guide the model.

4. Model Initialization
Connect to IBM watsonx.ai using your API key and Project ID.

5. Classification
Feed each test feedback into the model and collect its predicted category.

6. Evaluation & Report
Compare predictions with actual labels and print evaluation metrics.

7. Export Output
Save predictions to a CSV for further use or reporting.

 Sample Directory Structure

College-Feedback-Classifier/
│
├── classified_feedback_output.csv        # Output file
├── college_feedback.csv                  # Input dataset
├── college_feedback_classifier.py        # Python code
├── README.md                             # This file

 Example Few-shot Prompt

Feedback: The classrooms are clean and well-maintained.
Category: Facilities

Feedback: The syllabus is outdated and not very relevant.
Category: Academics

Feedback: The admin staff is unresponsive to emails.
Category: Administration


 Output
After running the model, the results are saved to:



To run this project, you need:

IBM Cloud account

API Key and Project ID from IBM Watson Machine Learning

Your dataset (college_feedback.csv) uploaded to Colab or available locally

Conclusion
This project streamlines feedback classification using modern AI techniques, enabling colleges to better understand student concerns and take actionable steps. Future work can include real-time dashboards, deeper analysis, or multilingual support.


