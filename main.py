import sys
import os
sys.path.append(os.path.abspath('./'))
from attack.attack_v2 import attack_video
from collections import deque
import numpy as np
from tqdm import tqdm
from attack.attack_v2 import cal_success_rate
from csv_read import read_csv
import directory_utils

if __name__ == "__main__":
    
    # Create output directory
    directory_utils.create_output_directories()

    #  video file name, attack start frame,  patch coords:[left, top, right, bottom]
    videos_info = read_csv('data-set.csv')

    dir_path = './data/'
    results = []
    for idx, video_info in enumerate(tqdm(videos_info)):
        print(video_info[0])
        (video_path, temp_attack_frame, patch_bbox, moving_direction) = video_info
        video_path = os.path.join(dir_path, video_path)
        temp_attack_frame_id_list = []
        for _ in range(100):
            temp_attack_frame_id_list.append(0)
        attack_det_id_dict = {temp_attack_frame : temp_attack_frame_id_list}

        params = {
            'max_age' :  60,  #4
            'min_hits' : 6,  #1
            'tracker_list' : [],
        }
        id_list = []
        for idx in range(100):
            id_list.append(str(idx))
        params['track_id_list'] = deque(id_list)

        ret = attack_video(params, video_path=video_path, attack_det_id_dict=attack_det_id_dict, patch_bbox=patch_bbox, moving_direction=moving_direction, is_return=True)
        results.append(ret)
