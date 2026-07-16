from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT
from pathlib import Path

source = Path('interview_questions_and_answers.md')
out = Path('interview_questions_and_answers.pdf')

styles = getSampleStyleSheet()
styles['Normal'].fontName = 'Helvetica'
styles['Heading1'].fontName = 'Helvetica-Bold'
styles['Heading2'].fontName = 'Helvetica-Bold'
styles['BodyText'].fontName = 'Helvetica'
styles['Title'].fontName = 'Helvetica-Bold'

story = []
story.append(Paragraph('Interview Questions and Short Answers', styles['Title']))
story.append(Spacer(1, 12))

for line in source.read_text(encoding='utf-8').splitlines():
    if not line.strip():
        story.append(Spacer(1, 6))
    elif line.startswith('# '):
        story.append(Paragraph(line[2:], styles['Heading1']))
    elif line.startswith('## '):
        story.append(Paragraph(line[3:], styles['Heading2']))
    elif line.startswith('### '):
        story.append(Paragraph(line[4:], styles['Heading2']))
    elif line.startswith('- '):
        story.append(Paragraph(line[2:], styles['BodyText']))
    elif line.startswith('   '):
        story.append(Paragraph(line.strip(), styles['BodyText']))
    else:
        story.append(Paragraph(line, styles['BodyText']))


doc = SimpleDocTemplate(str(out), pagesize=A4, title='Interview Questions and Answers')
doc.build(story)
print(f'PDF created at {out.resolve()}')
