# 📬 F1 25 Automated Mail Claimer

A **computer vision automation tool** that autonomously claims in-game mail rewards in *F1 25*, eliminating a ~2-hour manual workflow through real-time UI state detection and context-aware input simulation.

---

## 🧠 How It Works

The tool uses **OpenCV** to continuously monitor the screen, detect UI state transitions via frame differencing, and simulate the exact keypresses needed to navigate menus - entirely hands-free.

```
Screen Capture (loop)
        ↓
Frame Differencing (absdiff)
        ↓
UI State Classification
        ↓
Context-Aware Keypress Simulation (PyDirectInput)
        ↓
Next State → Repeat until all mail claimed
```

### Key Design Decisions

- **Frame differencing (`absdiff`)** - detects meaningful UI transitions (animations, screen changes) rather than relying on brittle template matching that fails with resolution or brightness changes
- **State-gated inputs** - keypresses are only sent on validated game states, preventing false triggers and timing errors
- **Context-aware navigation** - different menu states trigger different input sequences, handling the full end-to-end reward claim flow

---

## 🚀 Features

- Fully autonomous mail reward claiming in F1 25
- Robust UI state detection via `cv2.absdiff` frame differencing
- Context-aware input sequencing - no hardcoded timing delays
- Eliminates ~2 hours of manual repetitive input per session
- Packaged as a standalone `.exe` via **PyInstaller** — no Python install required

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| OpenCV (`cv2`) | Screen capture, frame differencing, state detection |
| PyDirectInput | Low-level keypress simulation (DirectInput, game-compatible) |
| PyInstaller | Package as standalone executable |
| Git | Version control |

---

## 📁 Project Structure

```
f1-mail-claimer/
├── src/
│   ├── app.py            # Entry point & main automation loop
│   ├── helpers.py        # Helper functions required for automated loop
├── screenshots/
│   └── states/           # Reference frames for state classification
        └──communicating-online-services.png
        └──mail-loading-screen1.png
        └──mail-loading-screen2.png
        └──mail-rewards-screen.png
        └──mail-screen1.png
        └──mail-screen2.png
        └──online-services-error.png
├── mail_claimer.exe
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Usage

### Option A - Run from source

```bash
# Clone the repo
git clone https://github.com/priyansh3010/f1-mail-claim-automation.git
cd f1-mail-claim-automation

# Install dependencies
pip install -r requirements.txt

# Run
python src/app.py
```

### Option B - Run the executable (Windows)

Download `mail_claimer.exe` from [Releases](https://github.com/yourusername/f1-mail-claimer/releases), launch F1 25, navigate to the mail screen, and run the executable (screenshots folder must be in the same directory as the .exe file).

---

## 📦 Dependencies

```
opencv-python
pydirectinput
pyinstaller
```

---

## ⚠️ Notes

- Designed and tested on **Windows** (required for DirectInput compatibility)
- Resolution-independent by design — frame differencing adapts to screen changes rather than relying on fixed pixel coordinates
- Intended for personal use automating repetitive in-game workflows

---

## 🔗 References

- [OpenCV Documentation](https://docs.opencv.org/)
- [PyDirectInput](https://github.com/learncodebygaming/pydirectinput)
- [PyInstaller](https://pyinstaller.org/)