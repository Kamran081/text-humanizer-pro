import matplotlib.pyplot as plt
from docx import Document

def visualize_similarity(similarity):
    plt.bar(["Similarity"], [similarity])
    plt.title("Plagiarism Reduction")
    plt.show()

def export_doc(text, filename="output.docx"):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(filename)
