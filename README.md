## Usage
```bash
# Hash a password
python main.py hash 'yourpassword'

# Generate a random password (12 characters)
python main.py generate

# Generate a 16-character password
python main.py generate --length 16

# Generate 5 passwords
python main.py generate --number 5

# Generate without special characters
python main.py generate --no-special