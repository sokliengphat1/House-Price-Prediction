# Median-House-Price-Prediction
Explore the California Housing dataset in this machine learning project aimed at predicting house prices. Utilizing various algorithms and data analysis techniques, the project offers insights into model building and predictive analytics in real estate.

## Project Structure

- **datasets/**
  - [housing.csv](https://www.kaggle.com/datasets/camnugent/california-housing-prices) (from Kaggle California Housing Prices Dataset) - Dataset containing historical data used for training and testing the machine learning model.

- **models/**
  - [best_model.pkl.gz](models/best_model.pkl.gz) - The trained machine learning model serialized and compressed using gzip format.
  - [scaler.pkl](models/scaler.pkl) - The serialized MinMaxScaler object used to scale features during training.

- **notebooks/**
  - [Median_House_Price_Prediction.ipynb](notebooks/Median_House_Price_Prediction.ipynb) - Jupyter notebook containing code for data exploration, preprocessing, model training, and evaluation.

- **src/**
  - [app.py](src/app.py) - The main file for implementing the application to predict new unseen data. It involves loading the model and implementing Streamlit for creating a user interface.

## Installation Requirements

To run the code in this project, you will need the following libraries:

- pandas
- matplotlib
- seaborn
- scikit-learn
- streamlit
- scipy
- joblib

You can install these dependencies using pip:

```bash
pip install pandas matplotlib seaborn wordcloud scikit-learn streamlit scipy joblib
````

You can test the application by navigating to the src folder and running the following command:
- streamlit run app.py

![image](https://github.com/sokliengphat1/Median-House-Price-Prediction/assets/156199069/183f2344-55b6-45ee-a363-3c2824b74138)
![image](https://github.com/sokliengphat1/Median-House-Price-Prediction/assets/156199069/d2922bef-85e1-49b5-af32-724e522f0958)


