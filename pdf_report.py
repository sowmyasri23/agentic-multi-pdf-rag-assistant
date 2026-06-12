from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(content, output_path):

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Resume Analysis Report",
        styles["Title"]
    )

    elements.append(title)

    elements.append(Spacer(1, 12))

    report_text = Paragraph(
        content.replace("\n", "<br/>"),
        styles["BodyText"]
    )

    elements.append(report_text)

    doc.build(elements)

    return output_path