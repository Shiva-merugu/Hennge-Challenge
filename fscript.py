import pyotp
import hashlib
import base64
import requests
import json

# =========================
# 🔧 EDIT THESE 2 VALUES
# =========================
email = "shivamerugu8074@gmail.com"
github_url = "https://gist.github.com/Shiva-merugu/28209d02a82ac636e946bb243557f6fe"

# =========================
# Step 1: Generate TOTP
# =========================
secret = email + "HENNGECHALLENGE004"

totp = pyotp.TOTP(
    secret,
    digits=10,
    interval=30,
    digest=hashlib.sha512
)

otp = totp.now()
print("OTP:", otp)

# =========================
# Step 2: Encode Authorization
# =========================
auth_string = f"{email}:{otp}"
encoded_auth = base64.b64encode(auth_string.encode()).decode()

print("Encoded Auth:", encoded_auth)

# =========================
# Step 3: Prepare Request
# =========================
url = "https://api.challenge.hennge.com/challenges/backend-recursion/004"

headers = {
    "Authorization": f"Basic {encoded_auth}",
    "Content-Type": "application/json"
}

data = {
    "github_url": github_url,
    "contact_email": email,
    "solution_language": "python"
}

# =========================
# Step 4: Send Request
# =========================
response = requests.post(url, json=Datas, headers=headers)

# =========================
# Step 5: Output
# =========================
print("Status Code:", response.status_code)
print("Response:", response.text)