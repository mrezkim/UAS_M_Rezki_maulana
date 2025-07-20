import cv2

class TreeDetector:
    def __init__(self):
        """
        Inisialisasi detektor (tanpa implementasi deteksi).
        """
        self.detector = None  # Placeholder untuk model deteksi
    
    def detect(self, image):
        """
        Input: Gambar (numpy array)
        Output: 
            - Kontur pohon (placeholder)
            - ROI (Region of Interest) pohon
        """
        # Contoh return dummy (akan diimplementasi nanti)
        height, width = image.shape[:2]
        fake_contour = [(width//4, height//4), (3*width//4, height//4), 
                       (3*width//4, 3*height//4), (width//4, 3*height//4)]
        
        return fake_contour, image[height//4:3*height//4, width//4:3*width//4]