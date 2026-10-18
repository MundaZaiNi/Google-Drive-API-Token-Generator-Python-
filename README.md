# Google Drive Token Generator (Python)

A beginner-friendly Python utility that authenticates with Google Drive using OAuth 2.0 and saves a local `token.pickle` file.

**Created by MundaZaini**

## Features
- Google OAuth 2.0 authentication
- Browser-based sign-in
- Local token generation
- Credential refresh when supported
- Windows, macOS, and Linux instructions
- Security-focused `.gitignore`

## Project Structure

```text
google-drive-token-generator/
├── generate_token.py
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

### Windows CMD
```cmd
python -m venv .venv
.venv\\Scripts\\activate
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

## Security
Never upload `credentials.json`, `token.pickle`, client secrets, access tokens, or refresh tokens to GitHub. `.gitignore` excludes real credential and token filenames.

Only load pickle files you created or trust; malicious pickle files can execute code.

## Official Documentation
- [Google Drive API Python Quickstart](https://developers.google.com/workspace/drive/api/quickstart/python)
- [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials)
- [Google Drive API Documentation](https://developers.google.com/workspace/drive/api)

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---

**Created by MundaZaini**
