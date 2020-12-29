


# EOF


import os
import sys


TARGET_FILE_NAME = 'tricky_soccer_ms.py'


# save current file to target file
print('SAVING {} AS {}...'.format(__file__, TARGET_FILE_NAME))
os.rename(__file__, TARGET_FILE_NAME)

# remove file content after "# EOF"
with open(TARGET_FILE_NAME, 'r') as f:
    file_content = f.read()
file_content = file_content.split('# EOF')[0]
with open(TARGET_FILE_NAME, 'w') as f:
    f.write(file_content)

# list projects/ directory and print file content before exiting
print(os.listdir())
print('{} SAVED!'.format(TARGET_FILE_NAME))
sys.exit()
