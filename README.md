## End to End Machine Learning Project

# Predictive Analysis of Student Performance *(Python, Scikit-learn, Flask, AWS, Azure, Docker, GitHub Actions, CI/CD Pipelines)*

## Problem Statement
The objective of this project was to develop a machine learning model to predict student performance in math, reading, and writing based on demographic and educational factors such as gender, race/ethnicity, parental education level, lunch type, and test preparation course.

## Key Contributions

- **Data Analysis & Feature Engineering:**  
  Conducted exploratory data analysis (EDA) to identify patterns and correlations, and engineered features to enhance model accuracy.  
  **Tools:** *Pandas, NumPy, Matplotlib, Seaborn*

- **Model Development & Evaluation:**  
  Built multiple machine learning models, including Random Forest, and fine-tuned them using cross-validation and hyperparameter tuning to optimize predictive performance.  
  **Tools:** *Scikit-learn, Random Forest, GridSearchCV*

- **Web Application & Cloud Deployment:**  
  Developed a Flask web application and a Streamlit dashboard for real-time predictions. Deployed the application to AWS and Azure, utilizing CI/CD pipelines and GitHub Actions for automated deployment and scaling.  
  **Tools:** *Flask, Streamlit, AWS (EC2, S3), Microsoft Azure, Docker, GitHub Actions*

- **Clean Code Practices:**  
  Ensured scalability and maintainability through modular programming and adherence to clean code principles.  
  **Practices:** *Modular Python, PEP8*

## Technologies Used

- **Programming Languages:** Python
- **Data Analysis & Visualization:** Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn, Random Forest, GridSearchCV
- **Web Frameworks:** Flask, Streamlit
- **Cloud Platforms:** AWS (EC2, S3), Microsoft Azure
- **CI/CD & Automation:** GitHub Actions, Docker, CI/CD Pipelines
- **Version Control:** Git, GitHub
- **Development Practices:** Modular Programming, Clean Code (PEP8)

## How to Run the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/Muhammadfarooq297/mlproject.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repository
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask web application:
    ```bash
    python app.py
    ```

5. Access the web application at `http://localhost:5000/` .

## Project Structure

- `app.py`: Flask application for serving the predictive model.
- `dashboard.py`: Streamlit dashboard for data visualization and predictions.
- `requirements.txt`: List of Python packages required to run the project.
- `data/`: Directory containing the dataset.
- `models/`: Saved models and related scripts.
- `notebooks/`: Jupyter notebooks for data analysis and model development.
- `static/` and `templates/`: Static files and HTML templates for the web app.



