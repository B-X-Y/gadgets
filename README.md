# Gadgets

[English](./README.md) | [中文文档](./README-CN.md)

## Table of Contents

* [Overview](#overview)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Available Gadgets](#available-gadgets)
    * [Mimic Typer](#mimic-typer)
    * [Humanizer](#humanizer)

---

## Overview

**Gadgets** is a collection of small, experimental scripts and utilities.
Each gadget is independent and may include its own usage instructions and behavior.

The repository currently contains multiple gadgets, with more planned for the future.

---

## Project Structure

```
├── .gitignore
├── LICENSE
├── README-CN.md
├── README.md
├── humanizer.py
├── mimic_typer.py
├── prompt.md
├── prompt_v2.md
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

**Mimic Typer** simulates human typing by outputting text character-by-character with natural delays, making the
behavior resemble genuine keyboard input and reducing the likelihood of detection by systems that flag automated typing.

#### Usage

1. Ensure `text_to_type.txt` exists in the repository root.
2. Place the text you want typed into that file.
3. Run the script:

```bash
python mimic_typer.py
```

After a short delay, it begins typing at your current cursor position.

### Humanizer

**Humanizer** rewrites or paraphrases an essay using an AI-powered rephrasing engine, producing a more natural and
human-like version of the original text.

#### Usage

1. Create a file named `essay_to_humanize.txt` in the repository root.
2. Place the essay you want to humanize into that file.
3. Run the script:

```bash
python humanizer.py
```

The humanized result will be saved as `humanized_essay.txt`

---

## LICENSE

This project is licensed under the MIT License. Please see the [LICENSE](./LICENSE) file for details.
