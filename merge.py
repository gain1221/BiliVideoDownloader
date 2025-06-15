import os
import subprocess
from pathlib import Path
from tqdm import tqdm


def merge_av(video_dir, audio_dir, output_dir, ffmpeg_path='./ffmpeg'):
    """
    合并同名音视频文件（使用项目目录下的FFmpeg）
    :param video_dir: 视频文件夹路径
    :param audio_dir: 音频文件夹路径
    :param output_dir: 输出文件夹路径
    :param ffmpeg_path: FFmpeg可执行文件路径（默认当前目录下的ffmpeg）
    """
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 验证FFmpeg是否存在
    if not os.path.exists(ffmpeg_path):
        raise FileNotFoundError(f"FFmpeg not found at specified path: {os.path.abspath(ffmpeg_path)}")

    # 获取视频和音频文件列表（不带扩展名）
    video_files = {Path(f).stem: f for f in os.listdir(video_dir)
                   if f.lower().endswith(('.mp4', '.mov', '.avi', '.mkv', '.flv'))}
    audio_files = {Path(f).stem: f for f in os.listdir(audio_dir)
                   if f.lower().endswith(('.mp3', '.wav', '.aac', '.flac', '.m4a'))}

    # 找出共同的文件名
    common_names = set(video_files.keys()) & set(audio_files.keys())

    if not common_names:
        print("Warning: No matching audio and video files found!")
        print(f"Video files: {len(video_files)} | Audio files: {len(audio_files)}")
        return

    print(f"Locate {len(common_names)} pair of audio and video files that can be combined")

    # 处理每个文件
    success_count = 0
    for name in common_names:
        print(f"Start merging: {name}")
        video_path = os.path.join(video_dir, video_files[name])
        audio_path = os.path.join(audio_dir, audio_files[name])
        output_path = os.path.join(output_dir, f"{name}.mp4")  # 输出为MP4格式

        # FFmpeg命令（使用本地路径）
        cmd = [
            ffmpeg_path,
            '-y',  # 覆盖输出文件
            '-i', video_path,  # 视频输入
            '-i', audio_path,  # 音频输入
            '-c:v', 'copy',  # 视频流直接复制
            '-c:a', 'aac',  # 音频转AAC格式
            '-map', '0:v:0',  # 选择视频流
            '-map', '1:a:0',  # 选择音频流
            '-shortest',  # 以较短的流为准
            '-movflags', '+faststart',  # 流式播放优化
            output_path
        ]

        try:
            # 运行FFmpeg并捕获输出
            result = subprocess.run(
                cmd,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8'
            )
            success_count += 1
            print(f"Finish merging: {name}")
        except subprocess.CalledProcessError as e:
            print(f"\nError file: {name}")
            print(f"Error message: {e.stderr[:200]}...")  # 只显示前200字符
        except Exception as e:
            print(f"\nAn error occurred while processing {name}: {str(e)}")

    # 打印总结报告
    print("\nMerge completed!")
    print(f"Success: {success_count}/{len(common_names)}")
    print(f"Output directory: {os.path.abspath(output_dir)}")