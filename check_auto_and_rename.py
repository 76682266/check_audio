import argparse
import os
import subprocess
#这个地方我经常出现PATH配置了无效的情况,win11,所以写死了下环境变量了,可以自行修改
ffmpeg_path="D:\\ffmpeg-6.0-full_build\\bin\\ffmpeg.exe"
#author ChatGPT + seven
def check_audio(file_path):
    """
    检查给定文件是否包含音轨
    """
    command = [ffmpeg_path, "-i", file_path, "-map", "0:a", "-c", "copy", "-f", "null", "-"]
    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        pass
    return False

def rename_files_with_audio(folder_path):
    """
    将包含音轨的文件重命名为 [WithAudio] + 原始文件名
    modify:如果判断有音频并且带前缀了,那么不要重命名了,省的你重新弄出来一堆开头名字的
    然后你就可以搜索关键字找自己想要的音视频文件啦
    """
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_name.startswith("[WithAudio]") or not check_audio(file_path):
                continue
            else:
                new_file_name = "[WithAudio]" + file_name
                os.rename(file_path, os.path.join(root, new_file_name))
                print(f"Renamed file {file_path} to {new_file_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename files with audio in the given folder")
    parser.add_argument("folder_path", help="Path to the folder to check for files with audio")
    args = parser.parse_args()

    rename_files_with_audio(args.folder_path)
