import cv2

import numpy as np


def analyze_texture(image_path):

    image = cv2.imread(

        image_path

    )

    gray = cv2.cvtColor(

        image,

        cv2.COLOR_BGR2GRAY

    )

    laplacian = cv2.Laplacian(

        gray,

        cv2.CV_64F

    )

    texture_value = np.var(

        laplacian

    )

    score = 0

    indicators = []


    if texture_value < 100:

        score = 20

        indicators.append(

            "Over-smoothed texture detected"

        )


    return {

        "texture_score": score,

        "texture_value": round(

            texture_value,

            2

        ),

        "indicators": indicators

    }