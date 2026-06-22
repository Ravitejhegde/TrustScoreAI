from services.analysis_pipeline import analyze_image

from services.results_formatter import format_results


data = analyze_image(

    "uploads/sample.png"

)

result = format_results(

    data

)

print(

    result

)