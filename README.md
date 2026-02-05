# 📱 KivyMD Material Calculator

A sleek, functional calculator built with **Python**, **KivyMD 1.2.0**, and deployed via **GitHub Actions**.

## ✨ Features
- **Material Design UI**: Uses `MDRaisedButton` with custom color palettes.
- **Responsive Layout**: Adapts to mobile portrait orientation using `MDGridLayout`.
- **Automated Builds**: Integrated with Buildozer and GitHub Actions for automatic APK generation.

## 🛠️ Requirements
- **Python 3.10+**
- **Kivy 2.3.0**
- **KivyMD 1.2.0**
- **Pillow** (for image processing)

## 🚀 How to Build the APK
This repo is configured for **CI/CD build automation**:
1. Fork or push changes to this repository.
2. Navigate to the **Actions** tab on GitHub.
3. Select the **Build APK** workflow.
4. Once completed, download the APK from the **Artifacts** section at the bottom of the run page.

## 📂 File Structure
- `main.py`: The application logic and UI definition.
- `buildozer.spec`: Configuration for the Android build process.
- `.github/workflows/android.yml`: The automation script for GitHub Actions.

## 🎨 Styling Note
The operators are highlighted in **Gold (#FFD700)** while numeric values use a **Flat Peru (#CD853F)** style with zero elevation for a modern, flat aesthetic.
