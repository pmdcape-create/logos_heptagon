import datetime
from io import BytesIO
import pandas as pd
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.colors import HexColor

# ==============================
# LLM SELECTOR
# ==============================
def get_llm(api_key):
    if api_key.startswith("gsk_"):
        return ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key, temperature=0.7)
    else:
        return ChatOpenAI(model="gpt-4o", api_key=api_key, temperature=0.7)

# ==============================
# PDF & HTML EXPORTERS
# ==============================
def reading_to_pdf(text: str) -> BytesIO:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(A4),
                            rightMargin=60, leftMargin=60, topMargin=70, bottomMargin=70)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='TitleCustom', parent=styles['Title'], fontSize=22, alignment=1, spaceAfter=30, textColor=HexColor("#1e3a8a")))
    styles.add(ParagraphStyle(name='HeadingBold', parent=styles['Normal'], fontSize=13, fontName='Helvetica-Bold', spaceAfter=12))
    styles.add(ParagraphStyle(name='BodyTextCustom', parent=styles['Normal'], fontSize=11.5, leading=16, spaceAfter=10, alignment=4))

    elements = []
    elements.append(Paragraph("LOGOS ANALYTICS FINDINGS", styles['TitleCustom']))
    elements.append(Spacer(1, 30))

    for line in text.split("\n"):
        clean = line.strip()
        if not clean:
            elements.append(Spacer(1, 8))
            continue
        clean = re.sub(r'[\*`_]', '', clean)
        is_heading = any(clean.startswith(x) for x in ["Your question:", "Interpreted as:", "Date & time:", "Resonance Coherence:", "Bottom line", "Conceptual Context"]) or re.match(r'^\d+\.', clean)
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
    html = f"""
    <!DOCTYPE html>
    <html>
    <head># utils/exports.py   ← you can also rename the file to exports.py if you want
import datetime
from io import BytesIO
import pandas as pd
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
import re


# ==============================
# PDF & HTML EXPORTERS (your original beautiful code – kept 100%)
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
            any(clean.startswith(x) for x in ["Your question:", "Interpreted as:",
                                              "Date & time:", "Resonance Coherence:",
                                              "Bottom line", "Conceptual Context"])
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
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>LOGOS 7x7 Grid – {topic}</title>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #f8fafc; color: #1e3a8a; }}
            h1, h2 {{ color: #1e3a8a; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ border: 1px solid #e2e8f0; padding: 12px; text-align: center; font-size: 11px; }}
            th {{ background: #1e3a8a; color: white; }}
            tr:nth-child(even) {{ background: #f0f4f8; }}
        </style>
    </head>
    <body>
        <h1>LOGOS 7×7 Grid Data</h1>
        <h2>Topic: {topic}</h2>
        <p><b>Date & time:</b> {now}</p>
        <p><b>Resonance Coherence:</b> {coherence:.1f}% | <b>Heptagonal Ratio:</b> {ratio:.3f}/1.000</p>
        {df.to_html(classes='table table-striped', header=True, index=True, border=0)}
    </body>
    </html>
    """
    buffer.write(html.encode('utf-8'))
    buffer.seek(0)
    return buffer
        <title>LOGOS 7x7 Grid - {topic}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #f8fafc; color: #1e3a8a; }}
            h1, h2 {{ color: #1e3a8a; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ border: 1px solid #e2e8f0; padding: 12px; text-align: center; font-size: 11px; }}
            th {{ background: #1e3a8a; color: white; }}
            tr:nth-child(even) {{ background: #f0f4f8; }}
            .layer-header {{ font-weight: bold; background: #e2e8f0; color: #1e3a8a; }}
        </style>
    </head>
    <body>
        <h1>LOGOS 7x7 Grid Data</h1>
        <h2>Topic: {topic}</h2>
        <p><b>Date & time:</b> {now}</p>
        <p><b>Resonance Coherence:</b> {coherence:.1f}% | <b>Heptagonal Ratio:</b> {ratio:.3f}/1.000</p>
        {df.to_html(classes='table table-striped', header=True, index=True)}
    </body>
    </html>
    """
    buffer.write(html.encode('utf-8'))
    buffer.seek(0)
    return buffer
