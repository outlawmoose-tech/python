# Python Strings Examples

# Create a string
text = ' Hello, World! '
print('Original:', text)

# Get the length of the string
length = len(text)
print('Length:', length)

# Convert to lowercase
lowercase = text.lower()
print('Lowercase:', lowercase)

# Convert to uppercase
uppercase = text.upper()
print('Uppercase:', uppercase)

# Remove leading and trailing whitespace
stripped = text.strip()
print('Stripped:', stripped)

# Replace a substring
replaced = text.replace('World', 'Python')
print('Replaced:', replaced)

# Split the string
splitted = text.split(',')
print('Splitted:', splitted)

# Join a list of strings
joined = ' '.join(['Hello', 'Python'])
print('Joined:', joined)

# Find a substring
index = text.find('World')
print('Index of "World":', index)

# Format strings
formatted = 'Hello, {}!'.format('Python')
print('Formatted:', formatted)
