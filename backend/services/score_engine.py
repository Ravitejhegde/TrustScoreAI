def calculate_score(

    validation,

    ela,

    noise

):

    score = 0

    reasons = []

    # ---------- Validation ----------

    if not validation["format_match"]:

        score += 15

        reasons.append(

            "Format mismatch"

        )

    # ---------- ELA ----------

    if ela["ela_score"] > 40:

        score += 35

        reasons.append(

            "High ELA score"

        )

    elif ela["ela_score"] > 20:

        score += 20

        reasons.append(

            "Medium ELA score"

        )

    # ---------- Noise ----------

    if noise["noise_score"] < 15:

        score += 20

        reasons.append(

            "Over smooth texture"

        )

    score = min(

        score,

        100

    )

    return {

        "trust_score": score,

        "reasons": reasons

    }