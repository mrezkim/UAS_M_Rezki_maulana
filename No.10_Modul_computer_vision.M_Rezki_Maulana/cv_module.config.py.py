import os

class Config:
    MODEL_DIR = os.path.join(os.path.dirname(__file__), "../models")
    
    # Placeholder path model (akan diisi saat implementasi)
    BARK_MODEL = os.path.join(MODEL_DIR, "bark_model.pkl")
    NEEDLE_MODEL = os.path.join(MODEL_DIR, "needle_model.h5")