def format_results(data):

    trust_score = 100

    reasons = []

    indicators = []

    if not data["validation"]["format_match"]:

        trust_score -= 20

        reasons.append(

            "Format mismatch"

        )

    if data["ela"]["ela_score"] > 40:

        trust_score -= 30

        reasons.append(

            "High ELA score"

        )

    if data["lighting"]["lighting_score"] > 0:

        trust_score -= 10

        reasons.append(

            "Suspicious lighting"

        )

    if data["clone"]["clone_score"] > 10:

        trust_score -= 10

        reasons.append(

            "Repeated patterns"

        )

    if data["texture"]["texture_score"] > 0:

        trust_score -= 10

        reasons.append(

            "Artificial textures"

        )

    if data["background"]["background_score"] > 0:

        trust_score -= 10

        reasons.append(

            "Background anomaly"

        )

    if data["anatomy"]["anatomy_score"] > 0:

        trust_score -= 10

        reasons.append(

            "Anatomy inconsistency"

        )

    indicators.extend(

        data["validation"]["indicators"]

    )

    indicators.extend(

        data["lighting"]["indicators"]

    )

    indicators.extend(

        data["texture"]["indicators"]

    )

    indicators.extend(

        data["background"]["indicators"]

    )

    indicators.extend(

        data["anatomy"]["indicators"]

    )

    trust_score = max(

        0,

        trust_score

    )

    if trust_score >= 80:

        risk_level = "Safe"

    elif trust_score >= 50:

        risk_level = "Uncertain"

    else:

        risk_level = "Suspicious"

    return {

        "trust_score": trust_score,

        "risk_level": risk_level,

        "reasons": reasons,

        "indicators": indicators

    }