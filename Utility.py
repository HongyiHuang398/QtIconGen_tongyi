import os


def get_embed_data(path: str) :
    return os.path.join(
        os.path.dirname(__file__), path
    )