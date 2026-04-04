# 📄 PaddleOCR OpenClaw Skill - README
PaddleOCR Local - 本地版文字识别

## 简介

这是一个 **Apache 2.0 开源** 的 PaddleOCR 本地部署技能，支持：

- ✅ 中文、英文、多语言识别
- ✅ 纯 CPU 运行（无需 GPU）
- ✅ 无 API 限制
- ✅ 完全免费

## 安装（已完成）

```bash
# Python 虚拟环境
source ~/.local/venv/paddleocr/bin/activate

# 已安装的组件
- PaddlePaddle 2.6.2
- PaddleOCR 2.9.1
- Python 3.12
```

## 使用方式

### CLI 命令

```bash
# 识别中文图片
python3 scripts/paddleocr_cli.py input.jpg

# 识别英文图片
python3 scripts/paddleocr_cli.py --lang en input.jpg

# 识别多语言图片
python3 scripts/paddleocr_cli.py --lang multilingual input.jpg

# 输出到文件
python3 scripts/paddleocr_cli.py -o output/ input.jpg
```

### 在 OpenClaw 中使用

当你说：
- "帮我识别图片文字"
- "提取这段文字"
- "OCR this image"

OpenClaw 会自动调用 `paddleocr_cli.py` 来识别图片中的文字。

## 支持的语言

| 语言代码 | 语言 | 说明 |
|---------|------|------|
| `ch` | 简体中文 | 默认 |
| `en` | 英文 | 全拉丁文 |
| `ch_cht` | 繁体中文 | 繁体 |
| `japan` | 日文 | 日语 + 平假名 |
| `korean` | 韩文 | 韩语 |
| `multilingual` | 多语言 | 100+ 种语言 |

## 目录结构

```
paddlex-ocr/
├── SKILL.md                  # OpenClaw Skill 定义
├── scripts/
│   └── paddleocr_cli.py      # CLI 工具
├── examples/
│   └── test_chinese.png      # 示例图片
└── README.md                 # 本文件
```

## 许可证

Apache 2.0 - 完全免费开源

## 贡献

欢迎提交 Issue 或 Pull Request。

## 参考资料

- GitHub: https://github.com/PaddlePaddle/PaddleOCR
- 官方文档：https://paddlepaddle.github.io/PaddleOCR
- PaddleOCR Blog: https://www.paddlepaddle.org.cn

---

**作者**：Max5168 (maxwell5168)