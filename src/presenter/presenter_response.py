class PresenterResponse:
    def __init__(self, data=None, error=None):
        self.data = data
        self.error = error
        self.valid = not error
