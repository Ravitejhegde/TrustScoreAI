def format_results(data):

    score = data["score"]["trust_score"]

    if score <= 30:

        risk = "Likely Human"

    elif score <= 60:

        risk = "Uncertain"

    elif score <= 80:

        risk = "Likely AI Generated"

    else:

        risk = "Highly Likely AI Generated"

    return {

        "trust_score": score,

        "risk_level": risk,

        "reasons": data["score"]["reasons"],

        "indicators": data["validation"]["indicators"]

    }