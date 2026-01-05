'''
Author: Yorai Shaoul
Date: 2023-02-03

Example script for downloading using the TartanAir dataset toolbox.
'''

# General imports.
import sys

# Local imports.
sys.path.append('..')
import tartanair as ta

# Create a TartanAir object.
tartanair_data_root = '/media/nigel/copel/tartanair-v2'

ta.init(tartanair_data_root)

# List available trajectories.
ta.visualize('AbandonedFactory2', 
              difficulty='easy', 
              trajectory_id = 'P000', 
              modality = ['image', 'depth'], 
              camera_name = ['lcam_front'],
              show_seg_palette = False)