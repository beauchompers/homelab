import string
import secrets

start = secrets.choice(string.ascii_uppercase)
middle = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(30))
end = secrets.choice(string.ascii_uppercase)

print(start + middle + end)