from pathlib import Path

path = Path('ch10/learning_python.txt')

content = path.read_text()

for line in content.splitlines():
    print(line.replace('Python', 'C'))