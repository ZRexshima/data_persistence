import json
from pathlib import Path

path: Path = Path('dict_test.json')
data: str = path.read_text()
user_data: dict[str, str] = json.loads(data)

# print(user_data)
print(f"Hello {user_data['first'].title()}! How is the weather in \
{user_data['location']}?")

