class DataLogger:
    def __init__(self):
        self.records = []

    def store(self, record):
        self.records.append(record)

    def get_latest(self, n=50):
        return self.records[-n:] if len(self.records) > n else self.records[:]

    def clear(self):
        self.records = []

    def count(self):
        return len(self.records)
