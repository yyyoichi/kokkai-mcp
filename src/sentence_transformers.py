from sentence_transformers import SentenceTransformer

model: SentenceTransformer | None = None

def initialize_model():
    global model
    if model is None:
        model = SentenceTransformer("intfloat/multilingual-e5-small")
        print("Model initialized")

def encode_text(sentences: list[str]) -> list[list[float]]:
    global model
    if model is None:
        initialize_model()
    return model.encode(sentences=sentences, convert_to_tensor=False, batch_size=10).tolist() # type: ignore