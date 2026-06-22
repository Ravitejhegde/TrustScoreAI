import cv2

import numpy as np


def analyze_background(image_path):

    image = cv2.imread(

        image_path

    )

    gray = cv2.cvtColor(

        image,

        cv2.COLOR_BGR2GRAY

    )

    edges = cv2.Canny(

        gray,

        100,

        200

    )

    edge_density = np.sum(

        edges > 0

    ) / edges.size

    score = 0

    indicators = []


    if edge_density < 0.05:

        score += 20

        indicators.append(

            "Unnaturally smooth background"

        )


    if edge_density > 0.35:

        score += 20

        indicators.append(

            "Highly complex background"

        )


    return {

        "background_score": score,

        "edge_density": float(round(

            edge_density,

            3

        )),

        "indicators": indicators

    }