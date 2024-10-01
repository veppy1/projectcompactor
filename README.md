# ProjectCompactor 🚀

[![PyPI Version](https://badge.fury.io/py/projectcompactor.svg)](https://pypi.org/project/projectcompactor/)
[![GitHub Stars](https://img.shields.io/github/stars/veppy/projectcompactor.svg?style=social&label=Star)](https://github.com/veppy1/projectcompactor)
[![License](https://img.shields.io/github/license/veppy/projectcompactor.svg)](LICENSE)
[![Build Status](https://img.shields.io/github/actions/workflow/status/veppy/projectcompactor/ci.yml?branch=main)](https://github.com/veppy1/projectcompactor/actions)

## 📦 Overview

**ProjectCompactor** is a powerful, user-friendly Python tool designed to **generate comprehensive project trees** and **extract detailed file contents** from any directory. Whether you're a developer, project manager, or enthusiast, ProjectCompactor streamlines the process of documenting and analyzing your project structure, making it easier to understand, share, and maintain your codebase.

## 🌟 Key Features

- **🔍 Comprehensive Project Tree Generation**
  - Automatically traverses directories to create a detailed hierarchical tree structure.
  - Visualizes the entire project layout with proper indentation for easy readability.

- **📄 Detailed File Content Extraction**
  - Extracts and includes contents of text-based files (e.g., `.py`, `.html`, `.txt`, `.md`).
  - Identifies binary or non-text files (e.g., `.png`, `.jpg`, `.exe`) and lists them without attempting to read their contents.

- **⚙️ Highly Configurable**
  - **Customizable File Extensions**: Specify additional file types to treat as text files.
  - **Exclusion Filters**: Exclude specific directories or file types from the analysis.
  - **Verbose Logging**: Enable detailed logging for troubleshooting and insights.

- **🚀 Efficient and Fast**
  - Utilizes multi-threading for concurrent file processing, ensuring quick execution even for large projects.
  - Progress indicators with `tqdm` provide real-time feedback during operation.

- **🛠️ Easy to Use Command-Line Interface**
  - Simple commands to generate project structures with optional parameters for customization.
  - Output can be directed to a specified file for easy sharing and documentation.

- **📈 SEO-Friendly Documentation**
  - Generates structured and detailed documentation ideal for project analysis and onboarding.

## 📋 Installation

Install **ProjectCompactor** easily using `pip`:

```bash
pip install projectcompactor
```
Ensure you have Python 3.6 or higher installed.

## 🖥️ Usage

After installation, you can use the `projectcompactor` command directly from your terminal.

### Basic Command

Generate a project structure of the current directory:

```bash
projectcompactor
```

Specify a Directory
Analyze a specific directory:

```bash
projectcompactor /path/to/your/project
```

Customize Output File
Specify a custom output file name:

```bash
projectcompactor -o my_structure.txt
```

Add Additional Text File Extensions
Include additional file extensions to treat as text files:

```bash
projectcompactor -e .rst .conf
```

Exclude Specific Directories and File Types
Exclude directories like node_modules and file types like .log:

```bash
projectcompactor --exclude-dirs node_modules .git --exclude-files .log .tmp
```

Enable Verbose Logging
Get detailed logs during execution:

```bash
projectcompactor -v
```

Full Example
Combine multiple options for a comprehensive analysis:
```bash
projectcompactor /path/to/your/project -o project_structure.txt -e .rst .conf --exclude-dirs node_modules .git --exclude-files .log .tmp -v
```


📂 Sample Output
Project Structure Section
```bash
# Project Structure

project/
    README.md
    src/
        main.py
        utils.py
    assets/
        logo.png
        styles.css
```


File Details Section
```bash
# File Details

## README.md
### Contents of README.md
# Sample Project
This is a sample project.

## src/main.py
### Contents of main.py
print("Hello, World!")

## src/utils.py
### Contents of utils.py
def helper():
    pass

## assets/logo.png
[Binary or Non-text file: logo.png]

## assets/styles.css
### Contents of styles.css
body { margin: 0; padding: 0; }
```

🎯 Use Cases
📚 Project Documentation
🔍 Uploading to Chat Assistant
🗃️ Archiving Projects
📊 Reporting