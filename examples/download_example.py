'''
Author: Yorai Shaoul
Date: 2023-02-03

Example script for downloading using the TartanAir dataset toolbox.
'''

# General imports.
import sys
import argparse

# Local imports.
sys.path.append('..')
import tartanair as ta

parser = argparse.ArgumentParser()
parser.add_argument('--data-root', type=str, required=True)
args = parser.parse_args()

# Create a TartanAir object.
tartanair_data_root = args.data_root

ta.init(tartanair_data_root)

# Can also download via a yaml config file.
ta.download(config = 'download_config.yaml')
