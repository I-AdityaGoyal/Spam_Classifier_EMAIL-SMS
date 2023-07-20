# Spam Classifier: EMAIL-SMS 📧🤖

<a href="https://gifyu.com/image/SWBtr"><img src="https://s12.gifyu.com/images/SWBtr.gif" alt="SWBtr.gif" border="0" /></a>

## Introduction

Welcome to the Spam Classifier: EMAIL-SMS repository! This project focuses on building a machine learning model that can accurately detect and classify spam messages in both emails and SMS/text messages. Spam messages are unsolicited and often irrelevant or inappropriate, causing annoyance and cluttering inboxes. The goal of this project is to develop an efficient spam classifier that can help users manage their communications effectively and reduce the impact of spam in their daily interactions.

## What is a Spam Classifier? 🔍🧠

A spam classifier is a machine learning model or algorithm designed to automatically detect and filter spam messages from legitimate ones. It analyzes the content and characteristics of incoming messages, such as emails or text messages, and assigns them a probability score of being spam or not. The classifier uses features like keywords, patterns, and sender information to distinguish between spam and non-spam messages, helping users identify and filter out unwanted messages.

## Files and Folders 📂🏷️

This repository contains the following files and folders:

- **Jupyter Notebook** 📓: This folder contains the main Jupyter Notebook file named `spam-classifier-sms-email.ipynb`. It includes the code, data analysis, model training, and evaluation for the spam classifier.

- **Streamlit Files** 🔬🔍: This folder contains the necessary files to deploy the spam classifier as a Streamlit web application. It includes:
    - `app.py`: The Python script for the Streamlit web application.
    - `model.pkl`: The trained machine learning model serialized using pickle.
    - `tfidf.pkl`: The TF-IDF vectorizer serialized using pickle.
    - `fun.pkl`: Other necessary function(s) serialized using pickle.

## Setup Instructions 🚀💻

To set up and use the Spam Classifier: EMAIL-SMS, follow these steps:

1. Clone this repository to your local machine using Git or download it as a ZIP file.
   
```bash
$ git clone https://github.com/I-AdityaGoyal/Spam_Classifier_EMAIL-SMS.git
```

2. Make sure you have Python and Jupyter Notebook installed on your system.

3. Navigate to the "Jupyter Notebook" folder and open the `spam-classifier-sms-email.ipynb` file using Jupyter Notebook.

```bash
$ cd /path/to/your_project/Jupyter\ Notebook/


$ jupyter notebook spam-classifier-sms-email.ipynb
```

4. Follow the instructions and run the cells in the notebook to reproduce the model training and evaluation process.

5. To use the Streamlit web application, navigate to the "Streamlit Files" folder.

```bash
$ cd /path/to/your_project/Streamlit\ Files/
```

6. Install the required Python packages by running the following command in your terminal or command prompt:

```bash
$ pip install -r requirements.txt
```

7. Once the required packages are installed, run the Streamlit application with the following command:

```bash
$ streamlit run app.py
```

8. The web application will be available in your browser at the provided URL (usually http://localhost:8501).

9. Upload a text message (email or SMS) to the web application and see the spam classifier in action!
    

<a href="https://ibb.co/wLdztd5"><img src="https://i.ibb.co/yRNQ2NH/Capture.png" alt="Capture" border="0"></a><br /><a target='_blank'></a><br />

## Contributions 💻📝🚀

Contributions to this project are welcome! If you have any suggestions, bug fixes, or enhancements, feel free to open an issue or submit a pull request.

