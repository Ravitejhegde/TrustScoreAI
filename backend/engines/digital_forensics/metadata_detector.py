from PIL import Image
import os
import exifread


def analyze_metadata(image_path):

    result = {}

    # ---------- Basic file info ----------

    result["file_name"] = os.path.basename(image_path)

    result["file_size_kb"] = round(
        os.path.getsize(image_path) / 1024,
        2
    )

    image = Image.open(image_path)

    result["width"] = image.width

    result["height"] = image.height

    result["format"] = image.format

    # ---------- EXIF info ----------

    result["camera_model"] = "Unknown"

    result["gps"] = "Not Found"

    result["software"] = "Unknown"

    with open(image_path, "rb") as file:

        tags = exifread.process_file(
            file,
            details=False
        )

        if "Image Model" in tags:

            result["camera_model"] = str(
                tags["Image Model"]
            )

        if "Image Software" in tags:

            result["software"] = str(
                tags["Image Software"]
            )

        gps_keys = [

            key

            for key in tags

            if "GPS" in key

        ]

        if gps_keys:

            result["gps"] = "Available"

    return result