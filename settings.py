'''
Created on Oct 29, 2015
@author: rhf
'''

import os
import logging, logging.config
import configparser as configparser
import argparse

CONFIG_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.cfg')
LOCAL_CONFIG_FILE = os.path.expanduser('~/.superimpose.cfg')

def get_parse_args():
    '''
    parse command line input arguments
    '''
    parser = argparse.ArgumentParser(description='Calculates: I_{scaled}(Q) = K*I(Q)+b')
    parser.add_argument('-r', '--reference', help='File used as reference to scale all curves', required=True)
    parser.add_argument('-i', '--input', help='Input files (if the reference file is included here it will ignored). Use wildcards, e.g., \'xpto_*\'.', required=True)
    parser.add_argument('-q', '--qmin', help='Q min. If not given, gets it from the config file.', required=False, type=float, default=config.getfloat('General','qmin'))
    parser.add_argument('-m', '--qmax', help='Q max. If not given, gets it from the config file.', required=False, type=float, default=config.getfloat('General','qmax'))
    parser.add_argument('-g', '--discard-begin', help='Discard n points from the beginning of every dataset.', required=False, type=int, default=config.getfloat('General','discard_points_begin'))
    parser.add_argument('-e', '--discard-end', help='Discard n points from the end of every dataset.', required=False, type=int, default=config.getfloat('General','discard_points_end'))
    parser.add_argument('-n', '--no-save', action='store_true', help='Do not save the scaled datasets as _scaled.csv.', required=False, default=(not config.getboolean('General','save_scaled_files')))

    groupk = parser.add_mutually_exclusive_group()
    groupk.add_argument('-k', help='Default K value for I_{scaled}(Q) = K*I(Q)+b.', required=False, type=float)
    groupk.add_argument('--k-list', nargs='+', help='List of K values. Must be the same lenght has data -1', type=float, required=False)

    groupb = parser.add_mutually_exclusive_group()
    groupb.add_argument('-b', help='Default b value for I_{scaled}(Q) = K*I(Q)+b.', required=False, type=float)
    groupb.add_argument('--b-list', nargs='+', help='List of B values. Must be the same lenght has data -1',  type=float, required=False)

    args = vars(parser.parse_args())
    return args

def get_config():
    '''
    Parse .cfg file
    '''
    config = configparser.ConfigParser()
    # config.optionxform=str # case insensitive
    config.read([CONFIG_FILE, LOCAL_CONFIG_FILE])
    return config

def get_logger():
    logging.config.fileConfig(CONFIG_FILE, disable_existing_loggers=False)
    logger = logging.getLogger()
    return logger


config = get_config()
logger = get_logger()
args = get_parse_args()
