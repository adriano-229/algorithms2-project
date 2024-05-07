import re

text = "Your text with alphanumeric words and dates"

pattern = r'\b\w+\b'

matches = re.findall(pattern, text)

print(matches)
