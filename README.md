# Image to Pixel Art Converter
### Using Linear Algebra Concepts (K-Means Clustering + Matrix Operations)

> A Python-based image processing project that converts any high-resolution image into a retro pixel-art style using K-Means color clustering and matrix transformations.

**Team Members:**
- Kshitij Satish Shetty — PES1UG24AM143
- Mallikarjuna Rao RV — PES1UG24AM155
- Mounik Manohar — PES1UG24AM168

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

You'll be prompted to enter the path of any image. Press **Enter** to use the default `input.jpg`, or provide any image filename:

```
Enter image path (or press Enter for default 'input.jpg'): your_image.jpg
Press any key to exit...
```

> **Any image works** — just make sure the file is in the same directory as `main.py`, or provide the full path.

---

## Project Structure

```
PixelArtProject/
├── main.py               # Main script
├── .gitignore
├── README.md
├── screenshots/
│   ├── Screenshot 2026-04-16 170934.png   # Output window
│   └── Screenshot 2026-04-16 170941.png   # Terminal run
├── Pixel-Art-Converter.pptx               # Project presentation
└── input.jpg                              # Default image
```

---

## Results & Observations

- **Higher K** → more clusters → finer detail
- **Lower K** → fewer clusters → lesser detail
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

---

## Screenshots

**Running the script in terminal:**

![Terminal](screenshots/Screenshot%202026-04-16%20170941.png)

**Output window — Original vs Pixel Art side by side:**

![Pixel Art Output](screenshots/Screenshot%202026-04-16%20170934.png)
