---
name: paddlex-ocr
version: 1.0.0
description: "本地版 PaddleOCR 技能 - Apache 2.0 开源，纯 CPU，免费无 API 限制"
homepage: "https://github.com/openclaw/skills/tree/main/skills/paddlex-ocr"
metadata:
  openclaw:
    emoji: "📄"
    requires:
      bins: [bash, python3.12]
    provides: ["ocr", "paddleocr"]
license: Apache 2.0
---

# 📄 PaddleOCR Local - 本地版文字识别

> **完全免费的本地 OCR 引擎，纯 CPU，无 API 限制**

PaddleOCR - **Apache 2.0 开源**，本地部署，无需任何 API Key。

---

## 🎯 功能

- ✅ **文本识别** - 支持中文、英文、多语言混合
- ✅ **文本检测** - 智能定位文字区域
- ✅ **纯 CPU** - 无需 GPU，Mac mini/PC 均可运行
- ✅ **无 API 限制** - 完全本地运行
- ✅ **Apache 2.0** - 开源免费

---

## 🚀 快速开始

### 1. 安装（已完成）

```bash
# Python 虚拟环境
source ~/.local/venv/paddleocr/bin/activate

# Python 版本：3.12.13
# PaddlePaddle: 2.6.2
# PaddleOCR: 2.9.1
```

### 2. 环境配置

```bash
# 设置环境变量
export OCR_WHEELS_DIR="${OCR_WHEELS_DIR:-${HOME}/.paddleocr/whl}"

# PaddleOCR v3.0+ ML 大模型下载目录（可选，首次运行自动下载）
export PADDLESOLUTIONS_MODEL_DIR="${PADDLESOLUTIONS_MODEL_DIR:-${HOME}/.paddlex}"
```

---

## 🛠️ 使用方式

### Python API

```python
from paddleocr import PaddleOCR

# 初始化 OCR（自动下载轻量级模型）
ocr = PaddleOCR(
    use_angle_cls=True,   # 开启方向分类
    lang='ch',            # 中文识别
    use_gpu=False,        # CPU 模式
    show_log=True,
    use_seed=True
)

# 识别图片
result = ocr.ocr('image.jpg')
for line in result[0]:
    text, confidence = line[1]
    print(f"{text}: {confidence:.2f}")
```

### CLI 调用

**调用脚本路径**: `scripts/paddleocr_cli.py`

```bash
# 识别中文图片
python scripts/paddleocr_cli.py input.jpg

# 识别英文图片
python scripts/paddleocr_cli.py --lang en input.jpg

# 识别多语言图片
python scripts/paddleocr_cli.py --lang multilingual input.jpg

# 输出目录
python scripts/paddleocr_cli.py -o output/ input.jpg
```

---

## 📐 命令行参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `-l, --lang` | 识别语言 | `ch`, `en`, `multilingual` |
| `-o, --output` | 输出目录 | `output/` |
| `--use_gpu` | GPU 模式 | `True`, `False` |
| `--det_model` | 检测模型 | `PP-DBNet`, `PP-YOLOE` |
| `--rec_model` | 识别模型 | `PP-OCRv5`, `PP-MobNet` |
| `--cls_mode` | 方向分类 | `True` (默认) |

---

## 🌍 支持语言

| 语言代码 | 语言 | 说明 |
|---------|------|------|
| `ch` | 中文简写 | 简体中文 |
| `en` | 英文 | 全拉丁文 |
| `multilingual` | 多语言 | 100+ 种语言 |
| `ch_cht` | 繁体中文 | 繁体 |
| `japan` | 日文 | 日语 + 平假名 |
| `korean` | 韩文 | 韩语 |

---

## 📊 性能

| 场景 | 模型 | 精度 | 大小 | CPU | GPU |
|------|------|------|------|-----|-----|
| **轻量级** | PP-LCNet | 中等 | 15.9MB | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **标准** | PP-MobNet | 高 | 43.5MB | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **高精度** | PP-DetHead | 超高 | 450MB | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**Mac mini 测试**:
- CPU: Apple Silicon M1/M2/M3
- 轻量级模型：单张图片 < 1 秒
- 标准模型：单张图片 1-2 秒

---

## 🔧 配置说明

### 环境变量

```bash
# OCR 模型仓库目录（下载默认位置）
export OCR_WHEELS_DIR="${HOME}/.paddleocr/whl"

# PaddlePaddle 模型目录（v3.0+ ML 大模型）
export PADDLESOLUTIONS_MODEL_DIR="${HOME}/.paddlex"

# 缓存目录
export OCR_CACHE_DIR="${HOME}/.cache/paddleocr"
```

### 推荐配置

Mac mini / 小内存设备：
```bash
export OCR_WHEELS_DIR="/Users/a1/.paddleocr/whl"
export PADDLESOLUTIONS_MODEL_DIR="/Users/a1/.paddlex"
```

---

## 🗺️ 目录结构

```
paddlex-ocr/
├── SKILL.md
├── scripts/
│   ├── paddleocr_cli.py       # CLI 工具
│   ├── paddleocr_api.py       # Python 库
│   └── README.md
├── examples/
│   ├── test_chinese.png
│   └── test_english.png
├── docs/
│   ├── usage.md
│   └── troubleshooting.md
├── LICENSE
└── .gitignore
```

---

## 🚫 注意事项

- ❌ **不支持 PDF 直接解析** - 需先提取图片
- ⚠️ **首次运行会下载模型** - 约 50MB
- ⚠️ **需要稳定的网络连接** - 模型下载
- ⚠️ **纯 CPU 性能有限** - PDF 建议用 GPU

---

## 📚 参考资料

- **GitHub**: https://github.com/PaddlePaddle/PaddleOCR
- **官方文档**: https://paddlepaddle.github.io/PaddleOCR
- **模型下载**: https://github.com/PaddlePaddle/PADLEOCR
- **Apache 2.0**: https://www.apache.org/licenses/LICENSE-2.0

---

## 🔄 版本历史

| 版本 | 发布时间 | 说明 |
|------|---------|------|
| 1.0.0 | 2026-04-04 | 初始版本，本地 PaddleOCR v2.9.1 |
| 1.1.0 | - | 支持 PDF 批量处理 ✏️ |
| 1.2.0 | - | 支持多文档混合 OCR ✏️ |

---

## 👨‍💻 开发者

- **作者**: Max5168 (maxwell)
- **许可**: Apache 2.0
- **联系**: maxwell5168@dscord

---

## 📝 贡献指南

欢迎贡献代码、报告问题或提出建议。请查看 [CONTRIBUTING.md](docs/CONTRIBUTING.md)。

---

**PaddleOCR** 是百度飞桨团队的开源 OCR 引擎，基于 PaddlePaddle 框架，支持多种 OCR 场景，完全免费且无 API 限制。