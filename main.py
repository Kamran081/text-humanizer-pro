from humanizer import humanize_text
from utils import visualize_similarity, export_doc

if __name__ == "__main__":
    text = input("Enter GPT text: ")
    polished, similarity, sentiment, readability = humanize_text(text)

    print("\n--- Humanized Text ---\n", polished)
    print("\n--- Analysis ---")
    print("Similarity with original:", round(similarity, 3))
    print("Sentiment:", sentiment)
    print("Readability Score:", readability)

    visualize_similarity(similarity)
    export_doc(polished)
