# Gadgets

## Table of Contents

* [Overview](#overview)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Available Gadgets](#available-gadgets)
  * [Mimic Typer](#mimic-typer)

---

## Overview

**Gadgets** is a collection of small, experimental scripts and utilities.
Each gadget is independent and may include its own usage instructions and behavior.

At the moment, the repository contains a single gadget with more planned for the future.

---

## Project Structure

```
├── README.md
├── mimic_typer.py
└── requirements.txt
```

All files currently reside in the project root.
Future gadgets may appear as standalone scripts or folders depending on their complexity.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/B-X-Y/gadgets.git
cd gadgets
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Available Gadgets

### Mimic Typer

**Mimic Typer** simulates human typing by outputting text character-by-character with natural delays, making the behavior resemble genuine keyboard input and reducing the likelihood of detection by systems that flag automated typing.

#### Usage

1. Ensure `text_to_type.txt` exists in the repository root.
2. Place the text you want typed into that file.
3. Run the script:

```bash
python mimic_typer.py
```

After a short delay, it begins typing at your current cursor position.
