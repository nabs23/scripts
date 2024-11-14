# Utility Scripts Collection

A collection of Python utility scripts for everyday tasks that help simplify and automate common actions for computer users. Each script is designed to handle a specific type of task, from file management to system monitoring, making life easier for users who need quick, efficient solutions.

## Table of Contents

- [Installation](#installation)
- [Available Scripts](#available-scripts)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nabs23/scripts
   cd scripts
   ```

2. (Optional) Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Available Scripts

| Script                        | Description |
| ----------------------------- | ----------- |
| **image_converter.py**        | Converts all `.webp` images in a folder to `.jpg`. |
| **bulk_renamer.py**           | Renames files in a directory according to a specified pattern. |
| **organize_by_extension.py**  | Organizes files in a folder into subfolders by file type. |
| **duplicate_finder.py**       | Finds and optionally deletes duplicate files based on content. |
| **folder_size_calculator.py** | Calculates the size of each folder in a specified directory. |
| **text_search.py**            | Searches for a keyword or phrase across text files in a directory. |
| **backup_script.py**          | Backs up specified files or folders to a target location with versioning. |
| **compression_tool.py**       | Compresses or decompresses files and folders. |
| **pdf_merger.py**             | Merges multiple PDF files into one document. |
| **system_info.py**            | Displays system information (CPU, memory, disk usage, etc.). |
| **image_resizer.py**          | Resizes all images in a folder to specified dimensions. |
| **temp_file_cleaner.py**      | Clears out temporary files in specified directories. |
| **webpage_screenshot.py**     | Captures a screenshot of a webpage from a given URL. |
| **clipboard_to_text.py**      | Saves clipboard content to a text file. |
| **bulk_url_downloader.py**    | Downloads files from a list of URLs. |

## Usage

Each script can be run independently. Simply navigate to the directory containing the script and execute it with Python.

Example:
```bash
python image_converter.py
```

### Script Descriptions

- **image_converter.py**: Converts all `.webp` images in the current folder to `.jpg` format and places them in a `jpg` subfolder.
- **bulk_renamer.py**: Prompts for a naming pattern and renames all files in the target folder.
- **duplicate_finder.py**: Scans a folder for duplicate files based on file content.
- **pdf_merger.py**: Accepts multiple PDF files as input and merges them into a single PDF file.

For detailed usage instructions, see the script’s header comments or use `--help` for options, where available.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or additional scripts.

## License

This project is licensed under the MIT License.


This README provides a structured overview for your collection of utility scripts, making it easy for other users to understand the purpose and use of each script in the repository.