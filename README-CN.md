# Gadgets

[English](./README.md) | [中文文档](./README-CN.md)

## 目录

* [概述](#概述)
* [项目结构](#项目结构)
* [安装](#安装)
* [可用的 Gadgets](#可用的-gadgets)
    * [Mimic Typer](#mimic-typer)
    * [Humanizer](#humanizer)

---

## 概述

**Gadgets** 是一组小型的实验性脚本和工具集合。
每个 gadget 都是独立的，并且可能包含其自己的使用说明和行为。

该仓库目前包含多个 gadgets，未来还将加入更多。

---

## 项目结构

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

所有文件目前都位于项目根目录。
未来的 gadgets 可能会以独立脚本或文件夹的形式出现，具体取决于其复杂度。

---

## 安装

克隆仓库：

```bash
git clone https://github.com/B-X-Y/gadgets.git
cd gadgets
```

安装依赖：

```bash
pip install -r requirements.txt
```

---

## 可用的 Gadgets

### Mimic Typer

**Mimic Typer** 通过逐字符并带有自然延迟的方式输出文本，从而模拟人类输入，使行为更接近真实键盘输入，并降低被识别为自动化输入系统检测到的可能性。

#### 使用方法

1. 确保仓库根目录下存在 `text_to_type.txt`。
2. 将你希望被输入的内容放入该文件。
3. 运行脚本：

```bash
python mimic_typer.py
```

短暂延迟后，它将开始在你当前的光标位置输入文本。

### Humanizer

**Humanizer** 使用 AI 驱动的改写引擎来重写或改述一篇文章，使其变得更加自然，更像人类撰写。

#### 使用方法

1. 在仓库根目录创建 `essay_to_humanize.txt` 文件。
2. 将你想进行 humanize 的文章放入该文件。
3. 运行脚本：

```bash
python humanizer.py
```

处理后的结果将保存为 `humanized_essay.txt`。

---

## LICENSE

该项目基于 MIT License 授权。详情请参阅 [LICENSE](./LICENSE) 文件。
