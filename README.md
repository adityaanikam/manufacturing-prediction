Here's a `README.md` file for your project, which includes a description, setup instructions, and steps to run the project. You can customize it as needed.

---

### **README.md**

```markdown
# Manufacturing Prediction API

This project is a FastAPI-based application designed to predict manufacturing downtime using machine learning. It includes endpoints for uploading data, training a model, and making predictions.

## Features

- Upload CSV files containing manufacturing data.
- Train a logistic regression model on the uploaded data.
- Predict manufacturing downtime based on input parameters.

## Tech Stack

- **FastAPI**: For building the API.
- **Scikit-learn**: For machine learning.
- **Joblib**: For model serialization.
- **Pandas**: For data manipulation.

---

## Getting Started

### Prerequisites

- Python 3.8 or later
- Virtual environment (recommended)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/adityaanikam/manufacturing-pprediction.git
   cd manufacturing-pprediction
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the directory structure:**
   Ensure the following structure exists in the project:
   ```
   .
   ├── data/
   │   └── synthetic_manufacturing_data.csv  # Add your CSV file here
   ├── LICENSE
   ├── README.md
   ├── main.py
   └── requirements.txt
   ```

---

## How to Run

1. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API:**
   Open your browser and navigate to `http://127.0.0.1:8000`.

3. **Explore API Documentation:**
   The interactive Swagger UI is available at `http://127.0.0.1:8000/docs`.

---

## Endpoints

1. **Root Endpoint (`GET /`):**
   - Returns a welcome message.

2. **Upload Data (`POST /upload`):**
   - Upload a CSV file containing manufacturing data.
   - Example:
     ```
     Columns required: Temperature, Run_Time, Downtime_Flag
     ```

3. **Train Model (`POST /train`):**
   - Trains a logistic regression model on the uploaded data.

4. **Make Prediction (`POST /predict`):**
   - Accepts JSON input and returns downtime prediction and confidence score.
   - Example:
     ```json
     {
       "Temperature": 80,
       "Run_Time": 120
     }
     ```

---

## Example Workflow

1. Upload a CSV file with manufacturing data using the `/upload` endpoint.
2. Train the model by calling the `/train` endpoint.
3. Make predictions by sending data to the `/predict` endpoint.

---

## Dependencies

- fastapi
- uvicorn
- pandas
- scikit-learn
- joblib

Install them using:
```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## Author

- **Aditya Nikam**
