# utils/exports.py  (or keep as utils_stable_io.py – both work)
import datetime
from io import BytesIO
import pandas as pd
import re

from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor


# ==============================
# PDF & HTML EXPORTERS – your original beautiful code, fully preserved
# ==============================

def reading_to_pdf(text: str) -> BytesIO:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(A4),
                            rightMargin=60, leftMargin=60,
                            topMargin=70, bottomMargin=70)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='TitleCustom', parent=styles['Title'],
                              fontSize=22, alignment=1, spaceAfter=30,
                              textColor=HexColor("#1e3a8a")))
    styles.add(ParagraphStyle(name='HeadingBold', parent=styles['Normal'],
                              fontSize=13, fontName='Helvetica-Bold', spaceAfter=12))
    styles.add(ParagraphStyle(name='BodyTextCustom', parent=styles['Normal'],
                              fontSize=11.5, leading=16, spaceAfter=10, alignment=4))

    elements = []
    elements.append(Paragraph("LOGOS ANALYTICS FINDINGS", styles['TitleCustom']))
    elements.append(Spacer(1, 30))

    for line in text.split("\n"):
        clean = line.strip()
        if not clean:
            elements.append(Spacer(1, 8))
            continue
        clean = re.sub(r'[\*`_]', '', clean)
        is_heading = (
            clean.startswith(("Your question:", "Interpreted as:", "Date & time:",
                              "Resonance Coherence:", "Bottom line", "Conceptual Context"))
            or re.match(r'^\d+\.', clean)
        )
        if is_heading:
            elements.append(Paragraph(f"<b>{clean}</b>", styles['HeadingBold']))
        else:
            elements.append(Paragraph(clean, styles['BodyTextCustom']))
        elements.append(Spacer(1, 4))

    doc.build(elements)
    buffer.seek(0)
    return buffer


def grid_to_html(df: pd.DataFrame, topic: str, coherence: float, ratio: float) -> BytesIO:
    buffer = BytesIO()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # Raw string + .format() → works perfectly with Python 3.13 on Streamlit Cloud
    html = r"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>LOGOS 7-by-7 Grid - {topic}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f8fafc; color: #1e3a8a; }
        h1, h2 { color: #1e3a8a; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #e2e8f0; padding: 12px; text-align: center; font-size: 11px; }
        th { background: #1e3a8a; color: white; }
        tr:nth-child(even) { background: #f0f4f8; }
    </style>
</head>
<body>
    <h1>LOGOS 7×7 Grid Data</h1>
    <h2>Topic: {topic}</h2>
    <p><b>Date & time:</b> {now}</p>
    <p><b>Resonance Coherence:</b> {coherence:.1f}% | <b>Heptagonal Ratio:</b> {ratio:.3f}/1.000</p>
    {table}
</body>
</html>""".format(
        topic=topic,
        now=now,
        coherence=coherence,
        ratio=ratio,
        table=df.to_html(classes='table table-striped', header=True, index=True, border=0)
    )

    buffer.write(html.encode('utf-8'))
    buffer.seek(0)
    return buffer
