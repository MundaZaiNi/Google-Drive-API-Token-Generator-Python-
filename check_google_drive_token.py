import os
import pickle
from datetime import timezone

BASE = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = os.path.join(BASE, "token.pickle")

if not os.path.isfile(TOKEN_FILE):
    print("ERROR: token.pickle nahi mili.")
    print("Script ko token.pickle ke same folder mein rakho.")
    raise SystemExit(1)

try:
    with open(TOKEN_FILE, "rb") as f:
        creds = pickle.load(f)
except Exception as exc:
    print("ERROR: Token file load nahi hui.")
    print("File corrupt ho sakti hai ya compatible nahi hai.")
    print("Error type:", type(exc).__name__)
    raise SystemExit(1)

print("Token file loaded successfully!")
print("Credentials valid:", creds.valid)
print("Refresh token available:", bool(creds.refresh_token))

if creds.expiry:
    expiry = creds.expiry
    if expiry.tzinfo is None:
        expiry = expiry.replace(tzinfo=timezone.utc)
    print("Expiry (UTC):", expiry.isoformat())
else:
    print("Expiry information unavailable.")

print("Secret token details security ke liye hide rakhe gaye hain.")
