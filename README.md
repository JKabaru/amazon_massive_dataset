
# amazon_massive_dataset

Brief project description.

## Table of Contents
- [Dependencies](#dependencies)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Dependencies

Ensure you have the following dependencies installed:
- Python 3.x
- Pandas: You can install it using pip with `pip install pandas`
- openpyxl: Used to read and write Excel files. You can install it using the command `pip install openpyxl`

Dependecies that are **pre-installed** in Python include:
- Tarfile: a standard library module in Python that provides the ability to read and create tar archives, it is also used in Unix and Linux systems to bundle files together into a single archive i.e **Amazon massive data file**
- argparse: A starndard Python library module that provides an easy and flexible way to handle command-line arguments in your scripts or programs
- os: A standard Python library that provides a portable way of interacting with the operating system, allowing you to perform various tasks related to file and directory operations, process management, path manipulation, runnin shell commands and more
- json: Provides functions for encoding and decoding JSON(JavaScript Object Notation) data. JSON is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate
  
## Getting Started

Clone the repository to get started:

```bash
git clone https://github.com/your-username/your-project.git
cd your-project
```

## Usage

Describe how to use your project here. Provide examples and usage instructions.

## Configuration

To configure the project for your specific environment, you may need to make the following changes:

1. **Import and Extract the Amazon massive data file**: Declare the file path and use the tarfile library to extract content from the **Amazon Massive Data file** into an already created directory.

2. **Data Directory**: Update the `data_directory` variable in the code to point to the directory containing your JSONL files.
   
   ```python
   data_directory = r'path/to/your/data_directory'
   ```

3. **Output Directory**: Update the `output_dir` variable to specify where you want to save the generated Excel files.
   
   ```python
   output_dir = r'path/to/your/output_directory'
   ```

4. **Keyword and Field**: When running the script, you can specify the keyword and field for filtering using the `--keyword` and `--field` arguments.
   
   ```shell
   python script_name.py --keyword your_keyword --field your_field
   ```
