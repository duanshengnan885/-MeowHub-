from PIL import Image
from collections import deque
import sys
import os

img_path = r"C:\Users\ikun\.gemini\antigravity-ide\brain\589b0e4d-152f-4009-88d4-ef1cd4e910ee\media__1785599447595.jpg"
out_dir = r"d:\个人项目\ai_assistant\ai_ui_assistant\assets"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "pet_image.png")

img = Image.open(img_path).convert("RGBA")
width, height = img.size
pixels = img.load()

# 1. Identify non-white pixels
def is_non_white(x, y):
    r, g, b, a = pixels[x, y]
    # If it's too close to white, we consider it white background
    if r > 240 and g > 240 and b > 240:
        return False
    return True

# 2. BFS from center to find all character pixels
visited = set()
queue = deque()
center_x, center_y = width // 2, height // 2

# We start from a vertical line in the middle to ensure we hit the character
for y in range(height):
    if is_non_white(center_x, y):
        queue.append((center_x, y))
        visited.add((center_x, y))

# Also add some horizontal line pixels near center
for x in range(width // 4, width * 3 // 4):
    if is_non_white(x, center_y):
        if (x, center_y) not in visited:
            queue.append((x, center_y))
            visited.add((x, center_y))

print("Starting BFS...")
character_pixels = set()
directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
# Expand search radius slightly for anti-aliasing / small gaps
while queue:
    x, y = queue.popleft()
    character_pixels.add((x, y))
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                if is_non_white(nx, ny):
                    queue.append((nx, ny))

print(f"Found {len(character_pixels)} character pixels")

# 3. Create a new image with just the character
new_img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
new_pixels = new_img.load()

left = width
right = 0
top = height
bottom = 0

for (x, y) in character_pixels:
    new_pixels[x, y] = pixels[x, y]
    if x < left: left = x
    if x > right: right = x
    if y < top: top = y
    if y > bottom: bottom = y

# Add a little padding to the crop
pad = 10
left = max(0, left - pad)
right = min(width, right + pad)
top = max(0, top - pad)
bottom = min(height, bottom + pad)

cropped = new_img.crop((left, top, right, bottom))

# Save
cropped.save(out_path)
print(f"Saved extracted character to {out_path}")
