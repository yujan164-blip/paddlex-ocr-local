#!/usr/bin/env python3
"""
PaddleOCR CLI Tool
===================
本地版 PaddleOCR 命令行工具，支持中文、英文、多语言识别。

Usage:
    python3 scripts/paddleocr_cli.py input.jpg
    python3 scripts/paddleocr_cli.py --lang en input.jpg
    python3 scripts/paddleocr_cli.py -o output/ input.jpg

Requirements:
    - Python 3.12+
    - paddleocr >= 2.9.1
    - paddlepaddle >= 2.6.2
    
Author: Max5168
License: Apache 2.0
"""

import argparse
import os
import sys
from pathlib import Path

# 设置环境变量
OCR_WHEELS_DIR = os.environ.get('OCR_WHEELS_DIR', Path.home() / '.paddleocr' / 'whl')
PADDLESOLUTIONS_MODEL_DIR = os.environ.get('PADDLESOLUTIONS_MODEL_DIR', Path.home() / '.paddlex')

def init_paddleocr(lang='ch', use_gpu=False):
    """
    初始化 PaddleOCR 实例
    """
    try:
        from paddleocr import PaddleOCR
        
        ocr = PaddleOCR(
            use_angle_cls=True,
            lang=lang,
            use_gpu=use_gpu,
            show_log=True,
            use_seed=True
        )
        return ocr
    except ImportError:
        print("❌ PaddleOCR 未安装！请先运行：pip install paddleocr paddlepaddle")
        print(f"  虚拟环境：{sys.prefix}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ PaddleOCR 初始化失败：{e}")
        sys.exit(1)

def run_ocr(image_path, ocr, output_dir=None):
    """
    运行 OCR 任务
    """
    image_path = Path(image_path)
    if not image_path.exists():
        print(f"❌ 文件不存在：{image_path}")
        return None
    
    # 确保输出目录存在
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        print(f"正在识别：{image_path.name}")
        result = ocr.ocr(str(image_path))
        
        if not result or not result[0]:
            print("⚠️ 未识别到文字")
            return None
        
        # 提取文字
        lines = []
        for line in result[0]:
            text, confidence = line[1][0], line[1][1]
            lines.append(f"{text}: {confidence:.2f}")
            print(f"📝 {text} (置信度：{confidence:.4f})")
        
        # 保存结果到文件（如果指定输出目录）
        if output_dir:
            base_name = image_path.stem
            output_file = output_dir / f"{base_name}_ocr.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                for line in lines:
                    f.write(line + '\n')
            print(f"\n✅ 结果已保存：{output_file}")
        
        return lines
        
    except Exception as e:
        print(f"❌ OCR 识别失败：{e}")
        return None

def main():
    """
    主程序入口
    """
    parser = argparse.ArgumentParser(
        description='PaddleOCR - 本地版文字识别工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
    python paddleocr_cli.py input.jpg
    python paddleocr_cli.py --lang en input.jpg
    python paddleocr_cli.py --lang multilingual input.jpg
    python paddleocr_cli.py -o output/ input.jpg
'''
    )
    
    parser.add_argument('image', help='图片路径 (支持 jpg, png, bmp, gif 等)')
    parser.add_argument('-l', '--lang', default='ch', 
                       choices=['ch', 'en', 'multilingual', 'ch_cht', 'japan', 'korean'],
                       help='识别语言 (默认：ch)')
    parser.add_argument('-o', '--output', default=None,
                       help='输出目录 (默认：不保存)')
    parser.add_argument('--use_gpu', action='store_true', default=False,
                       help='启用 GPU 模式')
    parser.add_argument('--det_model', default='PP-OCRv4',
                       help='检测模型 (默认：PP-OCRv4)')
    parser.add_argument('--rec_model', default='PP-OCRv4',
                       help='识别模型 (默认：PP-OCRv4)')
    parser.add_argument('--cls_mode', action='store_true', default=True,
                       help='启用方向分类 (默认：启用)')
    
    args = parser.parse_args()
    
    # 初始化 OCR
    print("正在初始化 PaddleOCR...")
    ocr = init_paddleocr(lang=args.lang, use_gpu=args.use_gpu)
    
    # 运行 OCR
    lines = run_ocr(args.image, ocr, args.output)
    
    if lines:
        print(f"\n✅ 识别完成，共 {len(lines)} 行")
        sys.exit(0)
    else:
        print("\n⚠️ 未识别到文字")
        sys.exit(1)

if __name__ == '__main__':
    main()