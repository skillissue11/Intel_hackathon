# Intel_hackathon

## Overview
The **Intel_hackathon** repository contains two main projects: the **Job Description Skill Extractor** and the **Employee Attrition Prediction Model**. Both tools leverage Python and natural language processing techniques to provide valuable insights for job seekers and organizations.

### Job Description Skill Extractor
The **Job Description Skill Extractor** is designed to analyze job descriptions and extract relevant skills associated with specific job titles. This project aims to help job seekers identify the key skills required for various roles, enhancing their understanding of job market demands.

### Employee Attrition Prediction Model
The **Employee Attrition Prediction Model** aims to predict employee attrition using a Random Forest Classifier. By analyzing various employee attributes, this model helps organizations identify employees at risk of leaving, enabling proactive measures to enhance employee retention.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Intel Optimizations with Scikit-learn](#usage)
- [Intel Optimizations with Transformers (T5 Model)](#model-training)
- [Conclusion](#model-prediction)


## Features
### Job Description Skill Extractor
- Extracts skills from job descriptions using natural language processing (NLP) techniques.
- Supports multiple job titles to enhance the relevance of extracted skills.
- Provides a user-friendly interface for inputting job descriptions and receiving skill output.

### Employee Attrition Prediction Model
- Data preprocessing and encoding of categorical variables.
- Model training using a Random Forest Classifier.
- Model saving and loading using joblib.
- Prediction of employee attrition based on new employee data.

## Technologies Used
- Python
- Pandas
- NumPy
- scikit-learn
- joblib
- Intel Extension for Scikit-learn

## Installation
To set up the projects, ensure you have Python and pip installed. Then, clone this repository and install the required packages:

```bash
git clone https://github.com/skillissue11/Intel_hackathon.git
cd Intel_hackathon
pip install pandas numpy scikit-learn joblib
```
The website extracts required skills from job titles and descriptions.
 It also predicts employee attrition based on the provided information.

![WhatsApp Image 2024-10-05 at 08 18 54_84a480e1](https://github.com/user-attachments/assets/bd868db9-088c-46b7-b09e-2318f2c1166b)
![WhatsApp Image 2024-10-05 at 08 19 07_d55f74ca](https://github.com/user-attachments/assets/24b55242-75a1-4d3b-b954-f743d434408f)

![WhatsApp Image 2024-10-05 at 08 20 12_591b9aae](https://github.com/user-attachments/assets/54800f45-4a47-43e7-807c-126ed91e20e5)
![WhatsApp Image 2024-10-05 at 08 20 34_fd75a5ab](https://github.com/user-attachments/assets/a20288c8-2afa-42f5-a5dc-142edde195e6)
![WhatsApp Image 2024-10-05 at 08 20 49_df934a9f](https://github.com/user-attachments/assets/73f949a5-2deb-4c22-9aab-5d12a5c766d0)

The graph illustrates the relationship between training loss and validation loss over multiple epochs.

![WhatsApp Image 2024-10-05 at 08 09 50_0592b9e0](https://github.com/user-attachments/assets/b56fcda0-1ffc-457f-8e47-75459b573db1)

## Intel Optimizations with Scikit-learn
This project integrates Intel's Extension for Scikit-learn, which significantly accelerates machine learning tasks by optimizing underlying algorithms. By incorporating the sklearnex library and using the patch_sklearn() function, we leverage Intel's advanced CPU optimizations without changing any of the core logic or APIs in scikit-learn.

In this implementation, Intel's optimizations improve the training speed and overall computational efficiency. The patching process works behind the scenes to accelerate scikit-learn's algorithms, especially beneficial for large-scale datasets like the IBM HR Analytics Employee Attrition Dataset. As seen in the code above, the model is trained using RandomForestClassifier, which now runs faster with Intel’s optimizations, allowing for quicker model iteration and validation.
![WhatsApp Image 2024-10-05 at 09 40 00_29618fdb](https://github.com/user-attachments/assets/1eae271a-1fd1-472e-ba61-23a1357a9b3f)


## Intel Optimizations with Transformers (T5 Model)
In this project, we leverage Intel's oneAPI and scikit-learn optimizations to enhance the performance of the T5 transformer model used for conditional generation tasks. By applying Intel’s patch_sklearn() function, the scikit-learn algorithms behind the scenes are optimized to run efficiently on Intel hardware. While the primary task involves the T5Tokenizer and T5ForConditionalGeneration from Hugging Face's Transformers library, Intel’s optimizations ensure smoother handling of data processing and training tasks within the overall pipeline.

Using the Intel® Extension for Scikit-learn, we speed up computations where applicable, especially when working with large datasets, without needing to modify the code for the transformer itself. The integration with oneAPI provides a seamless acceleration of the machine learning workflow, making the model more suitable for resource-intensive environments.

By utilizing these optimizations, we achieve enhanced performance without changing the core functionality of the T5 transformer.
![WhatsApp Image 2024-10-05 at 09 40 48_465054ca](https://github.com/user-attachments/assets/e4fcd316-3586-4022-bf48-1a62a668eb2c)


## Conclusion
This Employee Retention & Attrition Prediction system aims to:
- Leverage job data and employee metrics to forecast retention risks
- Provide actionable insights for HR decision-making
- Enable proactive retention strategies through data-driven predictions
- Enhance workforce stability and reduce unexpected turnover costs

By analyzing multiple factors, the system offers a holistic view of employee retention, empowering organizations to create targeted interventions and improve overall workforce management.

![WhatsApp Image 2024-10-04 at 22 46 40_bcaaa29c](https://github.com/user-attachments/assets/ead90ee4-9472-4434-a5ed-014501bb4d9a)

In real-life industrial sector applications, this system proves invaluable by:
- Reducing costly downtime associated with unexpected employee departures
- Maintaining continuity in specialized roles that require extensive training
- Optimizing resource allocation for employee development and retention programs
- Improving overall productivity by fostering a stable and experienced workforce
- Enhancing safety measures by retaining employees familiar with specific industrial processes and safety protocols

The predictive capabilities of this system align closely with the industrial sector's needs for operational efficiency, risk management, and long-term workforce planning. By anticipating potential attrition, companies can safeguard their human capital investments and maintain a competitive edge in talent retention.
