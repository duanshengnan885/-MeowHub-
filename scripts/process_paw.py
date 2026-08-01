from PIL import Image

img_path = r"C:\Users\ikun\.gemini\antigravity-ide\brain\b9779452-ef7b-4da6-94c4-910b734c3137\paw_generated_1785503680228.png"
img = Image.open(img_path).convert("RGBA")
pixels = img.load()
w, h = img.size

min_x, min_y, max_x, max_y = w, h, 0, 0

for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        dist = ((255-r)**2 + (255-g)**2 + (255-b)**2) ** 0.5
        
        if dist < 30:
            pixels[x, y] = (r, g, b, 0)
        elif dist < 80:
            alpha = int((dist - 30) / 50 * 255)
            pixels[x, y] = (r, g, b, alpha)
        
        if pixels[x, y][3] > 10:
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

if max_x >= min_x and max_y >= min_y:
    img = img.crop((min_x, min_y, max_x, max_y))

img.save(r"d:\个人项目\星喵 (MeowHub)\paw.png")
print("Paw processed with pure Pillow and saved successfully!")
