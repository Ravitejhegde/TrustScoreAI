def analyze_ai_probability(data):

    score = 0

    reasons = []

    if data["ela"]["ela_score"] > 40:

        score += 15

        reasons.append(

            "High ELA detected"

        )

    if data["noise"]["noise_score"] < 20:

        score += 10

        reasons.append(

            "Low image noise"

        )

    if data["lighting"]["lighting_score"] > 0:

        score += 10

        reasons.append(

            "Suspicious lighting"

        )

    if data["clone"]["clone_score"] > 10:

        score += 10

        reasons.append(

            "Repeated patterns"

        )

    if data["texture"]["texture_score"] > 0:

        score += 10

        reasons.append(

            "Artificial textures"

        )

    if data["background"]["background_score"] > 0:

        score += 10

        reasons.append(

            "Background anomaly"

        )

    if data["anatomy"]["anatomy_score"] > 0:

        score += 10

        reasons.append(

            "Anatomy inconsistency"

        )

    probability = min(

        score,

        100

    )

    return {

        "ai_probability": probability,

        "reasons": reasons

    }