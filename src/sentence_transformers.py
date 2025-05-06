from sentence_transformers import SentenceTransformer

model: SentenceTransformer | None = None

def initialize_model():
    global model
    if model is None:
        model = SentenceTransformer("intfloat/multilingual-e5-small")
        print("Model initialized")

def encode_text(sentences: list[str]):
    global model
    if model is None:
        initialize_model()
    return model.encode(sentences=sentences, convert_to_tensor=True) # type: ignore