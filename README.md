
  This project performs exploratory data analysis (EDA) on a movie dataset using Python.
  It focuses on cleaning, transforming, and analyzing movie-related data such as genres,
  release dates, and user engagement metrics. The goal is to uncover useful patterns
  across genres, years, and numerical features using visualizations and feature engineering.


---

## 📌 Project Overview

This notebook focuses on understanding movie trends and behaviors through:

- Data loading and preprocessing using `pandas`
- Genre normalization for multi-genre entries
- Date transformations for release year analysis
- Feature binning to categorize numerical variables
- Visual insights using `matplotlib` and `seaborn`

---

## 🔧 Technologies Used

- **Python 3.7+**
- Libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
- Jupyter Notebook for interactive analysis

---

## 🔍 Key Steps

1. **Data Cleaning**: 
   - Removed inconsistencies and handled missing values
   - Transformed columns like `Release_Date` into usable formats

2. **Genre Handling**:
   - Movies with multiple genres are split into separate rows
   - This enables more accurate genre-based aggregation

3. **Feature Engineering**:
   - Binned numeric columns using quantile cuts
   - Extracted release year from full date

4. **Exploratory Analysis**:
   - Visualized distributions and relationships
   - Grouped and compared movies by genre and release trends

---

## ▶️ How to Run

1. Clone the repo:

```bash
git clone https://github.com/KartikeySinghSingraur/Python-Project.git
cd Python-Project
