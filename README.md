# 💎 Nyra AI Face Swap Studio

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Google%20Colab-orange) ![Status](https://img.shields.io/badge/Status-Active-green)

**Nyra AI Face Swap Studio** is a high-performance, hybrid workflow for automated face swapping and media enhancement. Built upon the powerful [RealMe](https://github.com/RixAI/RealMe) engine, this suite integrates local asset management with high-speed Cloud GPU processing via Google Colab.

## ✨ Key Features

* **Hybrid Workflow:** Seamlessly switch between Local PC organization and Google Colab execution.
* **Nyra Studio V32 (Colab):** A custom, "Cyberpunk" styled GUI with:
    * Real-time batch tracking (Batch/Status/ETA).
    * Google Drive integration (Permanent storage).
    * Auto-resume capability (Setup once, run forever).
* **Local Toolkit:** Includes utilities for bulk renaming, upscaling (RealESRGAN), and file management.
* **High Quality:** Supports `inswapper_128` for swapping and `GFPGAN` for face enhancement.

---

## 📂 Project Structure

The project is organized to keep models, tools, and the core engine separate.

```text
My Tools/
├── Models/
│   ├── RealMe/                 # Core Engine
│   │   ├── models/             # Checkpoints (inswapper_128.onnx, GFPGANv1.4.pth)
│   │   ├── RealMe/             # Source code
│   │   └── run.py              # Main execution script
│   ├── RealESRGAN_x4plus.pth   # Upscaling models
│   └── inference_realesrgan.py
├── Tools/
│   ├── faceswap.py             # Local swapping wrapper
│   ├── upscaler.py             # Enhancement tool
│   └── Config/
├── Nyra_run.py                 # Main Local Launcher
├── rename.py                   # Bulk Video Renamer (Safe Mode)
├── cleaner.py                  # Workspace cleaner
└── colab_gdrive_upscaler.py    # Cloud bridge
