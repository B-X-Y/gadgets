# Gadgets

[English](./README.md) | [中文文档](./README-CN.md)

## 目录

* [概述](#概述)
* [项目结构](#项目结构)
* [安装](#安装)
* [可用的 Gadgets](#可用的-gadgets)
    * [Mimic Typer](#mimic-typer)

---

## 概述

**Gadgets** 是一组小型的实验性脚本和工具集合。
每个 gadget 都是独立的，并且可能包含其自己的使用说明和行为。

目前，该仓库包含一个 gadget，未来会加入更多。

---

## 项目结构

```
├── README.md
├── mimic_typer.py
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

## LICENSE

该项目基于 MIT License 授权。详情请参阅 [LICENSE](./LICENSE) 文件。
