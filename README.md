# Predicting Stock Returns from Stock Forums

## Overview

This project investigates the predictive power of Reddit discussions on stock market returns. We examine posts from finance-focused subreddits like r/WallStreetBets and r/Stocks using topic modeling and sentiment analysis. The main objective is to determine whether these user-generated posts contain signals that can forecast stock price movements.

Inspired by the methodology of "Choosing News Topics to Explain Stock Market Returns" by Glasserman et al. (2020), we apply Latent Dirichlet Allocation (LDA), Supervised LDA (sLDA), and logistic regression models to Reddit post content. Sentiment analysis via a fine-tuned BERT model serves as a baseline for comparison.

---

## Features

* **Data Collection**: Scraped \~4,000 Reddit posts from four subreddits.
* **Preprocessing**: Bag-of-words transformation, financial stopword removal, and token filtering.
* **Labeling**: Posts labeled as "long" or "short"; stock movement tracked three months later.
* **Modeling**:

  * Unsupervised and supervised topic modeling (LDA, sLDA)
  * Logistic regression for classification tasks
  * Sentiment analysis using BERT
* **Evaluation**:

  * Accuracy comparison between sLDA and BERT
  * Forum similarity via TTR, MTLD, FRE, TF-IDF, cosine similarity

---

## Project Structure

```
Predicting-Stock-Returns-Reddit
├── 1003Final_Part1.ipynb           # LDA and sLDA model experimentation
├── Chat_GPT_Labeling.ipynb         # Reddit post labeling workflow
├── DURF_Code.ipynb                 # Data transformation pipeline
├── ML_Final_Project_2024.ipynb     # Final model training and evaluation
├── Reddit Bot.ipynb                # Reddit scraping tool
├── wsbdata.csv                     # Reddit post dataset
├── DS_1003_Final_Project-2.pdf     # Full project report
└── README.md                       # Project description
```

---

## Models Used

* **LDA**: Identifies latent topics in Reddit posts
* **sLDA**: Learns supervised associations between topics and outcomes
* **Logistic Regression**: Predicts post stance and future stock price movement
* **BERT**: Sentiment analysis baseline

---

## Results

* **sLDA sentiment prediction accuracy**: 79.2%
* **BERT sentiment prediction accuracy**: 67.2%
* **sLDA stock price movement prediction accuracy**: 70.8%
* **Lexical analysis**:

  * r/WallStreetBets: Highest MTLD (197.81)
  * r/Stocks: Most complex FRE score (-183.42)
  * TF-IDF: "Earnings" emphasized in r/WallStreetBets and r/Stocks

---

## How to Use

1. Clone this repository and install dependencies:

```bash
pip install numpy pandas nltk scikit-learn transformers matplotlib gensim
```

2. Run `Reddit Bot.ipynb` to scrape data.
3. Process data in `Chat_GPT_Labeling.ipynb` and `DURF_Code.ipynb`.
4. Train and evaluate models in `ML_Final_Project_2024.ipynb`.

---

## Future Directions

* Scale to larger datasets (50k+ posts)
* Improve BERT with financial domain fine-tuning
* Integrate time-series forecasting models (LSTM, transformer-based)

---

## Team & Credits

Sunny Yang, Wiley Wu, Evan Wang, Jasper Wang
NYU DS 1003 Final Project – May 2024

---

## References

Glasserman, P., et al. (2020). Choosing News Topics to Explain Stock Market Returns. ICAIF.
Blei, D., Ng, A., & Jordan, M. (2003). Latent Dirichlet Allocation. JMLR.
Blei, D. & McAuliffe, J. (2007). Supervised Topic Models. NeurIPS.

---

For more details, refer to `DS_1003_Final_Project-2.pdf`.
