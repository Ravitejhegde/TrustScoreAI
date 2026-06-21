from PIL import Image
import numpy as np


def analyze_noise(image_path):

    image = Image.open(image_path)

    image = image.convert("L")

    image_array = np.array(image)

    noise_score = np.std(image_array)

    return {

        "noise_score": round(

            float(noise_score),

            2

        )

    }