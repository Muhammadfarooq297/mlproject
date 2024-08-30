# End to End Machine Learning Project

## **Predictive Analysis of Student Performance**  

---

## 🎯 Problem Statement  
The goal of this project was to develop a machine learning model to **predict student performance** (in math, reading, and writing) based on demographic and educational factors such as gender, race/ethnicity, parental education level, lunch type, and test preparation course.

---

## 🚀 Key Contributions

### 🔍 Exploratory Data Analysis (EDA)
- Performed thorough data exploration to uncover patterns and relationships between demographic factors and student performance in **math**, **reading**, and **writing**. 📊
- Identified key trends such as the influence of **parental education** and the impact of **lunch type** on performance. 📈

### 🔧 Data Transformation & Feature Engineering
- Cleaned and transformed the raw dataset into meaningful features using **data pipelines**. 🔄
- Handled categorical variables (like **gender** and **race/ethnicity**) with encoding techniques and engineered features such as **test preparation impact** for better model performance. 🛠️

### 🤖 Model Development and Evaluation
- Built several **machine learning models**, including **linear regression**, **decision trees**, and **random forests** to predict student scores. 🔢
- Used **cross-validation** and **hyperparameter tuning** to evaluate models and optimize performance. ✔️

### 🌐 Web Application for Real-Time Predictions
- Developed a **Flask web app** to deliver real-time predictions based on input features (e.g., gender, race/ethnicity, parental education level). Users could obtain actionable insights into potential student outcomes. 🌍

### ☁️ Cloud Deployment to AWS & Azure
- **AWS Cloud with CI/CD Pipelines:** Deployed the predictive model and web app to **AWS**, ensuring scalability and automated updates through **CI/CD pipelines**. 🛠️🚀
- **Azure Cloud with GitHub Actions:** Seamlessly deployed the application to **Azure**, utilizing **GitHub Actions** for continuous integration and workflow automation. ⚙️☁️

### 🧹 Clean Code and Modular Programming
- Wrote **modular, clean code** following best practices, ensuring the solution was **scalable**, **maintainable**, and **extensible**. 🧑‍💻📦

---


## 🛠️ Technologies Used

- **Programming Languages:** Python 🐍
- **Data Analysis & Visualization:** `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`
- **Machine Learning:** `Scikit-learn`, `Random Forest`, `GridSearchCV`
- **Web Frameworks:** `Flask`, `Streamlit`
- **Cloud Platforms:** AWS (EC2, S3) ☁️, Azure ☁️
- **CI/CD & Automation:** `GitHub Actions`, `Docker`, `CI/CD Pipelines`
- **Version Control:** `Git`, `GitHub`
- **Development Practices:** Modular Programming, Clean Code (PEP8)
- **_Languages:_** Python 🐍  
- **_Frameworks & Tools:_** Flask 🌐, Scikit-learn 📊, AWS ☁️, Azure ☁️, Docker 🐳, GitHub Actions ⚙️, CI/CD Pipelines 🚀
---

## 📝 How to Run the Project

1. **Clone the repository:**  
    ```bash
    git clone https://github.com/Muhammadfarooq297/mlproject.git
    ```

2. **Navigate to the project directory:**  
    ```bash
    cd your-repository
    ```

3. **Install the required dependencies:**  
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask web application:**  
    ```bash
    python app.py
    ```

5. **Access the web application at:**  
    `http://localhost:5000/`

---

## 📁 Project Structure

- **`app.py`:** Flask application for serving the predictive model.
- **`dashboard.py`:** Streamlit dashboard for data visualization and predictions.
- **`requirements.txt`:** List of Python packages required to run the project.
- **`data/`:** Directory containing the dataset.
- **`models/`:** Saved models and related scripts.
- **`notebooks/`:** Jupyter notebooks for data analysis and model development.
- **`static/` & `templates/`:** Static files and HTML templates for the web app.

---

🎉 Feel free to explore the code and make improvements!