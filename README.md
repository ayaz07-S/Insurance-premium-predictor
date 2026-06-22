# Insurance Premium Predictor

This project is a Machine Learning application that predicts the health insurance premium category based on various patient details. It consists of a **FastAPI** backend for serving the machine learning model and a **Streamlit** frontend for an interactive user interface.

## Project Structure

```
Insurance Premium Predictor/
├── app.py               # FastAPI application backend
├── frontend.py          # Streamlit frontend application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration for containerization
├── config/              # Configuration files
├── model/               # Machine learning models and prediction logic
└── schema/              # Pydantic schemas for data validation
```

## Features

- **FastAPI Backend:** Provides a high-performance RESTful API (`/predict`) to handle prediction requests.
- **Streamlit Frontend:** A user-friendly web interface allowing users to input patient details and get instant premium category predictions.
- **Input Parameters:** Age, Weight, Height, Income (LPA), Smoker status, City, and Occupation.
- **Machine Learning Model:** Utilizes a trained `scikit-learn` model to categorize health insurance premiums.

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation and Setup

1. **Clone the repository:**
   If you haven't already, clone this repository to your local machine.

2. **Create a Virtual Environment (Optional but recommended):**
   ```bash
   python -m venv myenv
   # On Windows
   myenv\Scripts\activate
   # On macOS/Linux
   source myenv/bin/activate
   ```

3. **Install Dependencies:**
   Install all the required Python packages using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the full application, you need to start both the FastAPI backend and the Streamlit frontend.

### 1. Start the FastAPI Backend
Run the following command to start the backend server:
```bash
uvicorn app:app --reload
```
The API will be available at `http://localhost:8000`. You can test the API and view the automatically generated Swagger documentation at `http://localhost:8000/docs`.

### 2. Start the Streamlit Frontend
Open a new terminal window, activate your virtual environment, and run:
```bash
streamlit run frontend.py
```
This will open the Streamlit web application in your default web browser (usually at `http://localhost:8501`), where you can interact with the predictor.

## Docker Deployment (Optional)

You can also use the provided `Dockerfile` to build and run the application in an isolated container environment. 

To build the image:
```bash
docker build -t insurance-premium-predictor .
```

To run the container:
```bash
docker run -p 8000:8000 -p 8501:8501 insurance-premium-predictor
```
*(Adjust the ports based on your Dockerfile configuration)*

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) - Backend framework
- [Streamlit](https://streamlit.io/) - Frontend application framework
- [Scikit-Learn](https://scikit-learn.org/) - Machine learning library
- [Pydantic](https://docs.pydantic.dev/) - Data validation
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
