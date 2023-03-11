#%%

# Read in text file
with open('data/spongebob/spongebob_anthology.txt', 'r') as file:
    text = file.read()

# Show first 1000 characters
print(f'\n\n------------------OLD-------------------- \n\n{text[:10000]}')

# Delete all text between square brackets, including brackets
import re
text = re.sub(r'\[.*?\]', '', text)

# Delete all text between parenthesis including parenthesis
text = re.sub(r'\(.*?\)', '', text)

print(f'\n\n------------------NEW--------------------  \n\n{text[:10000]}')


# save new file
with open('data/spongebob/spongebob_anthology_clean.txt', 'w') as file:
    file.write(text)



