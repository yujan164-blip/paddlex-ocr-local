# 📄 PaddleOCR OpenClaw Skill

## 🚀 快速开始

### 安装技能

```bash
# 克隆技能
git clone https://github.com/yujan164-blip/paddlex-ocr.git \
    ~/.openclaw-history/skills/paddlex-ocr
```

### 前提条件

```bash
# 1. 创建 Python 虚拟环境
python3 -m venv ~/paddleocr-venv
source ~/paddleocr-venv/bin/activate

# 2. 安装 PaddlePaddle 和 PaddleOCR
pip install paddlepaddle==2.6.2
pip install paddleocr==2.9.1

# 3. 验证安装
python3 -c "from paddleocr import PaddleOCR; print('✅ Ready!')"
```

### 使用技能

```bash
cd ~/.openclaw-history/skills/paddlex-ocr

# 识别中文图片
python3 scripts/paddleocr_cli.py input.jpg

# 识别英文图片
python3 scripts/paddleocr_cli.py --lang en input.jpg

# 识别多语言图片
python3 scripts/paddleocr_cli.py --lang multilingual input.jpg

# 输出到文件
python3 scripts/paddleocr_cli.py -o output/ input.jpg
```

---

## 📋 详细参数

| 参数 | 说明 | 默认值 |
|------|------|------|
| `image` | 图片路径 | - |
| `-l, --lang` | 识别语言 | `ch` |
| `-o, --output` | 输出目录 | 不保存 |
| `--use_gpu` | 启用 GPU 模式 | `False` |

### 支持的语言

| 语言代码 | 语言 | 说明 |
|---------|--|------|
| `ch` | 简体中文 | 默认 |
| `en` | 英文 | 全拉丁文 |
| `ch_cht` | 繁体中文 | 繁体 |
| `japan` | 日文 | 日语 |
| `korean` | 韩文 | 韩语 |
| `multilingual` | 多语言 | 100+ 种语言 |

---

## 🛠️ 目录结构

```
paddlex-ocr/
├── SKILL.md                  # OpenClaw Skill 定义
├── scripts/
│   └── paddleocr_cli.py      # CLI 命令行工具
├── examples/
│   └── test_chinese.png      # 示例图片
└── README.md                 # 使用说明
```

---

## 💡 使用示例

### Python 脚本调用

```python
from paddleocr import PaddleOCR

# 初始化 OCR
ocr = PaddleOCR(
    use_angle_cls=True,
    lang='ch',
    show_log=True
)

# 识别图片
result = ocr.ocr('image.jpg')
for line in result[0]:
    text, confidence = line[1]
    print(f"{text}: {confidence}")
```

---

## 🔧 打包部署

如需将技能打包成分发版本：

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包
cd scripts
pyinstaller --onefile paddleocr_cli.py

# 结果：dist/paddleocr_cli
```

打包后的可执行文件可以直接发送给其他用户，无需安装任何 Python 依赖！

---

## 📚 参考资料

- **PaddleOCR 官方**：https://github.com/PaddlePaddle/PaddleOCR
- **官方文档**：https://paddlepaddle.github.io/PaddleOCR
- **Apache 2.0 许可**：https://www.apache.org/licenses/LICENSE-2.0

---

**作者**: Max5168  
**许可**: Apache 2.0 开源
