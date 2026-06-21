from engines.digital_forensics.metadata_detector import analyze_metadata

from engines.digital_forensics.validation_detector import validate_image

from engines.digital_forensics.ela_detector import analyze_ela

from engines.digital_forensics.noise_detector import analyze_noise

from services.score_engine import calculate_score


def analyze_image(image_path):

    metadata = analyze_metadata(

        image_path

    )

    validation = validate_image(

        image_path

    )

    ela = analyze_ela(

        image_path

    )

    noise = analyze_noise(

        image_path

    )

    score = calculate_score(

        validation,

        ela,

        noise

    )

    return {

        "metadata": metadata,

        "validation": validation,

        "ela": ela,

        "noise": noise,

        "score": score

    }