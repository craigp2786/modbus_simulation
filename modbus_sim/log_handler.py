import logging

class InMemoryLogHandler(logging.Handler):
    def __init__(self, log_storage):
        super().__init__()
        self.log_storage = log_storage

    def emit(self, record):
        self.log_storage.append(self.format(record))

