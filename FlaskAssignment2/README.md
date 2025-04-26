# Assignment 2: Pip freeze

#### ⚠️ Finish Assignment 1 first before proceeding

### Create virtual env

1. Go to this folder `./FlaskAssignment2/`
2. Create virtual env

    ```powershell
    python -m venv .venv
    ```

### Activate virtual env

1. Deactivate the virtual env if it is still active

    ```powershell
    deactivate
    ```

2. Type the following:

    ```powershell
    .\.venv\Scripts\activate
    ```

### Install Flask 

1. Type the follwing:

    ```powershell
    pip install Flask
    ```

### Make the requirements.txt

1. Type the following:

    ```powershell
    pip freeze > requirements.txt
    ```

    This would list all the python dependencies you installed in the virtual environment and write it to `requirements.txt`.

### Experiment

1. Ensure the virtual env is still active. List all python dependencies in the virtual env.

    ```powershell
    pip list
    ```
2. Deactivate virtual env.

    ```powershell
    deactivate
    ```

3. Delete `.venv` from this folder `./FlaskAssignment2`.

    ```powershell
    rm .venv
    ```

4. Create a new virtual env.

    ```powershell
    python -m venv .venv
    ```

5. Activate virtual env

    ```powershell
    .\.venv\Scripts\activate
    ```

6. Verify that Flask is not installed

    ```powershell
    pip list
    ```

    In my case, the output is:

    ```powershell
    (.venv) PS C:\Users\admin\Documents\Development\gdg-python-flask\FlaskAssignment2> pip list
    Package Version
    ------- -------
    pip     24.3.1
    (.venv) PS C:\Users\admin\Documents\Development\gdg-python-flask\FlaskAssignment2>
    ```

7. Instead of doing `pip install Flask` we will use the `requirements.txt` generated from our deleted virtual env. By doing so, we won't need to type all python dependencies one by one.

    ```powershell
    pip install -r requirements.txt
    ```

8. Run the Flask app.

    ```powershell
    python app.py
    ```