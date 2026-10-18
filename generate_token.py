import pickle
from pathlib import Path
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/drive"]
BASE_DIR = Path(__file__).resolve().parent
CREDENTIALS_FILE = BASE_DIR / "credentials.json"
TOKEN_FILE = BASE_DIR / "token.pickle"

def main():
    if not CREDENTIALS_FILE.is_file():
        raise FileNotFoundError(
            "credentials.json not found. Copy credentials.example.json to "
            "credentials.json and replace demo placeholders with your real "
            "Google OAuth Desktop app credentials."
        )

    creds = None
    if TOKEN_FILE.is_file():
        try:
            with TOKEN_FILE.open("rb") as f:
                creds = pickle.load(f)  # Only load pickle files you trust.
        except (pickle.UnpicklingError, EOFError, OSError):
            print("Existing token could not be read; starting new login.")
            creds = None

    if creds and creds.valid:
        print(f"Valid token already exists: {TOKEN_FILE}")
        return

    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
        except Exception as exc:
            print(f"Token refresh failed ({exc}); starting new login.")
            creds = None

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            str(CREDENTIALS_FILE), SCOPES
        )
        creds = flow.run_local_server(
            host="127.0.0.1", port=0, open_browser=True
        )

    with TOKEN_FILE.open("wb") as f:
        pickle.dump(creds, f)

    print("Google authentication successful.")
    print(f"Token saved locally: {TOKEN_FILE}")
    print("Never upload credentials.json or token.pickle to GitHub.")

if __name__ == "__main__":
    main()
