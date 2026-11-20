from pathlib import Path
from src import input_manager as inpm
from src import ai_processor as aip

FOLDER = Path("input")

data = inpm.collect_inputs(FOLDER)

result = aip.generate_content(data["text"])

print(result)