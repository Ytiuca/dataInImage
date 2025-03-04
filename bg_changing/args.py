import argparse
from logger import Logger

LOGGER = Logger()

parser = argparse.ArgumentParser("bg_changing")
parser.add_argument("-x", "--x_length", type=int)
parser.add_argument("-y", "--y_length", type=int)
parser.add_argument("-d", "--delay", type=int)

arguments = parser.parse_args()
