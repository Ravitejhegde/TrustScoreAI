import cv2


def analyze_anatomy(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(

        image,

        cv2.COLOR_BGR2GRAY

    )

    face_detector = cv2.CascadeClassifier(

        cv2.data.haarcascades +

        "haarcascade_frontalface_default.xml"

    )

    faces = face_detector.detectMultiScale(

        gray,

        scaleFactor=1.1,

        minNeighbors=5

    )

    face_count = len(faces)

    score = 0

    indicators = []

    if face_count == 0:

        score += 20

        indicators.append(

            "No face detected"

        )

    if face_count > 3:

        score += 20

        indicators.append(

            "Unusual number of faces"

        )

    return {

        "anatomy_score": score,

        "face_count": face_count,

        "indicators": indicators

    }