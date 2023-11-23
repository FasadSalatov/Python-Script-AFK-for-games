# By Fasad with love❤


# Description
This project is a Python script for automatically moving the mouse in games using the PyAutoGUI and Pynput libraries.

# Installation
1. Install Python if you don't have it. [Download Python](https://www.python.org/downloads/)
2. Clone the repository:
   ```bash
   git clone [https://github.com/<your-username>/<your-project>](https://github.com/FasadSalatov/Python-Script-AFK-for-games/tree/main)https://github.com/FasadSalatov/Python-Script-AFK-for-games/.git
   cd <Python-Script-AFK-for-games>

## Create a virtual environment (recommended):
```console
python -m venv venv
```

## Activate the virtual environment:
### On Windows:
```console
venv\Scripts\activate
```
### On macOS and Linux:
```console
source venv/bin/activate
```
## Install dependencies:
```console
pip install -r requirements.txt
```
# Running the Script
## Run the script:
```python
python main.py
```
### The application will start moving the mouse across the screen.
### Press the `Space` key to pause or resume the script.
### Terminate the script by pressing `Ctrl + C` in the terminal.

# Configuration
## If needed, adjust script parameters such as the number of steps for slow movement directly in the `main.py` file.

# Additional Instructions
## Using a Different Key Instead of `Space`
### Open the main.py file.
### Change the line:
```python
if key == keyboard.Key.space:
```
### to the desired key. For example:
```python
if key == keyboard.Key.enter:
```
## Adjusting Mouse Parameters
### In the `main.py` file, you can configure mouse movement speed and other parameters by modifying variables in the move_mouse_slowly function.
