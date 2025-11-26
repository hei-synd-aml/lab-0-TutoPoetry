# Tutorial - Setting Up a Python Project with uv

![python env](./img/python_environment.png "Dependency hell")
Source: [xkcd](https://xkcd.com/1987/)

In this tutorial, you will be guided through the process of setting up a Python project using the `uv` package manager. The goal is to create a well-structured project that is easy to maintain and share with others (i.e., avoid "dependency hell", see picture above).
This tutorial is divided into three parts:
Part I - Installation: install Python, Git, and uv on your system (required for Part II and Part III).
Part II - Cloning an existing poject (created using uv): cloning the project, installing dependencies using uv and the pyproject.toml file.
Part III - Creating the Environment: create a new project using uv to manage dependences, modify the `pyproject.toml` file, install dependencies, and run a Jupyter notebook.

## Part I - Installation

In this section, you will install the necessary tools to create and manage Python projects using uv. This is necessary for the subsequent parts of the tutorial.
If you already have Python, Git, and uv installed, you can skip this section.

### Install Python

First, ensure that Python is installed on your system. In this tutorial, we will use Python 3.11.9. You can download it from the official website:

[Download Python 3.11.9](https://www.python.org/downloads/release/python-3119/)

During installation, make sure to:

- Check the box that says **"Add Python to PATH"**.
- *(Windows only)* Check the box that says **"Disable path length limit"**.

### Install Git

Git is a version control system that allows you to track changes in your codebase and collaborate with others.

Download and install the latest version of Git for your operating system from:

[Download Git](https://git-scm.com/downloads)

### Install uv

uv is a package manager for Python that simplifies dependency management and project structure. More information can be found on the official website:

[uv Official installation instructions](https://docs.astral.sh/uv/getting-started/installation/)

We suggest to install uv using the simplest method: via pip. If you want to install uv into an isolated environment or using other methods (such as via Homebrew on macOS), please refer to the official installation instructions linked above. The instructions below are for installing uv via pip and should work on Windows, macOS, and Linux.
Open a terminal (Command Prompt on Windows, Terminal on macOS and Linux) and run the following command:

```bash
pip install uv
```

To verify that uv is installed correctly, run the following command:

```bash
uv --version
```

**That's it!** You have successfully installed Python, Git, and uv on your system.

## Part II - Installing dependencies using uv and the pyproject.toml file

**NOTE**: you can test this section with the files provided in the folder "Test_UV_Part_II".

The goal of this section is to show how to use uv to install dependencies using poetry and the `pyproject.toml` file.
The typical scenario is when you clone a project from a repository that already has a `pyproject.toml` file with dependencies listed in it and you want to install them on a new machine.

*This is the typical workflow we will use in the Labs.*

Requirements: Git, Python and uv installed on your machine (see [Part I](#part-i---installation)).

1. Clone the project that you want to run from its repository using Git.

For example, to clone a project from GitHub/GirLab, run:

```bash
git clone <repository-url>
```

2. Navigate to the Project Directory.

Navigate to the project directory using the `cd` command:

```bash
cd <project-directory>
```

You should have the `pyproject.toml` file in the project directory.

3. Install Dependencies

Run the following command to install the project dependencies using Poetry:

```bash
uv sync
```

uv will read the `pyproject.toml` file and install the required dependencies in a virtual environment. Usually a `.venv` folder is created in the project directory.

**TROUBLESHOOTING**:
- Error during the `sync` process: you many encounter an error such "*failed to hardlink file from...*". This is a known issue with uv when synchronizing dependencies on folders located in certain file systems (e.g., OneDrive, network drives, etc.). To fix this issue:
    - Delete the `.venv` folder in the project directory (if it was created).
    - Delete the cache folder located at:
        - Windows: `C:\Users\<username>\AppData\Local\uv\cache`
        - macOS/Linux: `$HOME/.cache/uv`
    - Run the command `uv sync` again.

**That's it!** You have successfully installed the project dependencies using uv. Of course, you should also run the project to ensure everything is working as expected.
To add new dependencies to the project, you can use the `uv add` command followed by the package name, for example:

```bash
uv add numpy
```

to remove a package, use the `uv remove` command followed by the package name, for example:

```bash
uv remove numpy
```


4. Run the Project on PyCharm
    See the complete and updated guide here: [Configure a UV environment](https://www.jetbrains.com/help/pycharm/uv.html)
      
    Note: Once selected the right interpreter, especially for big projects, PyCharm may take some time to index all the files in the project. Wait for the indexing to finish. You can see the progress in the lower right corner of the PyCharm window. This may take a few minutes. Finally, run the project in PyCharm to ensure everything is working correctly.

5. Run the Project on Visual Studio Code
   
    5.1 Open Visual Studio Code and navigate to the project directory.
   
    5.2 Type `Ctrl+Shift+P` to open the command palette (on macOS, it's `Cmd+Shift+P`).
   
    5.3 Type "Python: Select Interpreter" and select the option.
   
    5.4 Click on "Enter interpreter path or browse" and paste the path to the virtual environment. It should be something like:
   
        - Windows: `path_to_the_lab_folder\.venv\Scripts\python.exe`
       
        - MacOS/Linux: `path_to_the_lab_folder/.venv/bin/python` (*to be tested*)
   

---

## Part III - Creating the Environment (OPTIONAL)

This part is **NOT** necessary for the Labs. 

If you just want to run a project that already has a `pyproject.toml` file, you are ready to go.

This part is useful if you want to *create* a new project from scratch or if you want to modify an existing project.

The goal of this section is to set up a virtual environment for your Machine Learning (ML) projects. Using uv, you can manage dependencies effectively, ensuring consistency across different systems and facilitating project sharing. This section is based on the official [web page](https://docs.astral.sh/uv/getting-started/features/#projects).

### Step 1: Create a New Project or initialising a pre-existing project

If you want to create a *new* project, navigate to your desired project directory and run:

```bash
uv init project_name
```

This command will create a new folder with the project name you provide, along with a `pyproject.toml` file to manage your dependencies, and a `readme.md` file.

If you do not want to create a new folder, you can run the command in the current directory without specifying a project name:

```bash
uv init
```

If you only want to create a pyproject.toml, use the `--bare` option:

```bash
uv init --bare
```


### Step 3: Install Dependencies

For our ML projects, we will install the following essential libraries (and some more):

- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`
- `seaborn`

Run the following command to install them:

```bash
uv add numpy pandas matplotlib scikit-learn seaborn ipykernel
```

uv will automatically manage dependencies and create a virtual environment for the project.
Additional dependences can be added using again the `uv add` command at later stage.


## Part IV - Troubleshooting

### 1. Pytorch with CUDA (TO DO)
This solution works for Windows (02.2024)

Open the .toml file and add the following lines:
```toml
[[tool.poetry.source]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cu118"
priority = "explicit"
```

Then run: 
```bash
poetry add torch==2.6.0+cu118 torchvision==0.21.0+cu118 torchaudio==2.6.0+cu118 --source pytorch
```

### 2. Poetry and Windows

After your run the command `poetry install`, you may encounter the following issue: 
```bash
Command '['C:\\Users\\yanni\\AppData\\Local\\Microsoft\\WindowsApps\\python.EXE', '-EsSc', 'import sys; print(sys.executable)']' returned non-zero exit status 9009.
```
This is a issue with Poetry and Windows. To fix it, you can try the following steps:

1. Open the command prompt as an administrator.
2. Run the command `poetry config virtualenvs.prefer-active-python true`.
3. Run the command `poetry config virtualenvs.in-project true`.
4. Run the command `poetry install` again.
5. If the issue persists, try running the command `poetry env use python` to set the Python interpreter for the virtual environment.


### 3. Poetry and PyCharm: jupyter server not found
If when running the first time the project in PyCharm, you get the error `jupyter server not found` (or something similar), usually is because the path to the virtual environment is too long. Be sure that:
- You have run the command `poetry config virtualenvs.in-project true`. 
- The virtual environment is created in the project folder (i.e., `path_to_the_lab_folder/.venv`).