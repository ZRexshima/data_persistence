import json
from pathlib import Path

user_data: dict[str, str] = {'first': 'shima', 'last': 'rider', 'location': 'stack'}
path: Path = Path('dict_test.json')

data: str = json.dumps(user_data)
path.write_text(data)