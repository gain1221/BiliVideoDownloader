import os

from getPlay import get_play
from merge import merge_av

# url = "https://www.bilibili.com/video/BV15cT2z9Eny?vd_source=0a54c4b4e9ce6095601a64830dd93f07&spm_id_from=333.788.videopod.episodes&p=3"
if __name__ == '__main__':
    print("Please enter the URL of the target video")
    url = input()
    get_play(url)
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    VIDEO_DIR = os.path.join(CURRENT_DIR, 'video')
    AUDIO_DIR = os.path.join(CURRENT_DIR, 'audio')
    OUTPUT_DIR = os.path.join(CURRENT_DIR, 'output')
    FFMPEG_PATH = os.path.join(CURRENT_DIR, 'ffmpeg')

    if os.name == 'nt' and not FFMPEG_PATH.endswith('.exe'):
        FFMPEG_PATH += '.exe'

    # 执行合并
    try:
        merge_av(VIDEO_DIR, AUDIO_DIR, OUTPUT_DIR, FFMPEG_PATH)
    except Exception as e:
        print(f"Program initialization failed: {str(e)}")
        print("Please check:")
        print(f"1. If FFmpeg exists at: {FFMPEG_PATH}")
        print(f"2. If video directory exists: {VIDEO_DIR}")
        print(f"3. If audio directory exists: {AUDIO_DIR}")
