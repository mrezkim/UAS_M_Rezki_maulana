# Pemanggilan fungsi
result = analyze_tree("pinus.jpg")
print(result)

# Output:
{
    "detection_roi": (300, 200, 3),  # Dimensi ROI terdeteksi
    "features": {
        "bark": 3,
        "needle": 2
    },
    "prediction": "White pine"
}