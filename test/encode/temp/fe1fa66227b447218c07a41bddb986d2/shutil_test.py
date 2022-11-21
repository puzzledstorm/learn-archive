import os
import shutil

temp_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(temp_dir)
final_out = f"{os.path.dirname(os.path.abspath(__file__))}/av_encode.mp4"
path_1 = temp_dir
path_2 = f"{temp_dir}/a.mp4"

path = path_1
if os.path.exists(final_out):
    shutil.copy2(final_out, path)
