from reportlab.platypus import SimpleDocTemplate

from reportlab.platypus import Paragraph

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def generate_pdf(

    result,

    filename="trustscore_report.pdf"

):

    document = SimpleDocTemplate(

        filename

    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(

        Paragraph(

            "TrustScoreAI Report",

            styles["Title"]

        )

    )

    elements.append(

        Paragraph(

            f"Date: {datetime.now()}",

            styles["Normal"]

        )

    )

    elements.append(

        Paragraph(

            f"Trust Score: {result['trust_score']}",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            f"Risk Level: {result['risk_level']}",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            "Reasons",

            styles["Heading3"]

        )

    )

    for reason in result["reasons"]:

        elements.append(

            Paragraph(

                f"• {reason}",

                styles["Normal"]

            )

        )

    elements.append(

        Paragraph(

            "Indicators",

            styles["Heading3"]

        )

    )

    for indicator in result["indicators"]:

        elements.append(

            Paragraph(

                f"• {indicator}",

                styles["Normal"]

            )

        )

    elements.append(

        Paragraph(

            "Disclaimer:",

            styles["Heading3"]

        )

    )

    elements.append(

        Paragraph(

            "This analysis provides an estimated probability and should not be considered definitive proof.",

            styles["Normal"]

        )

    )

    document.build(

        elements

    )

    return filename