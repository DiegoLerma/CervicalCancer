from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Definir el modelo de datos para la entrada de la API
class PatientData(BaseModel):
    Age: float
    Number_of_sexual_partners: float
    First_sexual_intercourse: float
    Num_of_pregnancies: float
    Smokes_years: float
    Smokes_packs_per_year: float
    Hormonal_Contraceptives_years: float
    IUD_years: float
    STDs_number: float
    STDs: float
    STDs_condylomatosis: float
    STDs_cervical_condylomatosis: float
    STDs_vaginal_condylomatosis: float
    STDs_vulvo_perineal_condylomatosis: float
    STDs_syphilis: float
    STDs_pelvic_inflammatory_disease: float
    STDs_genital_herpes: float
    STDs_molluscum_contagiosum: float
    STDs_AIDS: float
    STDs_HIV: float
    STDs_Hepatitis_B: float
    STDs_HPV: float
    STDs_Number_of_diagnosis: float
    Dx_Cancer: float
    Dx_CIN: float
    Dx_HPV: float
    Dx: float

# Crear la aplicación FastAPI
app = FastAPI()

# Cargar el modelo
model = joblib.load('cervical_cancer_model.pkl')

@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: PatientData):
    try:
        # Convertir los datos de entrada a un array de numpy
        input_data = np.array([[
            data.Age, data.Number_of_sexual_partners, data.First_sexual_intercourse, data.Num_of_pregnancies,
            data.Smokes_years, data.Smokes_packs_per_year, data.Hormonal_Contraceptives_years, data.IUD_years,
            data.STDs_number, data.STDs, data.STDs_condylomatosis, data.STDs_cervical_condylomatosis,
            data.STDs_vaginal_condylomatosis, data.STDs_vulvo_perineal_condylomatosis, data.STDs_syphilis,
            data.STDs_pelvic_inflammatory_disease, data.STDs_genital_herpes, data.STDs_molluscum_contagiosum,
            data.STDs_AIDS, data.STDs_HIV, data.STDs_Hepatitis_B, data.STDs_HPV, data.STDs_Number_of_diagnosis,
            data.Dx_Cancer, data.Dx_CIN, data.Dx_HPV, data.Dx
        ]])
        
        # Hacer una predicción
        predictions = model.predict(input_data)[0]
        
        # Descomponer el resultado en respuestas individuales
        hinselmann = predictions >= 1
        schiller = predictions >= 2
        citology = predictions >= 3
        biopsy = predictions >= 4

        return {
            "Hinselmann": int(hinselmann),
            "Schiller": int(schiller),
            "Citology": int(citology),
            "Biopsy": int(biopsy)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
