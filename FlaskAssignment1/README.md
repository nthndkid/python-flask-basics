# Assignment 1: Using virtual environment

### Ensure you have python installed

1. Go to `Microsoft Store` and download `Python 3.13`.
2. Once installed, verify if it works. Open terminal or powershell and type the code below:

    ```powershell
    python --version
    ```

    The output should be `Python 3.13.2`.

### Make a virtual env

1. Open terminal or powershell.
2. Use the `cd` command to navigate to your folder. Use `ls` to list contents of a folder. `cd ..` to go back to the parent directory of the current folder.

    ```powershell
    PS C:\Users\admin> ls


        Directory: C:\Users\admin


    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d-----         2/15/2025  11:25 AM                .ssh
    d-----         2/15/2025  11:24 AM                .vscode
    d-r---         2/12/2025   4:12 PM                Contacts
    d-r---         2/12/2025   4:12 PM                Desktop
    d-r---         2/15/2025  11:25 AM                Documents
    d-r---         2/15/2025  11:23 AM                Downloads
    d-r---         2/12/2025   4:12 PM                Favorites
    d-r---         2/12/2025   4:12 PM                Links
    d-r---         2/12/2025   4:12 PM                Music
    d-r---         2/12/2025   4:14 PM                OneDrive
    d-r---         2/12/2025   7:55 PM                Pictures
    d-r---         2/12/2025   4:12 PM                Saved Games
    d-r---         2/12/2025   4:32 PM                Searches
    d-r---         2/14/2025   6:20 PM                Videos
    -a----         2/15/2025  11:47 AM              7 .python_history


    PS C:\Users\admin> cd .\Documents\
    PS C:\Users\admin\Documents> ls


        Directory: C:\Users\admin\Documents


    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d-----         2/12/2025   4:31 PM                Dell
    d-----         2/15/2025  11:25 AM                Development


    PS C:\Users\admin\Documents> cd .\Development\
    PS C:\Users\admin\Documents\Development> ls


        Directory: C:\Users\admin\Documents\Development


    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d-----         2/15/2025  11:27 AM                gdg-python-flask


    PS C:\Users\admin\Documents\Development> cd .\gdg-python-flask\
    PS C:\Users\admin\Documents\Development\gdg-python-flask> ls


        Directory: C:\Users\admin\Documents\Development\gdg-python-flask


    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d-----         2/15/2025  11:44 AM                FlaskAssignment1
    -a----         2/15/2025  11:52 AM           2122 README.md


    PS C:\Users\admin\Documents\Development\gdg-python-flask> cd .\FlaskAssignment1\
    PS C:\Users\admin\Documents\Development\gdg-python-flask\FlaskAssignment1> ls


        Directory: C:\Users\admin\Documents\Development\gdg-python-flask\FlaskAssignment1


    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    -a----         2/15/2025  11:44 AM              0 app.py
    -a----         2/15/2025  11:55 AM           2886 README.md
    ```

3. Make the virtual env.

    ```powershell
    python -m venv .venv
    ```

4. Configure Windows to bypass execution policy. Run `Windows Powershell` as Administrator. Type the following code:


    ```powershell
    Windows PowerShell
    Copyright (C) Microsoft Corporation. All rights reserved.

    Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

    PS C:\WINDOWS\system32> Set-ExecutionPolicy Bypass

    Execution Policy Change
    The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
    you to the security risks described in the about_Execution_Policies help topic at
    https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
    [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): a
    PS C:\WINDOWS\system32>
    ```

5. Now that you have permission to run scripts, activate the python virtual environment. Ensure your current directory is in `./FlaskAssignment1/`.

    ```powershell
    PS C:\Users\admin\Documents\Development\gdg-python-flask\FlaskAssignment1> .\.venv\Scripts\activate
    (.venv) PS C:\Users\admin\Documents\Development\gdg-python-flask\FlaskAssignment1>
    ```

    You'll notice that the succeeding commands will have `(.venv)` in front. This means that we are using the virtual environment correctly.

6. Install Flask.

    ```powershell
    (.venv) PS C:\Users\admin\Documents\Development\gdg-python-flask\FlaskAssignment1> pip install Flask
    Collecting Flask
    Downloading flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
    Collecting Werkzeug>=3.1 (from Flask)
    Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
    Collecting Jinja2>=3.1.2 (from Flask)
    Downloading jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
    Collecting itsdangerous>=2.2 (from Flask)
    Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
    Collecting click>=8.1.3 (from Flask)
    Downloading click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
    Collecting blinker>=1.9 (from Flask)
    Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
    Collecting colorama (from click>=8.1.3->Flask)
    Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
    Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask)
    Downloading MarkupSafe-3.0.2-cp313-cp313-win_amd64.whl.metadata (4.1 kB)
    Downloading flask-3.1.0-py3-none-any.whl (102 kB)
    Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
    Downloading click-8.1.8-py3-none-any.whl (98 kB)
    Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
    Downloading jinja2-3.1.5-py3-none-any.whl (134 kB)
    Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
    Downloading MarkupSafe-3.0.2-cp313-cp313-win_amd64.whl (15 kB)
    Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
    Installing collected packages: MarkupSafe, itsdangerous, colorama, blinker, Werkzeug, Jinja2, click, Flask
    Successfully installed Flask-3.1.0 Jinja2-3.1.5 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 colorama-0.4.6 itsdangerous-2.2.0

    [notice] A new release of pip is available: 24.3.1 -> 25.0.1
    [notice] To update, run: python.exe -m pip install --upgrade pip
    (.venv) PS C:\Users\admin\Documents\Development\gdg-python-flask\FlaskAssignment1>
    ```

### Run the Flask app

1. Type the following:

    ```powershell
    python app.py
    ```

    And, open the link in a browser: `http://localhost:5000`.


### Exit virtual environment

1. Type the following:

    ```powershell
    deactivate
    ```

    By doing so, you will not be able to run the Flask app. Execute `.\.venv\Scripts\activate` again to open the virtual environment with Flask installed.