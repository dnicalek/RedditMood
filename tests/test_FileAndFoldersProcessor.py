import unittest
import os
import shutil
import json
from file_and_folders_processor import FileAndFoldersProcessor

class TestFileAndFoldersProcessor(unittest.TestCase):

    def setUp(self):
        # Set up a temporary folder for testing
        self.temp_folder = "D:\\temp_test_folder"
        os.makedirs(self.temp_folder, exist_ok=True)

    def tearDown(self):
        # Clean up the temporary folder after testing
        if os.path.exists(self.temp_folder):
            shutil.rmtree(self.temp_folder)

    def test_create_results_folder(self):
        # Arrange
        processor = FileAndFoldersProcessor()

        # Act
        processor.create_results_folder()

        # Assert
        full_folder_path = os.path.abspath("../results")
        print(f"Does folder {full_folder_path} exist? {os.path.exists(full_folder_path)}")
        print(f"Is {full_folder_path} a directory? {os.path.isdir(full_folder_path)}")
        self.assertTrue(os.path.exists(full_folder_path))
        self.assertTrue(os.path.isdir(full_folder_path))

    def test_count_files_in_folder(self):
        # Arrange
        processor = FileAndFoldersProcessor()
        file_path_1 = os.path.join(self.temp_folder, "file1.txt")
        file_path_2 = os.path.join(self.temp_folder, "file2.txt")
        file_path_3 = os.path.join(self.temp_folder, "file3.txt")

        os.makedirs(os.path.join(self.temp_folder, "folder"))
        with open(file_path_1, "w") as f:
            f.write("Test data")
        with open(file_path_2, "w") as f:
            f.write("Test data")
        with open(file_path_3, "w") as f:
            f.write("Test data")

        # Act
        count = processor.count_files_in_folder(self.temp_folder)

        # Assert
        self.assertEqual(count, 3)

    def test_read_lines_from_file(self):
        # Arrange
        processor = FileAndFoldersProcessor()
        file_path = os.path.join(self.temp_folder, "test_file.txt")

        # Create a file with test data
        with open(file_path, "w") as f:
            f.write("Line 1\nLine 2\nLine 3")

        # Act
        lines, num_posts = processor.read_lines_from_file(file_path)

        # Assert
        self.assertEqual(lines, ["Line 1\n", "Line 2\n", "Line 3"])
        self.assertEqual(num_posts, 3)

    def test_save_data_to_json(self):
        # Arrange
        processor = FileAndFoldersProcessor()
        file_path = os.path.join(self.temp_folder, "output_file.json")
        data = {"key": "value"}

        # Act
        processor.save_data_to_json(file_path, data)

        # Assert
        with open(file_path, "r", encoding="utf-8") as f:
            saved_data = json.load(f)
            self.assertEqual(saved_data, data)

if __name__ == '__main__':
    unittest.main()
