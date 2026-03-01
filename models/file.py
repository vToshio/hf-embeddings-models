class File:
    def __init__(self, filename: str, content: str):
        self.name = filename
        self.content = content

    def __repr__(self):
        return ((self.name, self.content))