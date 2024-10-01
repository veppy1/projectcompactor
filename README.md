# ProjectCompactor

**ProjectCompactor** is a Python tool that generates a hierarchical project structure of a given directory. It includes the contents of text-based files and lists binary or non-text files without attempting to read them.

## Features

- **Recursive Directory Traversal:** Walk through all subdirectories.
- **Comprehensive File Type Handling:** Supports a wide range of text-based file extensions.
- **Configurable Text File Extensions:** Specify additional file extensions to treat as text files.
- **File Content Extraction:** Includes contents for text-based files.
- **Binary File Handling:** Identifies and lists binary or non-text files without attempting to read them.
- **Exclusion Filters:** Exclude specific directories or file types from the analysis.
- **Customizable Output:** Specify the output file name and target directory.
- **Progress Indicators:** Displays a progress bar while processing files.
- **Command-Line Interface:** Easy-to-use CLI with multiple options.
- **Verbose Logging:** Enable detailed logging for debugging purposes.

## Installation

You can install **ProjectCompactor** using `pip`:

```bash
pip install projectcompactor
