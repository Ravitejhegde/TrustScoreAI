from PIL import Image
import os


def validate_image(image_path):

    result = {}

    allowed = [

        "jpg",

        "jpeg",

        "png",

        "webp"

    ]

    # ---------- Extension ----------

    extension = image_path.split(".")[-1].lower()

    result["extension"] = extension

    result["valid_extension"] = (

        extension in allowed

    )

    # ---------- File Size ----------

    file_size = os.path.getsize(

        image_path

    )

    result["file_size_mb"] = round(

        file_size / (1024 * 1024),

        2

    )

    # ---------- Image ----------

    image = Image.open(

        image_path

    )

    result["width"] = image.width

    result["height"] = image.height

    # ---------- Actual Format ----------

    actual_format = (

        image.format.lower()

    )

    result["actual_format"] = (

        actual_format

    )

    result["format_match"] = (

        extension == actual_format

    )

    # ---------- Resolution ----------

    result["valid_resolution"] = (

        image.width >= 300

        and

        image.height >= 300

        and

        image.width <= 8000

        and

        image.height <= 8000

    )

    # ---------- Size ----------

    result["valid_size"] = (

        result["file_size_mb"] <= 20

    )

    # ---------- Indicators ----------

    result["indicators"] = []

    if not result["format_match"]:

        result["indicators"].append(

            "File extension does not match actual image format"

        )

    if not result["valid_size"]:

        result["indicators"].append(

            "File size exceeds limit"

        )

    if not result["valid_resolution"]:

        result["indicators"].append(

            "Image resolution is outside allowed range"

        )

    if not result["valid_extension"]:

        result["indicators"].append(

            "Unsupported file type"

        )

    return result