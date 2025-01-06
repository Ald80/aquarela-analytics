class NotFoundError(Exception):
    def __init__(self, message="Not found"):
        self.message = message
        super().__init__(self.message)

class ConflictError(Exception):
    def __init__(self, message="Conflict with the current state of the target resource"):
        self.message = message
        super().__init__(self.message)

class ServerError(Exception):
    def __init__(self, message="Internal server error"):
        self.message = message
        super().__init__(self.message)