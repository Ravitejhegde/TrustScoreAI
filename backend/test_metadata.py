from engines.digital_forensics.metadata_detector import analyze_metadata

image_path = "uploads/image.jpeg"

result = analyze_metadata(image_path)

print(result)