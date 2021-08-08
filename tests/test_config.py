#!/usr/bin/env python3

import unittest
import os
from wallymart.database_manager.database_configurator import DatabaseConfigurator

class TestConfig(unittest.TestCase):

    def test_database_configurator(self):
        """Test creation of database"""
        db_configurator = DatabaseConfigurator()
        db_configurator.initialize_database()
        # check for each table that exists
        for filename in db_configurator.filename_for_table_name.values():
            with self.subTest():
                file = f'{db_configurator._repo_dir}/{db_configurator.data_dir}/{filename}'
                assert os.path.exists(file), f"{filename} does not exist"

if __name__ == '__main__':
    unittest.main()
