import cv2

import numpy as np


def analyze_clone(image_path):

    image = cv2.imread(

        image_path

    )

    gray = cv2.cvtColor(

        image,

        cv2.COLOR_BGR2GRAY

    )

    orb = cv2.ORB_create(

        500

    )

    keypoints, descriptors = orb.detectAndCompute(

        gray,

        None

    )

    if descriptors is None:

        return {

            "clone_score": 0,

            "duplicate_regions": 0,

            "indicators": []

        }

    matcher = cv2.BFMatcher(

        cv2.NORM_HAMMING,

        crossCheck=True

    )

    matches = matcher.match(

        descriptors,

        descriptors

    )

    duplicate_regions = max(

        0,

        len(matches) - len(keypoints)

    )

    score = min(

        duplicate_regions,

        30

    )

    indicators = []

    if duplicate_regions > 10:

        indicators.append(

            "Repeated patterns detected"

        )

    return {

        "clone_score": score,

        "duplicate_regions": duplicate_regions,

        "indicators": indicators

    }