from engines.digital_forensics.validation_detector import validate_image

from engines.digital_forensics.ela_detector import analyze_ela

from engines.digital_forensics.noise_detector import analyze_noise

from services.score_engine import calculate_score


image = "uploads/image.jpeg"

validation = validate_image(

    image

)

ela = analyze_ela(

    image

)

noise = analyze_noise(

    image

)

result = calculate_score(

    validation,

    ela,

    noise

)

print(result)