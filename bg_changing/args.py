import argparse

parser = argparse.ArgumentParser("bg_changing")
parser.add_argument("-x", "--x_length", type=int)
parser.add_argument("-y", "--y_length", type=int)
parser.add_argument("-d", "--delay", type=int)
parser.add_argument("-s", "--save", action=argparse.BooleanOptionalAction)

arguments = parser.parse_args()
