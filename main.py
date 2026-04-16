import cv2
import numpy as np

# 🔹 Resize for screen
def resize_for_screen(image, max_width=1200):
    h, w = image.shape[:2]
    if w > max_width:
        scale = max_width / w
        new_size = (int(w * scale), int(h * scale))
        return cv2.resize(image, new_size)
    return image

# 🔹 Input image path
path = input("Enter image path (or press Enter for default 'input.jpg'): ")
if path == "":
    path = "input.jpg"

img = cv2.imread(path)

if img is None:
    print("❌ Image not found!")
    exit()

# 🔹 Pixel Art Processing
small = cv2.resize(img, (64, 64))

data = small.reshape((-1, 3))
data = np.float32(data)

K = 8
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)

_, labels, centers = cv2.kmeans(
    data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS
)

centers = np.uint8(centers)
compressed = centers[labels.flatten()]
result = compressed.reshape(small.shape)

pixel_art = cv2.resize(
    result,
    (img.shape[1], img.shape[0]),
    interpolation=cv2.INTER_NEAREST
)

# 🔹 Resize both for display (same height)
h = 500
scale1 = h / img.shape[0]
scale2 = h / pixel_art.shape[0]

img_resized = cv2.resize(img, (int(img.shape[1]*scale1), h))
pixel_resized = cv2.resize(pixel_art, (int(pixel_art.shape[1]*scale2), h))

# 🔹 Combine side by side
combined = np.hstack((img_resized, pixel_resized))

# 🔹 Add labels (optional but looks 🔥 in PPT/demo)
cv2.putText(combined, "Original", (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.putText(combined, "Pixel Art", (img_resized.shape[1] + 20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# 🔹 Show result
cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
cv2.imshow("Result", combined)

print("\nPress any key to exit...")
cv2.waitKey(0)
cv2.destroyAllWindows()