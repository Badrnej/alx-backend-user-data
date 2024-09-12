# Flask API Project

## Resources
To complete this project, you should familiarize yourself with the following resources:

- [Flask documentation](https://flask.palletsprojects.com/)
- [Requests module](https://docs.python-requests.org/en/latest/)
- [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without the help of Google:

- How to declare API routes in a Flask app
- How to get and set cookies in Flask
- How to retrieve request form data
- How to return various HTTP status codes from your Flask app

## Requirements
- **Editors**: Allowed editors are `vi`, `vim`, and `emacs`.
- **Environment**: All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- **File Format**:
  - All files should end with a new line.
  - The first line of all Python files should be exactly `#!/usr/bin/env python3`.
- **README**: A `README.md` file at the root of the project folder is mandatory.
- **Coding Style**: 
  - Your code should follow the `pycodestyle` style guide (version 2.5).
  - SQLAlchemy version must be `1.3.x`.
- **File Execution**: All files must be executable.
- **Documentation**:
  - All modules, classes, and functions should have proper documentation explaining their purpose.
  - You can test documentation length using:
    ```bash
    python3 -c 'print(__import__("my_module").__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    ```
- **Type Annotations**: All functions should be type-annotated.
- **Architecture**:
  - The Flask app should only interact with the `Auth` class and should not directly interact with the database.
  - Only public methods of `Auth` and `DB` classes should be used outside these classes.

## Setup
You will need to install `bcrypt` for password hashing. To install, run:

```bash
pip3 install bcrypt

