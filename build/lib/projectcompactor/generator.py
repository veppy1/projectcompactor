# projectcompactor/generator.py

import os
import argparse
import logging
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

class ProjectCompactor:
    def __init__(self, start_path=None, output_file='project_structure.txt',
                 text_extensions=None, exclude_dirs=None, exclude_files=None, verbose=False):
        """
        Initializes the ProjectCompactor.

        Args:
            start_path (str, optional): Path to start traversal. Defaults to current directory.
            output_file (str, optional): Name of the output file. Defaults to 'project_structure.txt'.
            text_extensions (set, optional): Set of file extensions to treat as text files.
            exclude_dirs (set, optional): Set of directory names to exclude.
            exclude_files (set, optional): Set of file extensions to exclude.
            verbose (bool, optional): Enable verbose logging. Defaults to False.
        """
        self.start_path = os.path.abspath(start_path) if start_path else os.getcwd()
        self.output_file = output_file
        self.text_file_extensions = text_extensions if text_extensions else {
            '.txt', '.py', '.html', '.css', '.js', '.md', '.json',
            '.xml', '.csv', '.yaml', '.yml', '.ini', '.cfg', '.bat', '.sh',
            '.java', '.c', '.cpp', '.rb', '.go', '.ts', '.jsx', '.tsx'
        }
        self.exclude_dirs = exclude_dirs if exclude_dirs else set()
        self.exclude_files = exclude_files if exclude_files else set()
        self.verbose = verbose

        # Set up logging
        logging.basicConfig(
            level=logging.DEBUG if self.verbose else logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def is_text_file(self, file_path):
        """
        Determines if a file is a text file by attempting to read its content.

        Args:
            file_path (str): Path to the file.

        Returns:
            bool: True if text file, False otherwise.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                f.read(1024)
            return True
        except (UnicodeDecodeError, PermissionError, IsADirectoryError):
            return False

    def generate_tree(self):
        """
        Generates the project tree as a string.

        Returns:
            str: Hierarchical project tree.
        """
        tree_lines = []
        for root, dirs, files in os.walk(self.start_path):
            # Exclude specified directories
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
            # Calculate the level of indentation
            level = root.replace(self.start_path, '').count(os.sep)
            indent = ' ' * 4 * level
            dir_name = os.path.basename(root) if os.path.basename(root) else root
            tree_lines.append(f"{indent}{dir_name}/")
            sub_indent = ' ' * 4 * (level + 1)

            # Exclude specified file types
            filtered_files = [f for f in files if os.path.splitext(f)[1] not in self.exclude_files]

            for file in filtered_files:
                tree_lines.append(f"{sub_indent}{file}")

        return '\n'.join(tree_lines)

    def process_file(self, file_path, relative_path):
        """
        Processes a single file to extract its content or indicate binary.

        Args:
            file_path (str): Absolute path to the file.
            relative_path (str): Path relative to the start directory.

        Returns:
            str: Detailed information about the file.
        """
        details = [f"## {relative_path}"]

        _, ext = os.path.splitext(file_path)
        if ext.lower() in self.text_file_extensions and self.is_text_file(file_path):
            details.append(f"### Contents of {os.path.basename(file_path)}")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    contents = f.read()
                details.append(contents)
            except Exception as e:
                details.append(f"[Error reading file: {e}]")
        else:
            details.append(f"[Binary or Non-text file: {os.path.basename(file_path)}]")
        
        details.append("\n")  # Add a newline for separation
        return '\n'.join(details)

    def generate_file_details(self):
        """
        Generates detailed information for each file using multi-threading.

        Returns:
            str: File details including contents or binary indication.
        """
        details = []
        file_paths = []
        relative_paths = []

        # Collect all file paths and their relative paths
        for root, dirs, files in os.walk(self.start_path):
            # Exclude specified directories
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
            # Exclude specified file types
            for file in files:
                if os.path.splitext(file)[1] in self.exclude_files:
                    continue
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, self.start_path)
                file_paths.append(file_path)
                relative_paths.append(relative_path)
        
        logging.info(f"Processing {len(file_paths)} files...")

        # Use ThreadPoolExecutor to process files concurrently
        with ThreadPoolExecutor(max_workers=os.cpu_count() or 1) as executor:
            future_to_file = {
                executor.submit(self.process_file, fp, rp): rp
                for fp, rp in zip(file_paths, relative_paths)
            }
            for future in tqdm(as_completed(future_to_file), total=len(file_paths), desc="Processing files"):
                file_detail = future.result()
                details.append(file_detail)
        
        return '\n'.join(details)

    def generate(self):
        """
        Generates the project structure and writes to the output file.
        """
        logging.info("Generating project tree...")
        tree = self.generate_tree()
        logging.info("Generating file details...")
        details = self.generate_file_details()

        with open(self.output_file, 'w', encoding='utf-8') as output:
            # Write the project tree at the top
            output.write("# Project Structure\n\n")
            output.write(tree)
            output.write("\n\n# File Details\n\n")
            
            # Write detailed information for each file
            output.write(details)
        
        logging.info(f"Project structure has been saved to '{self.output_file}'.")

def main():
    parser = argparse.ArgumentParser(
        description='ProjectCompactor: Generate a project tree and file contents.'
    )
    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='Path to the directory to analyze (default: current directory)'
    )
    parser.add_argument(
        '-o', '--output',
        default='project_structure.txt',
        help='Output file name (default: project_structure.txt)'
    )
    parser.add_argument(
        '-e', '--extensions',
        nargs='*',
        help='Additional file extensions to treat as text files (e.g., .md .rst)'
    )
    parser.add_argument(
        '--exclude-dirs',
        nargs='*',
        default=[],
        help='Directories to exclude from the analysis (e.g., node_modules .git)'
    )
    parser.add_argument(
        '--exclude-files',
        nargs='*',
        default=[],
        help='File extensions to exclude from the analysis (e.g., .log .tmp)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    args = parser.parse_args()

    # Combine default text extensions with user-specified extensions
    text_extensions = set()
    if args.extensions:
        text_extensions.update(ext if ext.startswith('.') else f".{ext}" for ext in args.extensions)

    compactor = ProjectCompactor(
        start_path=args.path,
        output_file=args.output,
        text_extensions=text_extensions if text_extensions else None,
        exclude_dirs=set(args.exclude_dirs),
        exclude_files=set(args.exclude_files),
        verbose=args.verbose
    )
    compactor.generate()

if __name__ == '__main__':
    main()
