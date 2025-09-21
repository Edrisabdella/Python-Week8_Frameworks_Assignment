# Frameworks Assignment – CORD-19 Data Explorer  

This project explores the **CORD-19 dataset** (`metadata.csv`) and creates a simple **Streamlit application** to visualize COVID-19 research insights.  

---

## 📌 Features
- Load and clean CORD-19 metadata  
- Basic data exploration (missing values, statistics, types)  
- Data visualizations:  
  - Publications by year  
  - Top publishing journals  
  - Word cloud of paper titles  
  - Distribution by source  
- Interactive **Streamlit app** with filters and charts  

---

## 🛠️ Tools Used
- pandas==1.5.3
- matplotlib==3.7.0
- seaborn==0.12.2
- streamlit==1.22.0
- wordcloud==1.9.2
- numpy==1.24.2 

---

## 📂 Project Structure
```
Frameworks_Assignment/
│
├── README.md          # Documentation
├── requirements.txt   # Dependencies
├── notebook.ipynb     # Jupyter Notebook with analysis
├── app.py             # Streamlit web app
├── screenshots/       # Example output screenshots
└── data/
    └── metadata.csv   # Place dataset here (not included in repo)
```

---

## ⚡ Installation
1. Clone this repo:
   ```bash
   git clone https://github.com/<your-username>/Frameworks_Assignment.git
   cd Frameworks_Assignment
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add the dataset:
   - Download `metadata.csv` from Kaggle ([CORD-19 Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge))  
   - Place it inside the `data/` folder.  

---

## ▶️ Usage

### Run Jupyter Notebook
```bash
jupyter notebook notebook.ipynb
```

### Run Streamlit App
```bash
streamlit run app.py
```

## Project Structure text

- `cord19_analysis.py`: Script for data loading, cleaning, analysis, and visualization
- `app.py`: Streamlit application for interactive data exploration
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation

## Features

- Data loading and cleaning
- Basic exploratory data analysis
- Visualizations including bar charts, histograms, and word clouds
- Interactive Streamlit app with filters for year and journal
- Metrics and insights about the dataset

## Results

The analysis reveals patterns in COVID-19 research publications, including:
- Trends in publication volume over time
- Most prolific journals in COVID-19 research
- Common words in paper titles
- Distribution of abstract lengths

---

## 📊 Example Results & Screenshots  

### Publications by Year
![Publications by Year](screenshots/publications_by_year.png)

### Top Journals
![Top Journals](screenshots/top_journals.png)

### Word Cloud of Paper Titles
![Word Cloud](screenshots/wordcloud.png)

### Streamlit App
![Streamlit App](screenshots/streamlit_app.png)

> 📌 *Note:* Save your charts or app screenshots inside a folder named `screenshots/` and they will appear here automatically.  

---

## 📝 Reflection
- **Challenges:** Handling missing values, working with a large dataset, ensuring Streamlit runs smoothly.  
- **Learning Outcomes:** Improved data cleaning skills, gained experience with visualizations, and created a functional interactive dashboard.  

---
