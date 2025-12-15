class DuplicateRecordError(Exception):
    """Raised when attempting to create a record that already exists."""
    def __init__(self, message="Record already exists"):
        self.message = message
        super().__init__(self.message)
