"""
DataLogger — Day 3
==================
Responsibility: Store one complete record per cycle in memory and
serve the most recent N records to the dashboard for display.

Storage is a plain Python list — no database, no files.
This is intentional:
  - Zero setup (no sqlite install, no file path management)
  - Students already know how lists work
  - DataLogger can be swapped for a file-backed version in a future
    phase without changing any other class
"""


class DataLogger:

    def __init__(self):
        # Pre-filled: a plain list is all the storage this class needs.
        self.records = []

    def store(self, record):
        """
        Append one cycle record to the in-memory log.

        Args:
            record (dict): complete cycle record assembled by main.py
                           (contains timestamp, temperature, ac_state, etc.)
        """
        # TODO: append record to self.records
        pass

    def get_latest(self, n=50):
        """
        Return the most recent n records.
        If fewer than n records exist, return all of them.

        Args:
            n (int): maximum number of records to return

        Returns:
            list[dict]: the last n items from self.records
        """
        # TODO: return the last n records from self.records
        # HINT: self.records[-n:] gives the last n items.
        #       Test both cases: what happens when len(records) > n?
        #       What happens when len(records) <= n?
        #       Both should work with a single expression.
        pass

    def clear(self):
        """Wipe all stored records (allows reset without restarting the simulation)."""
        # TODO: reset self.records to an empty list
        pass

    def count(self):
        """Return the total number of records stored since the simulation started."""
        # TODO: return the number of items in self.records
        pass
