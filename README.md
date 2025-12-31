# 💎 Nyra AI Face Swap Studio

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Google%20Colab-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)

**Nyra AI Face Swap Studio** is a high-performance, hybrid workflow for automated face swapping and media enhancement. Built upon the powerful [RealMe](https://github.com/RixAI/RealMe) engine, this suite integrates a robust Local PC asset management system with a high-speed Cloud GPU processing interface via Google Colab.

---

## ⚡ Quick Start: Cloud Rendering

Run the studio immediately using free Cloud GPUs. No local installation required.

<a href="https://colab.research.google.com/drive/1qe13g2ysr-7OwImZWWX8LC6rxuL13aiH?authuser=1" target="_blank">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="30"/>
</a>

---

## ✨ Key Features

* **💎 Hybrid Workflow:** Seamlessly switch between Local PC organization and Cloud execution.
* **🎨 Nyra Studio UI (V32):** A custom, "Cyberpunk" styled GUI running on Colab featuring:
    * **Real-time Tracking:** Live Batch count, Frame status, and ETA.
    * **Drive Integration:** Auto-syncs Source, Targets, and Outputs with Google Drive.
    * **Auto-Resume:** Setup once, run forever without re-downloading models.
* **🛠️ Local Toolkit:** * **Safe Renamer:** Bulk renames videos to clean formats (`Source_01.mp4`) with preview.
    * **Upscaler:** Integrated RealESRGAN for 4k upscaling.
    * **Cleaner:** One-click workspace cleanup.
* **🚀 High Quality:** Supports `inswapper_128` for swapping and `GFPGAN v1.4` for face restoration.

---

## 📂 Project Structure

This repository is organized to separate the core engine from custom utility tools.

```text
My Tools/
├── Models/
│   ├── RealMe/                 # Core Face Swap Engine
│   │   ├── models/             # Checkpoints
│   │   │   ├── inswapper_128.onnx
│   │   │   └── GFPGANv1.4.pth
│   │   ├── RealMe/             # Source Code (Processors)
│   │   └── run.py              # Main Execution Logic
│   ├── RealESRGAN_x4plus.pth   # Upscaling Model
│   └── inference_realesrgan.py # Upscaling Script
├── Tools/
│   ├── faceswap.py             # Local wrapper for swapping
│   ├── upscaler.py             # Local wrapper for upscaling
│   └── Config/
├── Nyra_run.py                 # Main Launcher for Local PC
├── rename.py                   # Smart Bulk Video Renamer
├── cleaner.py                  # Cache Cleaner
└── colab_gdrive_upscaler.py    # Cloud-Drive Bridge
