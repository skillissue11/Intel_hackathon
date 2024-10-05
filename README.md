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
- [Usage](#usage)
- [Model Training](#model-training)
- [Model Prediction](#model-prediction)
- [Dataset](#dataset)
- [Results](#results)
- [License](#license)

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
