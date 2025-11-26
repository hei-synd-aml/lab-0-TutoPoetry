1. Test the code in this folder (main.py). It requires a module called "numpy".
2. Use uv to automatically install it running `uv sync` in the terminal.
3. Select the Python interpreter from the created uv virtual environment. It should be located in a `.venv` folder in the project directory (this directory).
    3.1 In VS Code:
        3.1.1 Open the command palette (Ctrl+Shift+P), then type and select "Python: Select Interpreter".
        3.1.2 Choose the interpreter located in the `.venv` folder. The path should look like `<project_path>/.venv/Scripts/python.exe` on Windows or `<project_path>/.venv/bin/python` on macOS/Linux.
    3.2 In PyCharm:
        3.2.1 Go to File > Settings > Project: <project_name> > Python Interpreter.
        3.2.2 Click on the gear icon and select "Add".
        3.2.3 Choose "Existing environment" and navigate to the Python interpreter located in the `.venv` folder.

4. Run the code in the main.py file to verify that it works.