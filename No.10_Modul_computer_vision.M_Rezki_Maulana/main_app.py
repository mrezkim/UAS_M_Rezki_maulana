from cv_module.detector import TreeDetector
from cv_module.features import FeatureExtractor
from cv_module.classifier import PineClassifier

def analyze_tree(image_path):
    # Inisialisasi modul CV
    detector = TreeDetector()
    extractor = FeatureExtractor()
    classifier = PineClassifier()
    
    # Baca gambar
    image = cv2.imread(image_path)
    
    # Step 1: Deteksi pohon (tanpa proses aktual)
    contour, roi = detector.detect(image)
    
    # Step 2: Ekstraksi ciri (placeholder)
    bark_features = extractor.extract_bark_features(roi)
    needle_features = extractor.extract_needle_features(roi)
    
    # Step 3: Klasifikasi (dummy)
    prediction = classifier.predict(bark_features + needle_features)
    
    return {
        "detection_roi": roi.shape,  # Contoh info debug
        "features": {
            "bark": len(bark_features),
            "needle": len(needle_features)
        },
        "prediction": prediction
    }