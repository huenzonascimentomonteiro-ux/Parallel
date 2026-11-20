from pathlib import Path

def collect_inputs(folder):
    # 1. Encontrar arquivos de texto
    txt_files = list(folder.glob("*.txt"))

    if not txt_files:
        raise FileNotFoundError("No .txt file found")

    # 2. Ler os textos
    all_text = []

    for txt in txt_files:
        text = txt.read_text(encoding="utf-8")
        all_text.append(text)

    # 3. Encontrar imagens
    img_files = []

    for ext in ["png", "jpg", "jpeg"]:
        img_files.extend(folder.rglob(f"*.{ext}"))
    
    # 4. Retornar os resultados
    data = {
        "images" : img_files,
        "text" : all_text
    }

    return data