from PIL import Image
from PIL import ImageChops

import os
import uuid

def analyze_ela(image_path):

    temp_path = "temp_ela.jpg"

    original = Image.open(

        image_path

    )

    original.save(

        temp_path,

        "JPEG",

        quality=90

    )

    compressed = Image.open(

        temp_path

    )

    ela_image = ImageChops.difference(

        original.convert("RGB"),

        compressed.convert("RGB")

    )

    extrema = ela_image.getextrema()

    max_difference = max(

        value[1]

        for value in extrema

    )

    os.remove(

        temp_path

    )

    return {

        "ela_score": max_difference

    }