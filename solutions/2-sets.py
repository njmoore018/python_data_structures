def count_keywords(keywords, documents):
    counts = {}
    for keyword in keywords:
        counts[keyword] = 0
    for doc in documents:
        words = doc.split()
        for word in words:
            word = word.lower()
            if word in keywords:
                counts[word] += 1
            elif word.endswith("s") and word[:-1] in keywords:
                counts[word[:-1]] += 1
    return counts

def main():
    keywords = set(["apple", "banana", "orange"])
    documents = [
    "I ate an apple for breakfast this morning",
    "I prefer bananas to oranges",
    "Oranges are high in vitamin C"
    ]
    results = count_keywords(keywords, documents)
    print(results)


if __name__ == "__main__":
    main()