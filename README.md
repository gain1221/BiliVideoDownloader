# B站视频下载与合并工具

这是一个用于下载B站视频并自动合并音视频的Python工具。该工具可以自动下载视频的音频和视频流，并使用FFmpeg将它们合并成完整的视频文件。

## 功能特点

- 支持从B站视频链接下载视频
- 自动分离并下载视频和音频流
- 使用FFmpeg自动合并音视频
- 支持多种视频格式（mp4, mov, avi, mkv, flv）
- 支持多种音频格式（mp3, wav, aac, flac, m4a）
- 自动创建必要的目录结构
- 提供详细的处理进度和错误报告

## 环境要求

- Python 3.6+
- FFmpeg
- 以下Python包：
  - requests
  - tqdm
- 需要自行下载FFmpeg (官网地址：https://ffmpeg.org/)
## 安装步骤

1. 克隆或下载本项目到本地
2. 安装所需的Python包：
   ```bash
   pip install requests tqdm
   ```
3. 下载FFmpeg并放置在项目根目录下
   - Windows用户：下载ffmpeg.exe
   - Linux/Mac用户：下载ffmpeg可执行文件

## 使用方法

1. 运行主程序：
   ```bash
   python main.py
   ```
2. 在提示时输入B站视频URL
3. 程序会自动：
   - 下载视频和音频文件
   - 将它们保存到相应的目录
   - 使用FFmpeg合并文件
   - 输出最终视频到output目录

## 目录结构

```
project/
├── main.py          # 主程序入口
├── getPlay.py       # 视频下载模块
├── merge.py         # 音视频合并模块
├── ffmpeg           # FFmpeg可执行文件
├── video/           # 视频文件存储目录
├── audio/           # 音频文件存储目录
└── output/          # 合并后的输出目录
```

## 注意事项

1. 使用前请确保已正确安装FFmpeg
2. 需要有效的B站Cookie才能下载视频
3. 确保有足够的磁盘空间存储视频文件
4. 下载的视频仅供个人学习使用，请遵守相关法律法规

## 常见问题

1. 如果遇到"FFmpeg not found"错误，请检查ffmpeg文件是否在正确的位置
2. 如果下载失败，请检查网络连接和Cookie是否有效
3. 如果合并失败，请确保视频和音频文件都已正确下载

## 许可证

本项目仅供学习和研究使用，请勿用于商业用途。

## 贡献

欢迎提交Issue和Pull Request来帮助改进这个项目。 
