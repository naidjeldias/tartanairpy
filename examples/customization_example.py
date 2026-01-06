'''
Author: Yorai Shaoul
Date: 2023-02-05

Example script for synthesizing data in new camera-models from the TartanAir dataset.
'''

# General imports.
import sys
import argparse
from scipy.spatial.transform import Rotation

# Local imports.
sys.path.append('..')
import tartanair as ta

ENV_TRAJ_LIST = [
    ('AbandonedFactory2', ['P000', 'P001', 'P002', 'P003','P004', 'P005']),
    ('ArchVizTinyHouseDay', ['P000', 'P001', 'P002', 'P003','P004', 'P005','P006']),
    ('CountryHouse', ['P000', 'P001', 'P002', 'P003','P004', 'P005']),
    ('OldBrickHouseDay', ['P001', 'P002', 'P003','P004', 'P005', 'P006','P007']),
    ('RetroOffice', ['P000', 'P001', 'P002', 'P003','P004', 'P005']),
    ('AmericanDiner', ['P000', 'P002', 'P003','P004', 'P005']),
]
parser = argparse.ArgumentParser()
parser.add_argument('--data-root', type=str, required=True)
args = parser.parse_args()

# Create a TartanAir object.
tartanair_data_root = args.data_root
ta.init(tartanair_data_root)

# Create the requested camera models and their parameters.
R_raw_new0 = Rotation.from_euler('y', 0, degrees=True).as_matrix().tolist()
R_raw_new1 = Rotation.from_euler('y', 90, degrees=True).as_matrix().tolist()
R_raw_new2 = Rotation.from_euler('y', 180, degrees=True).as_matrix().tolist()

cam_model_0 = {'name': 'pinhole', 
               'raw_side': 'left', # TartanAir has two cameras, one on the left and one on the right. This parameter specifies which camera to use.
               'params': 
                        {'fx': 535.4, 'fy': 539.2, 'cx': 320.1, 'cy': 247.6, 'width': 640, 'height': 480},
                        'R_raw_new': R_raw_new0}

cam_model_1 = {'name': 'pinhole', 
               'raw_side': 'left', # TartanAir has two cameras, one on the left and one on the right. This parameter specifies which camera to use.
               'params': 
                        {'fx': 535.4, 'fy': 539.2, 'cx': 320.1, 'cy': 247.6, 'width': 640, 'height': 480},
                        'R_raw_new': R_raw_new1}

cam_model_2 = {'name': 'pinhole', 
               'raw_side': 'left', # TartanAir has two cameras, one on the left and one on the right. This parameter specifies which camera to use.
               'params': 
                        {'fx': 535.4, 'fy': 539.2, 'cx': 320.1, 'cy': 247.6, 'width': 640, 'height': 480},
                        'R_raw_new': R_raw_new2}


for env, traj_list in ENV_TRAJ_LIST:
    for traj in traj_list:
        ta.customize(env = env, 
                     difficulty = 'easy', 
                     trajectory_id = [traj], 
                     modality = ['image', 'depth'], 
                     new_camera_models_params=[cam_model_0, cam_model_1, cam_model_2], 
                     num_workers = 4,
                     device = "cuda") # or cpu
