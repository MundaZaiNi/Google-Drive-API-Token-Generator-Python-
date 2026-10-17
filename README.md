Google Drive API Token Generator (Python)

A beginner-friendly Python project to authenticate with the Google Drive API and generate a local "token.pickle" file using Google's OAuth 2.0 authentication.

Created for developers who want to connect their Python applications to Google Drive.

Features

- Google OAuth 2.0 authentication
- Automatic browser-based login
- Generates "token.pickle" locally
- Reuses valid credentials
- Refreshes expired credentials when possible
- Windows, macOS and Linux setup instructions
- Troubleshooting for common OAuth errors
- Security-focused ".gitignore"

Project Structure

google-drive-token-generator/
├── generate_token.py
├── requirements.txt
├── .gitignore
├── .env.example
├── LICENSE
└── README.md

File Description

- "generate_token.py" — Main Python script for Google authentication and token generation.
- "requirements.txt" — Required Python libraries.
- ".gitignore" — Prevents credentials and token files from being committed.
- ".env.example" — Example configuration notes.
- "LICENSE" — MIT open-source license.
- "README.md" — Project documentation and setup instructions.

Requirements

- Python 3.10 or newer
- A Google account
- A Google Cloud project
- Google Drive API enabled
- OAuth Client ID with application type Desktop app

Step 1: Configure Google Cloud

1. Open "Google Cloud Console Credentials" (https://console.cloud.google.com/apis/credentials).
2. Create or select a Google Cloud project.
3. Enable the "Google Drive API" (https://console.cloud.google.com/apis/library/drive.googleapis.com).
4. Configure Google Auth Platform and the OAuth consent screen.
5. Create an OAuth Client ID.
6. Select Desktop app as the application type.
7. Download the JSON credentials file.
8. Rename it to "credentials.json".
9. Place it in the same folder as "generate_token.py".

Important: If your application is in Testing mode, add your Google account under Google Auth Platform → Audience → Test users.

Step 2: Install Dependencies

Windows

Open Command Prompt and run:

cd /d "C:\Google API"
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Replace "C:\Google API" if your project is located in a different folder.

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Step 3: Generate the Token

Make sure "credentials.json" is present in your project folder.

Run:

python generate_token.py

Your browser should open automatically.

1. Select your Google account.
2. Review the requested permissions.
3. Approve access to Google Drive.
4. Wait for the authentication process to finish.

After successful authentication, "token.pickle" will be created locally.

OAuth Permissions

The default scope used by this project is:

https://www.googleapis.com/auth/drive

This scope provides broad Google Drive access.

For read-only applications, you can instead use:

https://www.googleapis.com/auth/drive.readonly

Choose the narrowest scope that meets your application's requirements. If you change scopes after generating a token, remove your local "token.pickle" and authenticate again.

Troubleshooting

FileNotFoundError: credentials.json

Make sure the credentials file:

- Is named exactly "credentials.json".
- Is in the same folder as "generate_token.py".
- Belongs to an OAuth client of type Desktop app.

Error 400: redirect_uri_mismatch

- Check that the OAuth client type is Desktop app, not Web application.
- Download the correct Desktop app credentials JSON.
- Replace the old local "credentials.json" file.

Error 403: access_denied

If your OAuth application is in Testing mode:

1. Open Google Auth Platform.
2. Select Audience.
3. Add your Google account under Test users.
4. Save the changes and try authentication again.

Browser Does Not Open

Check that your system has a default browser installed. Keep the Python script running while completing authentication.

Package Installation Errors

Upgrade pip and try again:

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Use a supported Python version and a virtual environment when possible.

Security Guidelines

- Never upload "credentials.json" to GitHub.
- Never upload "token.pickle" to GitHub.
- Never share OAuth client secrets, access tokens or refresh tokens.
- Only load pickle files that you created or trust.
- Use the narrowest OAuth permissions required.
- Revoke Google account access if your credentials are exposed.

The included ".gitignore" excludes common credentials and generated token files.

Official Documentation

- "Google Drive API Python Quickstart" (https://developers.google.com/workspace/drive/api/quickstart/python)
- "Google Cloud Credentials" (https://console.cloud.google.com/apis/credentials)
- "Google Drive API Documentation" (https://developers.google.com/workspace/drive/api)

License

This project is distributed under the MIT License. See the "LICENSE" file for details.

---

Created by MundaZaini
