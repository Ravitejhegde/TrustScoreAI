from PIL import Image

import numpy as np


def analyze_lighting(image_path):

    image = Image.open(

        image_path

    )

    gray = image.convert(

        "L"

    )

    pixels = np.array(

        gray

    )

    brightness = np.mean(

        pixels

    )

    contrast = np.std(

        pixels

    )

    score = 0

    indicators = []


    if brightness > 220:

        score += 20

        indicators.append(

            "Overly bright image"

        )


    if brightness < 40:

        score += 20

        indicators.append(

            "Overly dark image"

        )


    if contrast < 30:

        score += 20

        indicators.append(

            "Low contrast detected"

        )


    return {

        "lighting_score": score,

        "brightness": float(round(

            brightness,

            2

        )),

        "contrast": float(round(

            contrast,

            2

        )),

        "indicators": indicators

    }