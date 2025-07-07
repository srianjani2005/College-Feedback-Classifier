#  College Feedback Classifier

This project classifies student feedback into high-level categories such as Academics, Facilities, and Administration using foundation models from IBM watsonx.ai. It automates the process of analyzing qualitative feedback and enables educational institutions to make better, data-driven decisions.

---

##  Objectives

- Automatically classify open-ended student feedback into specific themes
- Reduce manual effort in sorting and analyzing large amounts of text data
- Generate structured outputs and reports for easier review
- Support decision-makers with accurate insights from student inputs

---

##  Tools & Technologies Used

| Category             | Tools / Technologies                            |
|----------------------|--------------------------------------------------|
| Programming Language | Python                                           |
| Libraries            | pandas, sklearn, IBM Watson Machine Learning SDK |
| AI Models            | FLAN-T5, Mistral (via IBM watsonx.ai)           |
| Platform             | IBM watsonx.ai                                   |
| Cloud Storage        | IBM Cloud Object Storage                         |
| IDE                  | Google Colab                                     |

---



##  Methodology

1. Data Preparation  
   - Feedback dataset collected in CSV format

2. Prompt Engineering (Few-shot learning)
   - Sample labeled feedbacks are shown to guide the AI model

3. Model Setup  
   - IBM watsonx.ai foundation models (FLAN-T5-XXL) initialized using project credentials

4. Feedback Classification  
   - Each feedback entry processed and categorized into Academics, Facilities, or Administration

5. Evaluation
   - Results reviewed against manually labeled data for validation

6. Export Results  
   - Final classified output saved to a CSV for reporting

---

##  Example Output

| Feedback                                      | Category       |
|----------------------------------------------|----------------|
| "Wi-Fi is too slow in the hostel."           | Facilities     |
| "Professors are always supportive and clear."| Academics      |
| "Fee payment portal was down again."         | Administration |

---

##  Features

- Zero manual sorting needed
- Fast classification using few-shot prompting
- Easily scalable and adaptable
- Output in clean, structured format (CSV)

---

##  Future Enhancements

- Add support for more categories like *Hostel, Mess, Transport*
- Integrate with a web dashboard for real-time viewing
- Include feedback sentiment analysis for deeper insights

---



##  Acknowledgements

- IBM watsonx.ai for providing free access to their powerful foundation models
- VIT-AP University for supporting innovation through real-world projects




