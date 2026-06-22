from engines.digital_forensics.metadata_detector import analyze_metadata

from engines.digital_forensics.validation_detector import validate_image

from engines.digital_forensics.ela_detector import analyze_ela

from engines.digital_forensics.noise_detector import analyze_noise

from engines.visual_analysis.lighting_detector import analyze_lighting

from engines.visual_analysis.clone_detector import analyze_clone

from engines.visual_analysis.texture_detector import analyze_texture

from engines.visual_analysis.background_detector import analyze_background

from engines.visual_analysis.anatomy_detector import analyze_anatomy

from engines.model_analysis.ai_detector import analyze_ai_probability


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

    lighting = analyze_lighting(

        image_path

    )

    clone = analyze_clone(

        image_path

    )

    texture = analyze_texture(

        image_path

    )

    background = analyze_background(

        image_path

    )

    anatomy = analyze_anatomy(

        image_path

    )

    ai = analyze_ai_probability(

        {

            "ela": ela,

            "noise": noise,

            "lighting": lighting,

            "clone": clone,

            "texture": texture,

            "background": background,

            "anatomy": anatomy

        }

    )

    return {

        "metadata": metadata,

        "validation": validation,

        "ela": ela,

        "noise": noise,

        "lighting": lighting,

        "clone": clone,

        "texture": texture,

        "background": background,

        "anatomy": anatomy,

        "ai": ai

    }