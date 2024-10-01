# tests/test_generator.py

import unittest
import os
import shutil
from projectcompactor.generator import ProjectCompactor

class TestProjectCompactor(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory structure for testing
        self.test_dir = 'test_project'
        os.makedirs(self.test_dir, exist_ok=True)
        os.makedirs(os.path.join(self.test_dir, 'subdir'), exist_ok=True)
        
        # Create some text and binary files
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w', encoding='utf-8') as f:
            f.write("Hello World")
        
        with open(os.path.join(self.test_dir, 'file2.bin'), 'wb') as f:
            f.write(b'\x00\xFF\x00\xFF')
        
        with open(os.path.join(self.test_dir, 'subdir', 'file3.py'), 'w', encoding='utf-8') as f:
            f.write("print('Subdirectory File')")
        
        self.output_file = 'test_output.txt'
    
    def tearDown(self):
        # Remove the temporary directory after tests
        shutil.rmtree(self.test_dir)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
    
    def test_generate(self):
        compactor = ProjectCompactor(start_path=self.test_dir, output_file=self.output_file)
        compactor.generate()
        
        # Check if output file exists
        self.assertTrue(os.path.exists(self.output_file))
        
        with open(self.output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for project tree
        self.assertIn(f"{self.test_dir}/", content)
        self.assertIn("    subdir/", content)
        self.assertIn("    file1.txt", content)
        self.assertIn("    file2.bin", content)
        self.assertIn("    subdir/file3.py", content)
        
        # Check for file details
        self.assertIn("## file1.txt", content)
        self.assertIn("Hello World", content)
        
        self.assertIn("## file2.bin", content)
        self.assertIn("[Binary or Non-text file: file2.bin]", content)
        
        self.assertIn("## subdir/file3.py", content)
        self.assertIn("print('Subdirectory File')", content)

if __name__ == '__main__':
    unittest.main()
