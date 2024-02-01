# Streamlit AWS Cognito Integration Example

## Overview

This project demonstrates the integration of Streamlit, a Python framework for building web applications, with AWS Cognito, a fully managed identity service provided by Amazon Web Services (AWS). By combining these technologies, this example app showcases a seamless and secure user authentication and authorization system.

## Features

- **User Authentication:** Leverage AWS Cognito to enable secure user sign-up, sign-in, and account management.
  
- **Streamlit Web Application:** Build a responsive and interactive web application using Streamlit, providing a user-friendly interface.

- **Protected Routes:** Implement authentication checks to restrict access to certain routes and ensure a secure user experience.

## Requirements

- Python 3.x
- Streamlit 1.30.0
- AWS Account with Cognito User Pool set up

## Getting Started

1.  **Install dependencies**
```bash
cd streamlit-aws-cognito
pip install -r requirements.txt
```

2.  **Configure AWS Cognito**
Set up a User Pool in your AWS Console.
Create .env file in **components** folder and add your AWS Cognito credentials.
```bash
COGNITO_DOMAIN = "https://xxx.auth.eu-north-1.amazoncognito.com"
CLIENT_ID = "xxx"
CLIENT_SECRET = "xxx"
APP_URI = "http://localhost:8501/"
```

3.  **Run the Streamlit app**
```bash
streamlit run app.py
```
Access the app in your browser:
Open http://localhost:8501 in your web browser.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

Copyright © 2024 [João Silva](https://github.com/jptsantossilva)




