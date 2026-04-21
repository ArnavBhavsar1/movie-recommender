# 🎬 Movie Recommendation System (Streamlit + ML)

An interactive Movie Recommendation System built using **Machine Learning** and **Streamlit**, which suggests similar movies based on user input. The app uses **content-based filtering** and optionally displays **movie posters**.

---

## 🚀 Features

* 🎥 Select a movie from dropdown
* 🎯 Get top 5 similar movie recommendations
* ⚡ Fast performance using caching
* 🧠 Content-based recommendation system
* 🖼 Displays movie posters (via TMDB API or placeholders)
* 💻 Interactive UI using Streamlit

---

## 🛠 Tech Stack

* **Python**
* **Pandas**
* **scikit-learn**
* **Streamlit**
* **TMDB API (optional for posters)**

---

## 📁 Project Structure

```id="z3k8lm"
movie_recommender/
│── app.py                     # Streamlit UI
│── main.py (optional)         # Backend testing script
│── tmdb_5000_movies.csv      # Dataset
│── tmdb_5000_credits.csv     # Dataset
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash id="1kd9zv"
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash id="8sd7xq"
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash id="0o8f9x"
pip install -r requirements.txt
```

---

### 4️⃣ Add Dataset

Download dataset from Kaggle:
👉 TMDB 5000 Movie Dataset

Place files in project folder:

```id="u3l8nm"
tmdb_5000_movies.csv
tmdb_5000_credits.csv
```

---

### 5️⃣ Run the App

```bash id="4ksl2q"
streamlit run app.py
```

---

## 💡 How It Works

1. Load movie dataset
2. Extract important features:

   * Genres
   * Keywords
   * Cast
   * Director
3. Combine features into a single text column (**tags**)
4. Convert text → numerical vectors using **CountVectorizer**
5. Compute similarity using **cosine similarity**
6. Recommend movies with highest similarity score

---

## 🧠 Machine Learning Concept

This project uses:

* **Content-Based Filtering**
* **Bag of Words (BoW)**
* **Cosine Similarity**

---

## 🎯 Example Output

Input:

```
Avatar
```

Output:

```
Guardians of the Galaxy  
John Carter  
Star Trek  
Aliens vs Predator  
Independence Day  
```

---

## 🖼 Posters (Optional)

You can enable movie posters using:

* TMDB API
* Dummy placeholders
* Local images

---

## 🔥 Future Improvements

* 🎬 Add movie posters using API
* ⭐ Show ratings and genres
* 🔍 Add search functionality
* 🌐 Deploy on Streamlit Cloud
* 📱 Improve UI design

---

## 📌 Resume Highlight

> Built an interactive Movie Recommendation System using Machine Learning and Streamlit, leveraging cosine similarity to suggest movies and integrating API-based poster display.

---

## ⚠️ Important Notes

* Dataset must be placed correctly
* First run may take time (data processing)
* Use caching for better performance


