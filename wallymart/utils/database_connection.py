#!/usr/bin/env python3

import os
import re
import pandas as pd
from wallymart.orm.order_item import OrderItem


class DatabaseConnection:
    """Controls read/write to the database and enables viewing rows 5 at a time.

    :parameter str filename: The filename of the database to connect to.
    :parameter str data_dir: The directory of the database.
    :ivar pd.DataFrame table: Keeps a copy of the database in memory.
    :ivar int num_items_per_page: Specify the number of lines in the database to display \
    in a single view.
    :ivar int page: Specifies which page.
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
        """Appends to the table. This method updates the temporary view and also
        writes to the CSV file in the database.

        :parameter pd.Dataframe df: The dataframe containing the rows to be appended.
        """
        self.table = self.table.append(df)
        self._ensure_file_ends_with_newline(self._filepath)
        df.to_csv(self._filepath, mode='a', header=None, index=None)

    def overwrite(self):
        """Overwrites the entire file. This is required for updating existing rows
        in the database, because it is a limitation that pandas cannot just overwrite a single row
        in a CSV file.
        """
        self.table.to_csv(self._filepath, index=None)

    def get_view(self):
        """Used for displaying products to customers and orders to employees. Default view displays
        5 rows at a time.
        """
        view = self.table.iloc[(self.page-1)*self.num_items_per_page:self.page*self.num_items_per_page]
        return view

    def next_page(self):
        """Scroll to the next view. Does nothing if used on the last view.
        """
        if self.page*self.num_items_per_page <= len(self.table):
            self.page += 1

    def prev_page(self):
        """Scroll to the previous view. Does nothing if used on the first view.
        """
        if self.page > 1:
            self.page -= 1
