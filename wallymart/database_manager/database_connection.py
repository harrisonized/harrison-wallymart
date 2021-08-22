#!/usr/bin/env python3

import os
import re
import pandas as pd
from wallymart.order_manager.order_item import OrderItem


class DatabaseConnection:
    """Read/write the database
    View items
    """

    def __init__(self, filename, data_dir='data'):  # should put these in config files
        self._repo_dir = re.match('^(.*?)harrison-wallymart', os.getcwd()).group()
        self.data_dir = data_dir
        self.filename = filename
        self._filepath = f'{self._repo_dir}/{self.data_dir}/{self.filename}'
        self.table = pd.read_csv(self._filepath)
        self.num_items_per_page = 5
        self.page = 1

    # ----------------------------------------------------------------------
    # Private

    def _ensure_file_ends_with_newline(self, file):
        """If csv file does not end with newline, adds a newline
        """
        # get last line
        # see: https://stackoverflow.com/questions/46258499/how-to-read-the-last-line-of-a-file-in-python
        with open(file, 'rb') as f:
            f.seek(-2, os.SEEK_END)
            try:
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)
            except OSError:
                pass
            last_line = f.readline().decode()

        # add newline if not exist
        if last_line[-1:] != '\n':
            with open(file, 'a') as f:
                f.write('\n')

    # ----------------------------------------------------------------------
    # Public

    def append(self, df):
        self.table = self.table.append(df)
        self._ensure_file_ends_with_newline(self._filepath)
        df.to_csv(self._filepath, mode='a', header=None, index=None)

    def overwrite(self):
        """This is a limitation of pandas, cannot just write to a single row
        """
        self.table.to_csv(self._filepath, index=None)

    def get_view(self):
        view = self.table[(self.page-1)*self.num_items_per_page:self.page*self.num_items_per_page]
        return view

    def next_page(self):
        if self.page*self.num_items_per_page <= len(self.table):
            self.page += 1

    def prev_page(self):
        if self.page > 1:
            self.page -= 1
