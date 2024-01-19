"""
from reportlab.pdfgen import canvas

def to_pdf(arquivo_entrada, pdf_saida):

    with open(arquivo_entrada, "r",encoding="utf-8") as arquivo_texto:
        conteudo = arquivo_texto.read()

    conteudo = conteudo.replace('\\n', '\n')
    pdf = canvas.Canvas(pdf_saida)
    pdf.setFont("Helvetica", 12)
    
    
    # Configura a posição inicial
    x_pos = 100
    y_pos = 800

    # Divide o conteúdo em linhas e adiciona ao PDF
    pdf.setTextOrigin(x_pos, y_pos)
    pdf.setFont("Helvetica", 12)

    # Adiciona o texto com quebra de linha automática
    pdf.drawText(conteudo)
        
    pdf.save()


to_pdf("arquivo_playlists.txt","pdf_playlists.pdf") """

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph

def converter_txt_para_pdf(arquivo_entrada, pdf_saida):
    # Abre o arquivo de texto para leitura
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo_texto:
        # Lê o conteúdo do arquivo de texto
        conteudo = arquivo_texto.read()

    # Substitui as quebras de linha representadas por '\n' por quebras de linha reais
    conteudo = conteudo.replace('\\n', '\n')

    # Cria um objeto PDF usando reportlab
    pdf = SimpleDocTemplate(pdf_saida, pagesize=letter)
    story = []

    # Adiciona o conteúdo ao PDF usando Paragraph
    style = getSampleStyleSheet()["Normal"]
    par = Paragraph(conteudo, style)
    story.append(par)

    # Constrói o PDF
    pdf.build(story)

# Substitua 'seuarquivo.txt' e 'seupdf.pdf' pelos nomes do seu arquivo de texto e o nome desejado para o PDF, respectivamente.
converter_txt_para_pdf("arquivo_playlists.txt","pdf_playlists.pdf")
