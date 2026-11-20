from src.ai_processor import client

for model in client.models.list():
    if "generateContent" in model.supported_actions:
        print(model.name)