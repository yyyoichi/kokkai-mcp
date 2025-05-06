from src.sentence_transformers import encode_text


if __name__ == "__main__":
    sentences = [
        "今朝は晴れていたけど、昼から雨が降ってきた",
        "毎朝パンを食べているけど、今日はご飯を食べた",
    ]
    result = encode_text(sentences)
    print(len(result))