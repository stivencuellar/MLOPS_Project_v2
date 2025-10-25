import os
import pandas as pd
import pickle
import urllib.request
import kagglehub
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #Graficar
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import math
import logging
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import max_error
from sklearn.metrics import mean_absolute_error
from sklearn.decomposition import PCA
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import root_mean_squared_error
import statsmodels.api as sm
from statsmodels.stats.diagnostic import linear_reset
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_white
from statsmodels.sandbox.stats.runs import runstest_1samp
import mlflow
from scipy.stats import kstest
import pickle
import pickle
from pathlib import Path
import xgboost as xgb
from prefect import flow, task
import subprocess, textwrap, os, pathlib
import pickle
from pathlib import Path
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import root_mean_squared_error

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@task(name="read_dataframe", description="Lectura del set de datos", retries=3, retry_delay_seconds=10)
def read_dataframe():
    path = kagglehub.dataset_download("ranjeetjain3/seaborn-tips-dataset")
    destino = "MLOPS_Project/data"
    shutil.copytree(path, destino, dirs_exist_ok=True)
    print("Dataset guardado en:", destino)
    datos = pd.read_csv("MLOPS_Project/data/tips.csv")
    return datos

@task(name="normalizar_log", description="Normalizacion a logaritmo", retries=3, retry_delay_seconds=10)
def normalizar_log(datos):
    continuas=datos[["total_bill","tip","size"]]
    continuas_L = pd.DataFrame()

    for col in continuas.columns:
        col_data = continuas[col]
        min_val = col_data.min()

        if (col_data < 0).any():
            desplazamiento = abs(min_val) + 1
            continuas_L[f"{col}_L"] = np.log(col_data + desplazamiento)

        elif (col_data == 0).any():
            continuas_L[f"{col}_L"] = np.log(col_data.replace(0, 1))
        else:
            continuas_L[f"{col}_L"] = np.log(col_data)

    return continuas_L

@task(name="concatenar", description="Concatenacion de dataframes", retries=3, retry_delay_seconds=10)
def concatenar(datos, continuas_L):
    datos_concat = pd.concat([datos, continuas_L], axis=1)
    return datos_concat

@task(name="PCA_generation", description="Generacion de componentes principales", retries=3, retry_delay_seconds=10)
def PCA_generation(explicatorias):

    scaler = StandardScaler()
    explicatorias_scaled = scaler.fit_transform(explicatorias)
    pca = PCA()
    res_pca = pca.fit(explicatorias_scaled)
    pred_pca = res_pca.transform(explicatorias_scaled)
    df_pred = pd.DataFrame(pred_pca, columns=[f"PC{i+1}" for i in range(pred_pca.shape[1])])
    componentes = df_pred[["PC1", "PC2"]].copy()

    cumVar = pd.DataFrame(np.cumsum(res_pca.explained_variance_ratio_)*100,
                        columns=["cumVarPerc"])
    expVar = pd.DataFrame(res_pca.explained_variance_ratio_*100, columns=["VarPerc"])
    pd.concat([expVar, cumVar], axis=1)\
        .rename(index={0: "PC1", 1: "PC2", 2: "PC3", 3: "PC4", 4: "PC5", 5: "PC6", 6: "PC7", 7: "PC8", 8: "PC9", 9: "PC10"})
    
    return componentes

@task(name="concatenar_PCA", description="Concatenacion de componentes principales", retries=3, retry_delay_seconds=10) 
def concatenar_PCA(datos_final, componentes):
    datos_concat = pd.concat([datos_final, componentes], axis=1)
    return datos_concat


@task(name="split_data", description="Particion de datos", retries=3, retry_delay_seconds=10)
def split_data(datos_final):
    np.random.seed(101)
    sample = np.random.choice(datos_final.index, size=int(0.8 * len(datos_final)), replace=False)
    train = datos_final.loc[sample]
    test = datos_final.drop(sample)
    #X_train = train[["total_bill","tip","size"]]
    X_train_L = train[["total_bill_L","tip_L","size_L", "PC1", "PC2"]]
    return X_train_L


@task(name="train_model_PCA", description="Entrenamiento del modelo con PCA", retries=3, retry_delay_seconds=10)    
def train_model_PCA(datosEntrenamiento):
    formula_PCA = 'tip_L ~ PC1 + PC2'
    model_PCA = sm.formula.ols(formula_PCA, data=datosEntrenamiento).fit()
    return model_PCA


@flow(name="Modelo Propinas", description="End-to-end ML pipeline for tips prediction", flow_run_name="El jei tips")
def tip_prediction():
    datos = read_dataframe()
    datos.head()

    #Esta fraccion de codigo va para el main
    continuas_L = normalizar_log(datos)
    datos_final = concatenar(datos, continuas_L) # Este es el nuevo data set con toda la inforamcion completa
    print(datos_final.head())

    #PCA Será aplicado a variables con logaritmo
    explicatorias=datos_final[["total_bill_L","tip_L","size_L"]]

    componentes = PCA_generation(explicatorias)
    datos_final = concatenar_PCA(datos_final, componentes)
    print(datos_final.head())

    datosEntrenamiento = split_data(datos_final) # Partiendo la data de entrenamiento (Dataframe)

    datosEntrenamiento.head()

    modelo_entrenado_PCA = train_model_PCA(datosEntrenamiento) 
    print(modelo_entrenado_PCA.summary())

    return modelo_entrenado_PCA

# ---------------- MAIN ----------------
if __name__ == "__main__":
    tip_prediction()