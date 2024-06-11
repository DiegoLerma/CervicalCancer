# Cervical Cancer Risk Prediction API

This project provides a REST API for predicting the risk of cervical cancer based on patient data. The API is built using FastAPI and leverages a Random Forest classifier for the prediction.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the API](#running-the-api)
- [API Usage](#api-usage)
  - [Endpoints](#endpoints)
  - [Request Example](#request-example)
  - [Response Example](#response-example)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project aims to predict the risk of cervical cancer by using various patient data points. It provides an easy-to-use API where you can submit patient information and receive a prediction indicating whether the patient is at risk of cervical cancer.

## Setup

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/DiegoLerma/CervicalCancer.git
    cd cervical-cancer-prediction-api
    ```

2. Create and activate a virtual environment (recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Train the model (if not already trained):

    ```sh
    python train_model.py
    ```

### Running the API

1. Start the FastAPI server:

    ```sh
    uvicorn api:app --reload
    ```

2. The API will be accessible at `http://127.0.0.1:8000`.

## API Usage

### Endpoints

- `POST /predict`: Predict the risk of cervical cancer based on patient data.

### Request Example

Send a `POST` request to `http://127.0.0.1:8000/predict` with the following JSON body:

```json
{
    "Age": 30,
    "Number_of_sexual_partners": 3,
    "First_sexual_intercourse": 18,
    "Num_of_pregnancies": 2,
    "Smokes_years": 5,
    "Smokes_packs_per_year": 10,
    "Hormonal_Contraceptives_years": 2,
    "IUD_years": 0,
    "STDs_number": 0,
    "STDs": 0,
    "STDs_condylomatosis": 0,
    "STDs_cervical_condylomatosis": 0,
    "STDs_vaginal_condylomatosis": 0,
    "STDs_vulvo_perineal_condylomatosis": 0,
    "STDs_syphilis": 0,
    "STDs_pelvic_inflammatory_disease": 0,
    "STDs_genital_herpes": 0,
    "STDs_molluscum_contagiosum": 0,
    "STDs_AIDS": 0,
    "STDs_HIV": 0,
    "STDs_Hepatitis_B": 0,
    "STDs_HPV": 0,
    "STDs_Number_of_diagnosis": 0,
    "Dx_Cancer": 0,
    "Dx_CIN": 0,
    "Dx_HPV": 0,
    "Dx": 0
}
```

### Response Example

The API will respond with a JSON object indicating the results of the different tests:

```json
{
    "Hinselmann": 1,
    "Schiller": 1,
    "Citology": 1,
    "Biopsy": 1
}
```

## Model Training

To train the model, run the `train_model.py` script. This script processes the data, handles missing values, and trains a Random Forest model. The trained model is then saved to a file named `cervical_cancer_model.pkl`.

```sh
python train_model.py
```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
