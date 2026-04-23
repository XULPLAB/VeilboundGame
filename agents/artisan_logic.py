import os, uuid
from PIL import Image, ImageOps
from rembg import remove
def process_assets():
    base_dir = "assets/textures"
    sub_folders = ["prisms", "creatures"]
    found_sheet, sheet_type = None, None
    for sub in sub_folders:
        path = os.path.join(base_dir, sub)
        if not os.path.exists(path): os.makedirs(path, exist_ok=True); continue
        files = [f for f in os.listdir(path) if 'sheet' in f.lower()]
        if files:
            files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)), reverse=True)
            found_sheet, sheet_type = os.path.join(path, files[0]), sub
            break
    if not found_sheet: return
    img = Image.open(found_sheet).convert("RGBA")
    w, h = img.size
    cols, rows, total = (6, 1, 6) if sheet_type == "prisms" else (3, 7, 21)
    tw, th = w // cols, h // rows
    count = 0
    for r in range(rows):
        for c in range(cols):
            count += 1
            if count > total: break
            tile = img.crop((c*tw, r*th, c*tw+tw, r*th+th))
            tile = remove(tile)
            pw, ph = int(tw*0.1), int(th*0.1)
            tile = ImageOps.expand(tile, border=(pw, ph), fill=(0,0,0,0))
            tile.save(os.path.join(base_dir, sheet_type, f"{sheet_type}_unit_{count}_{uuid.uuid4().hex[:4]}.png"))
    os.remove(found_sheet)
if __name__ == "__main__": process_assets()
