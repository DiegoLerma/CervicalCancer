# train_model.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import joblib

# Cargar datos
cancer_df = pd.read_csv('risk_factors_cervical_cancer.csv')

# Preprocesamiento de datos
cancer_df = cancer_df.replace('?', np.NaN)

numerical_df = ['Age', 'Number of sexual partners', 'First sexual intercourse','Num of pregnancies', 'Smokes (years)',
                'Smokes (packs/year)','Hormonal Contraceptives (years)','IUD (years)','STDs (number)']
categorical_df = ['Smokes','Hormonal Contraceptives','IUD','STDs','STDs:condylomatosis','STDs:cervical condylomatosis',
                  'STDs:vaginal condylomatosis','STDs:vulvo-perineal condylomatosis', 'STDs:syphilis',
                  'STDs:pelvic inflammatory disease', 'STDs:genital herpes','STDs:molluscum contagiosum', 'STDs:AIDS',
                  'STDs:HIV','STDs:Hepatitis B', 'STDs:HPV', 'STDs: Number of diagnosis','Dx:Cancer', 'Dx:CIN',
                  'Dx:HPV', 'Dx', 'Hinselmann', 'Schiller','Citology', 'Biopsy']

for feature in numerical_df:
    cancer_df[feature] = pd.to_numeric(cancer_df[feature], errors='coerce').fillna(cancer_df[feature].astype(float).mean())

for feature in categorical_df:
    cancer_df[feature] = pd.to_numeric(cancer_df[feature], errors='coerce').fillna(1.0)

cancer_df['Number of sexual partners'] = round(cancer_df['Number of sexual partners'].astype(float))
cancer_df['Num of pregnancies'] = round(cancer_df['Num of pregnancies'].astype(float))
cancer_df['STDs (number)'] = round(cancer_df['STDs (number)'].astype(float))

cancer_df.drop(['STDs: Time since first diagnosis', 'STDs: Time since last diagnosis', 'Smokes', 'Hormonal Contraceptives', 'IUD'], axis=1, inplace=True)

# Separación de características y etiquetas
cancer_df_features = cancer_df.drop(['Hinselmann', 'Schiller', 'Citology', 'Biopsy'], axis=1)
cancer_df['cervical_cancer'] = cancer_df[['Hinselmann', 'Schiller', 'Citology', 'Biopsy']].sum(axis=1)
cancer_df_label = cancer_df['cervical_cancer']

# Balanceo de datos
smote = SMOTE()
cancer_df_features_ovr, cancer_df_label_ovr = smote.fit_resample(cancer_df_features, cancer_df_label)

# Entrenamiento del modelo
model = RandomForestClassifier(n_jobs=4, n_estimators=100, random_state=42)
model.fit(cancer_df_features_ovr, cancer_df_label_ovr)

# Guardar el modelo
joblib.dump(model, 'cervical_cancer_model.pkl')
