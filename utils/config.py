# Configuration settings for PyPassGuard

# API settings (for future use with Have I Been Pwned)
API_SETTINGS = {
    'hibp_api_url': 'https://api.pwnedpasswords.com/range/',
    'user_agent': 'PyPassGuard-Password-Checker'
}

# Password requirements
PASSWORD_REQUIREMENTS = {
    'min_length': 8,
    'require_uppercase': True,
    'require_lowercase': True,
    'require_digits': True,
    'require_special_chars': True,
    'special_chars': '!@#$%^&*()_+-=[]{};:\'",.<>/?'
}

# Common substitutions for password strengthening
COMMON_SUBSTITUTIONS = {
    'a': ['@', '4', 'á', 'à'],
    'b': ['8', '6', 'ß'],
    'e': ['3', '€', 'ë'],
    'i': ['1', '!', 'í', 'ì'],
    'o': ['0', 'ö', 'ó', 'ò'],
    's': ['5', '$', 'š'],
    't': ['7', '+'],
    'g': ['9', '&'],
    'l': ['1', '|'],
    'z': ['2', '%']
}