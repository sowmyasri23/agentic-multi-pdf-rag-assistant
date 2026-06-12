from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


def create_chat_report(chat_history):

    pdf_file = "chat_history_report.pdf"

    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "Chat History Report",
        styles["Title"]
    )

    content.append(title)

    content.append(
        Spacer(1, 20)
    )

    for item in chat_history:

        content.append(
            Paragraph(
                f"<b>User:</b> {item['question']}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Assistant:</b> {item['answer']}",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

    doc.build(content)

    return pdf_file