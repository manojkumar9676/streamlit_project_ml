# 🌸 Iris Flower Prediction App (Streamlit)

## 📌 Overview

This project is a simple Machine Learning web application built using **Streamlit** that predicts the species of an Iris flower based on user input features.

It demonstrates:

* Basic ML model training using Scikit-learn
* Interactive UI using Streamlit
* Real-time prediction

---

## 🚀 Features

* User-friendly web interface
* Input sliders for flower features
* Instant prediction of Iris species:

  * Setosa
  * Versicolor
  * Virginica
* Lightweight and fast

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* NumPy
* Pandas

---

## 📂 Project Structure

```
streamlit_project/
│
├── app.py               # Main Streamlit application
├── requirements.txt    # Dependencies
└── venv/               # Virtual environment (not uploaded to GitHub)
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/iris.git
cd iris
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open browser:

```
http://localhost:8501
```

---

## 📊 How It Works

* The model is trained using the built-in Iris dataset from Scikit-learn
* User inputs 4 features:

  * Sepal Length
  * Sepal Width
  * Petal Length
  * Petal Width
* Model predicts the flower species

---

## 📌 Future Improvements

* Save and load trained model (`.pkl`)
* Add prediction probability visualization
* Deploy on Streamlit Cloud
* Improve UI design

---

## 👤 Author

**B. Manoj Kumar**
ECE-A
Roll No: A23126512005

---

## ⭐ Note

This project is built for learning purposes and beginner-level ML deployment using Streamlit.
