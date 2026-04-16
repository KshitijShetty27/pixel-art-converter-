# Image to Pixel Art Converter
### Using Linear Algebra Concepts (K-Means Clustering + Matrix Operations)

> A Python-based image processing project that converts any high-resolution image into a retro pixel-art style using K-Means color clustering and matrix transformations.

**Team Members:**
- Kshitij Satish Shetty — PES1UG24AM143
- Mallikarjuna Rao RV — PES1UG24AM155
- Mounik Manohar — PES1UG24AM168

---

## Screenshots

**Running the script in terminal:**

![Terminal](screenshots/Screenshot%202026-04-16%20170941.png)

**Output window — Original vs Pixel Art side by side:**

![Pixel Art Output](screenshots/Screenshot%202026-04-16%20170934.png)

---

## Objective

- Convert a high-resolution image into a pixel-art style image
- Reduce image complexity by lowering resolution and the number of colors
- Represent image data using matrices and vectors
- Demonstrate a practical application of Linear Algebra in image processing

---

## Linear Algebra Concepts Used

| Concept | How It's Applied |
|---|---|
| Matrix & Vector Representation | Image stored as an (m × n × 3) matrix; each pixel is an RGB vector |
| Euclidean Distance | Used by K-Means to measure similarity between color vectors |
| Vector Clustering (K-Means) | Groups similar colors into K clusters |
| Matrix Transformation & Reconstruction | Pixel values replaced by cluster centroids and upscaled back |

---

## Methodology

1. **Read image** → represented as an `(m × n × 3)` matrix
2. **Downsample** → resize to `64×64` to reduce detail
3. **Reshape** → flatten pixels into a list of RGB vectors
4. **K-Means clustering** → cluster colors into K groups (default K=8)
5. **Replace pixels** → assign each pixel its cluster centroid color
6. **Upscale** → resize back to original dimensions using nearest-neighbor interpolation (preserves blocky pixel look)
7. **Display** → show original and pixel-art result side by side

---

## How to Run

### Prerequisites

```bash
pip install opencv-python numpy
```

### Run

```bash
python main.py
```

You'll be prompted to enter an image path. Press **Enter** to use the default `input.jpg`, or type a filename like `flower.jpg`.

```
Enter image path (or press Enter for default 'input.jpg'): flower.jpg
Press any key to exit...
```

---

## Project Structure

```
PixelArtProject/
├── main.py               # Main script
├── flower.jpg            # Sample input image
├── man.jpg               # Sample input image
├── scenery.jpg           # Sample input image
├── screenshots/
│   ├── Screenshot 2026-04-16 170934.png   # Output window
│   └── Screenshot 2026-04-16 170941.png   # Terminal run
├── LAA Exp.pptx          # Project presentation
└── LAA Exp.pdf           # Project presentation (PDF)
```

---

## Results & Observations

- **Higher K** → more colors retained → finer detail
- **Lower K** → fewer colors → stronger pixel-art effect
- Downsampling to 64×64 combined with color quantization produces the characteristic blocky, stylized look

---

## Applications

- Retro game design and graphics
- Image compression
- Digital art and stylization tools

---

## Tech Stack

- **Python 3**
- **OpenCV** (`cv2`) — image I/O, resizing, display
- **NumPy** — matrix operations and reshaping
