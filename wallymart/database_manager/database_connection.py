#!/usr/bin/env python3

import os
import re
import pandas as pd

class DatabaseConnection:
    """Read/write the database
    """
    def __init__(self, filename, data_dir='data'):  # should put these in config files
        self._repo_dir = re.match('^(.*?)harrison-wallymart', os.getcwd()).group()
        self.data_dir = data_dir
        self.filename = filename
        self._filepath = f'{self._repo_dir}/{self.data_dir}/{self.filename}'
        self.table = pd.read_csv(self._filepath)

    def _ensure_file_ends_with_newline(self, file):
        """If csv file does not end with newline, adds a newline
        """
        # get last line
        # see: https://stackoverflow.com/questions/46258499/how-to-read-the-last-line-of-a-file-in-python
        with open(file, 'rb') as f:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
            last_line = f.readline().decode()

        # add newline if not exist
        if last_line[-1:] != '\n':
            with open(file, 'a') as f:
                f.write('\n')

    def append(self, df):
        self.table = self.table.append(df)
        self._ensure_file_ends_with_newline(self._filepath)
        df.to_csv(self._filepath, mode='a', header=None, index=None)
