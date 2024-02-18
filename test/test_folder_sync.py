import os
import shutil
import tempfile
import unittest
from folder_sync import sync_folder, log_action


class TestFolderSync(unittest.TestCase):
    def setUp(self):
        # Create temporary directories for testing
        self.original_folder = tempfile.mkdtemp()
        self.replica_folder = tempfile.mkdtemp()
        self.log_file = tempfile.mkstemp()[1]  # Creating a temporary log file but not sure if its the right way, need to comeback here later

    def tearDown(self):
        # Remove temporary directories and files after testing
        shutil.rmtree(self.original_folder)
        shutil.rmtree(self.replica_folder)
        try:
            os.unlink(self.log_file)  # delete the log file
        except OSError as e:
            print(f"Error: {e.strerror} - {e.filename}")



    def test_sync_folder(self):
        # Create some files and directories in the original folder
        os.makedirs(os.path.join(self.original_folder, 'dir1'))
        open(os.path.join(self.original_folder, 'file1.txt'), 'w').close()

        sync_folder(self.original_folder, self.replica_folder, self.log_file)
        # Check if directories are synchronized
        self.assertTrue(os.path.exists(os.path.join(self.replica_folder, 'dir1')))
        # Check if files are synchronized
        self.assertTrue(os.path.exists(os.path.join(self.replica_folder, 'file1.txt')))

    def test_log_action(self):

        log_action(self.log_file, "Test action")
        with open(self.log_file, 'r') as f:
            lines = f.readlines()
            self.assertTrue(any("Test action" in line for line in lines))


if __name__ == '__main__':
    unittest.main()

# all test passed but i fell something is not right with the logs files.
