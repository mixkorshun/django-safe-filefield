import magic


def detect_content_type(f):
    sample = f.read(2048)
    f.seek(0)

    return magic.from_buffer(sample, mime=True)
