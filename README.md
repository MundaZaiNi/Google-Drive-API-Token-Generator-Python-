# Google Drive Token Generator (Python)

A simple Python utility that authenticates with Google Drive using OAuth 2.0 and saves a local `token.pickle` file.

**Created by MundaZaini**

## Features

- Google OAuth 2.0 authentication
- Browser-based sign-in
- Local token generation
- Credential refresh when supported
- Windows, macOS, and Linux instructions
- Security-focused `.gitignore`

## Project Files

- `generate_token.py` — Authenticates with Google and saves the token.
- `requirements.txt` — Lists required Python packages.
- `.gitignore` — Excludes private credentials and generated token files.
- `.env.example` — Configuration notes.
- `LICENSE` — MIT license.
- `README.md` — Project documentation.

## Requirements

- Python 3.10 or newer
- A Google account
- A Google Cloud project
- Google Drive API enabled
- OAuth Client ID with application type **Desktop app**

## 1. Google Cloud Setup

1. Open [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials).
2. Create or select a project.
3. Enable the [Google Drive API](https://console.cloud.google.com/apis/library/drive.googleapis.com).
4. Configure Google Auth Platform if prompted.
5. Create an OAuth Client ID and select **Desktop app**.
6. Download the JSON credentials file.
7. Rename it to `credentials.json` and put it beside `generate_token.py`.

If the app is in Testing mode, add your account under **Google Auth Platform → Audience → Test users**.

## 2. Install on Windows

Open Command Prompt in the project folder and run:

```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. Install on macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 4. Generate the Token

Make sure `credentials.json` is in the same folder as `generate_token.py`, then run:

```bash
python generate_token.py
```

A browser should open. Sign in with your Google account and approve the requested permissions. After successful authentication, `token.pickle` is saved in the project folder.

## OAuth Scope

The default scope is:

`https://www.googleapis.com/auth/drive`

This grants broad Drive access. For read-only access, change the scope in the script to:

`https://www.googleapis.com/auth/drive.readonly`

If you change scopes after creating a token, delete your local `token.pickle` and authenticate again.

## Troubleshooting

### `FileNotFoundError: credentials.json`

Check that the file is named exactly `credentials.json` and is in the same folder as the script.

### `Error 400: redirect_uri_mismatch`

Use a **Desktop app** OAuth client, not a Web application client. Download the matching JSON file again.

### `Error 403: access_denied`

If the app is in Testing mode, add the Google account you use to sign in under **Audience → Test users**.

### Package installation errors

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Security

Never upload these files to a public repository:

- `credentials.json`
- `token.pickle`
- OAuth client secrets
- Access tokens or refresh tokens

Each user must create their own OAuth credentials and token. Only load pickle files you created or trust, because malicious pickle files can execute code.

## Official Documentation

- [Google Drive API Python Quickstart](https://developers.google.com/workspace/drive/api/quickstart/python)
- [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials)
- [Google Drive API Documentation](https://developers.google.com/workspace/drive/api)

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

**Created by MundaZaini**
