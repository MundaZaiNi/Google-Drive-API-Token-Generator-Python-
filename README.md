Google Drive Token Generator (Python)

""Python" (https://img.shields.io/badge/Python-3.10%2B-blue.svg)" (https://www.python.org/)
""Google Drive API" (https://img.shields.io/badge/Google%20Drive-API-34A853.svg)" (https://developers.google.com/workspace/drive/api)
""License: MIT" (https://img.shields.io/badge/License-MIT-yellow.svg)" (LICENSE)

A beginner-friendly Python utility to authenticate with Google Drive API using OAuth 2.0 and generate a local "token.pickle" file.

✨ Features

- Google OAuth 2.0 authentication
- Browser-based Google login
- Automatic token generation
- Credential refresh when supported
- Windows, macOS, and Linux support
- Security-focused ".gitignore"
- Beginner-friendly documentation

📁 Project Structure

google-drive-token-generator/
├── generate_token.py
├── requirements.txt
├── .gitignore
├── .env.example
├── LICENSE
└── README.md

📋 File Descriptions

File| Description
"generate_token.py"| Authenticates with Google and generates the token
"requirements.txt"| Lists required Python libraries
".gitignore"| Excludes private credentials and generated files
".env.example"| Contains configuration notes
"LICENSE"| MIT open-source license
"README.md"| Project documentation

📌 Requirements

- Python 3.10 or newer
- A Google account
- A Google Cloud project
- Google Drive API enabled
- OAuth Client ID configured as Desktop app

⚙️ Installation

1. Clone the repository

Replace "YOUR_USERNAME" with your GitHub username.

git clone https://github.com/YOUR_USERNAME/google-drive-token-generator.git
cd google-drive-token-generator

2. Create a virtual environment

Windows CMD:

python -m venv .venv
.venv\Scripts\activate

macOS / Linux:

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

☁️ Google Cloud Setup

1. Open "Google Cloud Credentials" (https://console.cloud.google.com/apis/credentials).
2. Create or select a project.
3. Enable the "Google Drive API" (https://console.cloud.google.com/apis/library/drive.googleapis.com).
4. Configure Google Auth Platform and the OAuth consent screen.
5. Create an OAuth Client ID.
6. Select Desktop app as the application type.
7. Download the JSON credentials file.
8. Rename it to "credentials.json".
9. Place it beside "generate_token.py".

Testing mode: If your app is in Testing mode, add your Google account under Google Auth Platform → Audience → Test users.

🚀 Generate Your Token

Run the following command from the project folder:

python generate_token.py

Your browser should open.

1. Sign in with your Google account.
2. Review the requested permissions.
3. Approve access to Google Drive.
4. Wait for authentication to finish.

The script saves "token.pickle" in the project folder.

🔑 OAuth Permissions

The default scope is:

"https://www.googleapis.com/auth/drive"

This grants broad Google Drive access.

For read-only access, use:

"https://www.googleapis.com/auth/drive.readonly"

Change the scope in "generate_token.py" before authenticating. If you change scopes after generating a token, delete your local "token.pickle" and authenticate again.

🛠️ Troubleshooting

"FileNotFoundError: credentials.json"

- Check the filename.
- Put the file beside "generate_token.py".
- Use credentials from a Desktop app OAuth client.

"Error 400: redirect_uri_mismatch"

- Confirm the client type is Desktop app, not Web application.
- Download the correct OAuth JSON file.
- Replace the old local "credentials.json".

"Error 403: access_denied"

- Open Google Auth Platform → Audience.
- Add your account under Test users if the app is in Testing mode.
- Save and retry authentication.

Package installation errors

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Use a supported Python version and a virtual environment.

🔒 Security

Never upload these files to a public repository:

- "credentials.json"
- "token.pickle"
- OAuth client secrets
- Access tokens or refresh tokens

Each user must create their own OAuth credentials and token.

Only load pickle files that you created or trust. A malicious pickle file can execute code when loaded.

The included ".gitignore" excludes common credentials and generated token files. Always review files before publishing.

📚 Official Documentation

- "Google Drive API Python Quickstart" (https://developers.google.com/workspace/drive/api/quickstart/python)
- "Google Cloud Credentials" (https://console.cloud.google.com/apis/credentials)
- "Google Drive API Documentation" (https://developers.google.com/workspace/drive/api)

📄 License

This project is licensed under the MIT License. See "LICENSE" (LICENSE) for details.

---

👨‍💻 Author

MundaZaini
