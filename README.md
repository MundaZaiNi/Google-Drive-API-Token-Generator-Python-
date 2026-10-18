# Google Drive Token Generator (Python)

A beginner-friendly Python utility that authenticates with Google Drive using OAuth 2.0 and saves a local `token.pickle` file.

**Created by MundaZaini**

## Features
- Google OAuth 2.0 authentication
- Browser-based sign-in
- Local token generation
- Credential refresh when supported
- Windows, macOS, and Linux instructions
- Optional Windows BAT setup
- Security-focused `.gitignore`

## Project Structure

```text
google-drive-token-generator/
├── generate_token.py
├── setup_google_drive_token.bat
├── requirements.txt
├── credentials.example.json
├── token.pickle.example.md
├── .gitignore
├── LICENSE
└── README.md
```

## Requirements
- Python 3.10 or newer
- A Google account
- A Google Cloud project with Google Drive API enabled
- OAuth Client ID with application type **Desktop app**

## 1. Google Cloud Setup
1. Open [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials).
2. Create or select a project.
3. Enable the [Google Drive API](https://console.cloud.google.com/apis/library/drive.googleapis.com).
4. Configure Google Auth Platform if prompted.
5. Create an OAuth Client ID and select **Desktop app**.
6. Download the JSON credentials file and save a private local copy as `credentials.json` beside `generate_token.py`.

If the app is in Testing mode, add your account under **Google Auth Platform → Audience → Test users**.

## 2. Install Dependencies

### Option A: Windows BAT setup

The optional `setup_google_drive_token.bat` script installs the required libraries, checks for `credentials.json`, and runs `generate_token.py`.

1. Put `setup_google_drive_token.bat`, `generate_token.py`, and `requirements.txt` in the same project folder.
2. Download your real OAuth Desktop app JSON and save it in that folder as `credentials.json`.
3. Double-click `setup_google_drive_token.bat`.
4. Follow the prompts and complete Google sign-in in your browser.

The BAT file normally does not need Administrator permission when Python is installed for your user and the project folder is writable. If Python or pip is unavailable, fix that installation first rather than automatically elevating the script.

Example BAT file:

```bat
@echo off
setlocal
title Google Drive Token Generator
cd /d "%~dp0" || (
    echo ERROR: Could not open the project folder.
    pause
    exit /b 1
)

if not exist "generate_token.py" (
    echo ERROR: generate_token.py was not found in this folder.
    pause
    exit /b 1
)

if not exist "requirements.txt" (
    echo ERROR: requirements.txt was not found in this folder.
    pause
    exit /b 1
)

echo Installing required Python libraries...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo WARNING: pip upgrade failed; trying to install requirements anyway.
)

python -m pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Dependency installation failed.
    pause
    exit /b 1
)

if not exist "credentials.json" (
    echo ERROR: credentials.json was not found.
    echo Save your OAuth Desktop app JSON beside this BAT file.
    pause
    exit /b 1
)

echo.
echo Starting Google Drive authentication...
python generate_token.py
if errorlevel 1 (
    echo.
    echo ERROR: Token generation failed. Review the message above.
)
echo.
pause
endlocal
```

### Option B: Windows CMD (manual)

Run these commands in the project folder:

```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. Generate the Token

Make sure your real `credentials.json` is beside `generate_token.py`, then run:

```bash
python generate_token.py
```

A browser should open. Sign in and approve the requested permissions. The script saves `token.pickle` locally.

## Demo Files
- `credentials.example.json` contains placeholders only and will not authenticate.
- `token.pickle.example.md` explains the token generation process; it is not a real token file.

## Troubleshooting

### `FileNotFoundError: credentials.json`
Copy your real downloaded Desktop app OAuth JSON into this folder and name it `credentials.json`.

### `Error 400: redirect_uri_mismatch`
Use a **Desktop app** OAuth client, not a Web application client.

### `Error 403: access_denied`
If the app is in Testing mode, add your account under **Audience → Test users**.

### `python` is not recognized
Install Python and enable the option to add Python to PATH. Open a new terminal after installation.

## Security
Never upload `credentials.json`, `token.pickle`, client secrets, access tokens, or refresh tokens to GitHub. `.gitignore` should exclude real credential and token filenames.

Only load pickle files you created or trust; malicious pickle files can execute code.

## Official Documentation
- [Google Drive API Python Quickstart](https://developers.google.com/workspace/drive/api/quickstart/python)
- [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials)
- [Google Drive API Documentation](https://developers.google.com/workspace/drive/api)

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---

**Created by MundaZaini**
