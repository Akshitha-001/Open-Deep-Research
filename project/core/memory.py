import json
from pathlib import Path
from typing import Any, Dict


MEM_FILE = Path(".research_memory.json")




def save(key: str, value: Any):
data = {}
if MEM_FILE.exists():
try:
data = json.loads(MEM_FILE.read_text())
except Exception:
data = {}
data[key] = value
MEM_FILE.write_text(json.dumps(data, indent=2))




def load(key: str):
if not MEM_FILE.exists():
return None
try:
data = json.loads(MEM_FILE.read_text())
except Exception:
return None
return data.get(key)




def clear():
if MEM_FILE.exists():
MEM_FILE.unlink()