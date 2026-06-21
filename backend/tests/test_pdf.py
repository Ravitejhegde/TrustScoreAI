from services.analysis_pipeline import analyze_image

from services.results_formatter import format_results

from services.pdf_generator import generate_pdf


data = analyze_image(

    "uploads/image.jpeg"

)

result = format_results(

    data

)

pdf = generate_pdf(

    result

)

print(pdf)