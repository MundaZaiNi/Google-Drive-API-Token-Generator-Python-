Google Drive Token Generator (Python)

""Python" (https://img.shields.io/badge/Python-3.10%2B-blue.svg)" (https://www.python.org/)
""Google Drive API" (https://img.shields.io/badge/Google%20Drive-API-34A853.svg)" (https://developers.google.com/workspace/drive/api)
""License: MIT" (https://img.shields.io/badge/License-MIT-yellow.svg)" (LICENSE)

A simple Python utility to authenticate with the Google Drive API using OAuth 2.0 and generate a local "token.pickle" file.

✨ Features

- 🔐 Google OAuth 2.0 authentication
- 🌐 Browser-based Google login
- 🪙 Automatic local token generation
- ♻️ Reuses valid credentials and refreshes expired tokens when possible
- 💻 Windows, macOS and Linux support
- 🛡️ Security-focused ".gitignore"
- 📖 Beginner-friendly setup instructions

📁 Project Structure

google-drive-token-generator/
├── generate_token.py
├── requirements.txt
├── .gitignore
├── .env.example
├── LICENSE
└── README.md

File| Description
"generate_token.py"| Authenticates with Google and generates the token
"requirements.txt"| Lists required Python libraries
".gitignore"| Excludes private credentials and generated files
".env.example"| Configuration notes
"LICENSE"| MIT license
"README.md"| Project documentation

📋 Requirements

- Python 3.10 or newer
- A Google account
- A Google Cloud project
- Google Drive API enabled
- OAuth Client ID configured as Desktop app

⚙️ Installation

1. Clone the repository

git clone https://github.com/MundaZaini/google-drive-token-generator.git
cd google-drive-token-generator

«Replace the repository URL with your actual GitHub repository URL if you choose a different name.»

2. Create a virtual environment

Windows (CMD):

python -m venv .venv
.venv\Scripts\activate

macOS / Linux:

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

☁️ Google Cloud Setup

1. Open "Google Cloud Console Credentials" (https://console.cloud.google.com/apis/credentials).
2. Create or select a project.
3. Enable the "Google Drive API" (https://console.cloud.google.com/apis/library/drive.googleapis.com).
4. Configure Google Auth Platform and the OAuth consent screen.
5. Create an OAuth Client ID.
6. Select Desktop app as the application type.
7. Download the OAuth JSON file.
8. Rename it to "credentials.json".
9. Place it in the repository's root directory.

Testing Mode

If your OAuth application is in Testing mode, open Google Auth Platform → Audience → Test users and add the Google account you will use to sign in.

🚀 Generate Your Token

After placing "credentials.json" in the project folder, run:

python generate_token.py

A browser window should open.

1. Sign in to your Google account.
2. Review the requested permissions.
3. Approve access.
4. Wait for authentication to complete.

The script creates "token.pickle" in the project directory.

🔑 OAuth Scope

The default scope is:

https://www.googleapis.com/auth/drive

This grants broad access to Google Drive.

For read-only access, you can use:

https://www.googleapis.com/auth/drive.readonly

Change the scope in "generate_token.py" before authenticating. If you change scopes after creating a token, delete your local "token.pickle" and authenticate again.

🧰 Troubleshooting

"FileNotFoundError: credentials.json"

- Verify that the filename is exactly "credentials.json".
- Place it beside "generate_token.py".
- Confirm that the file belongs to your Desktop app OAuth client.

"Error 400: redirect_uri_mismatch"

- Confirm the OAuth client type is Desktop app, not Web application.
- Download the correct OAuth JSON file.
- Replace the old local "credentials.json".

"Error 403: access_denied"

- Open Google Auth Platform → Audience.
- Add your account under Test users if the application is in Testing mode.
- Save and retry authentication.

Dependency installation errors

Upgrade pip and use a supported Python version:

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

🔒 Security

Never commit or share these files:

- "credentials.json"
- "token.pickle"
- OAuth client secrets
- Access tokens or refresh tokens

These files are private. Each user must generate their own credentials and token.

Only load pickle files that you created or trust. A malicious pickle file can execute code when loaded.

The included ".gitignore" excludes common credential and token filenames. Always review files before publishing a public repository.

📚 Official Documentation

- "Google Drive API Python Quickstart" (https://developers.google.com/workspace/drive/api/quickstart/python)
- "Google Cloud Credentials" (https://console.cloud.google.com/apis/credentials)
- "Google Drive API Documentation" (https://developers.google.com/workspace/drive/api)

📄 License

This project is licensed under the MIT License. See "LICENSE" (LICENSE) for details.

---

👨‍💻 Author

MundaZaini
