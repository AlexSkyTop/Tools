import jwt
import datetime

payload = {
  "role": "Admin",
  "iss": "bookshelf",
  "exp": 1741267428,
  "iat": 1740662628,
  "userId": 1,
  "email": "admin"
}

secret = "1234"

token = jwt.encode(payload, secret, algorithm="HS256")
print(token)