# To install dependencies with Conda:
# $ conda create --name video
# $ conda activate video
# $ conda install -c conda-forge pillow ffmpeg opencv
# It is important to use `-c conda-forge` because without it, the `cv2.VideoWriter` will
# fail to initialize.

import argparse
import cv2
import numpy as np
import os
from PIL import Image
import sys


def print_args(args):
    print("Input directory 1 (top): {}".format(args.input_dir1))
    print("Input directory 2 (bottom): {}".format(args.input_dir2))
    print("Top height fraction {}".format(args.top_height_fraction))
    print("Output width: {}".format(args.output_width))
    print("Output height: {}".format(args.output_height))
    print("Output fps: {}".format(args.fps))
    print("Output directory: {}".format(args.output_dir))
    print("Output frames only: {}".format(args.frames_only))


def check_args(args):
    if args.top_height_fraction <= 0 or 1 <= args.top_height_fraction:
        print("Usage: top height fraction ('-t' or '--top') must be between 0 and 1")
        sys.exit(1)
    if args.output_width <= 0:
        print("Usage: output width ('-ow' or '--width') must be greater than 0")
        sys.exit(1)
    if args.output_height <= 0:
        print("Usage: output height ('-oh' or '--height') must be greater than 0")
        sys.exit(1)
    if args.fps <= 0:
        print("Usage: frames per s second ('-fps' or '--fps') must be greater than 0")
        sys.exit(1)


def order(relative_path):
    path = os.path.abspath(relative_path)
    files = [os.path.join(relative_path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    files.sort()
    return files


def frame_numbers(ordered):
    return [int(os.path.splitext(os.path.basename(f))[0]) for f in ordered]


def next(ordered1, i1, ordered2, i2):
    if i1 == -1 and i2 == -1:
        # Have not started either.
        if ordered1[0] == ordered2[0]:
            return (0, 0)
        elif ordered1[0] < ordered2[0]:
            return (0, -1)
        else:
            return (-1, 0)
    elif i1 == -1:
        # Have started in ordered2 but not ordered1.
        if i2 + 1 < len(ordered2):
            if ordered1[0] == ordered2[i2 + 1]:
                return (0, i2 + 1)
            else:
                return (-1,  i2 + 1)
        else:
            return (0, i2 + 1)
    elif i2 == -1:
        # Have started in ordered1 but not ordered2.
        if i1 + 1 < len(ordered1):
            if ordered2[0] == ordered1[i1 + 1]:
                return (i1 + 1, 0)
            else:
                return (i1 + 1, -1)
        else:
            return (i1 + 1, 0)
    elif i1 + 1 >= len(ordered1) and i2 + 1 >= len(ordered2):
        # Have finished both.
        return (len(ordered1), len(ordered2))
    elif i1 + 1 >= len(ordered1):
        # Have finished ordered1.
        return (i1, i2 + 1)
    elif i2 + 1 >= len(ordered2):
        # Have finished ordered2.
        return (i1 + 1, i2)
    elif ordered1[i1 + 1] == ordered2[i2 + 1]:
        return (i1 + 1, i2 + 1)
    else:
        d1 = ordered1[i1 + 1] - ordered1[i1]
        d2 = ordered2[i2 + 1] - ordered2[i2]
        if d1 > 0 and d1 < d2:
            return (i1 + 1, i2)
        else:
            return (i1, i2 + 1)


def paste(im_dest, height, path, top):
    try:
        im = Image.open(path)
    except:
        print("Could not open '" + path + "'")
    try:
        aspect = im.size[0] / im.size[1]
        s = (round(height * aspect), round(height))
        im_resized = im.resize(s)
        im_dest.paste(im_resized, (round(im_dest.size[0] / 2) - round(s[0] / 2), top))
    except:
        print("Could paste '" + path + "'")


def combine(ordered1, ordered2, top_height_frac, output_size, output_dir, fps, frames_only):
    frames1 = frame_numbers(ordered1)
    frames2 = frame_numbers(ordered2)

    if not frames_only:
        output_file = os.path.join(output_dir, "split-screen-video.avi")
        fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
        writer = cv2.VideoWriter(output_file, fourcc, fps, output_size)

    i1 = i2 = -1
    while True:

        i1, i2 = next(frames1, i1, frames2, i2)
        if i1 == len(frames1) and i2 == len(frames2):
            break

        im = Image.new("RGB", output_size)
        height1 = output_size[1] * top_height_frac
        height2 = output_size[1] - height1

        if 0 <= i1 and i1 < len(frames1):
            paste(im, height1, ordered1[i1], 0)
        if 0 <= i2 and i2 < len(frames2):
            paste(im, height2, ordered2[i2], round(height1))

        i = max(i1, i2)
        if frames_only:
            f = os.path.join(output_dir, "{:05d}.png".format(i))
            print("Writing {}".format(f))
            im.save(f)
        else:
            print("Adding frame {}".format(i + 1))
            writer.write(cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR))

    if not frames_only:
        print("Writing {}...".format(output_file))
        writer.release()
        print("Done")   


if __name__ == "__main__":
    argv = sys.argv
    if "--" not in argv:
        argv = []
    else:
        argv = argv[argv.index("--") + 1:]

    parser = argparse.ArgumentParser(argv)
    parser.set_defaults(input_dir1=".")
    parser.add_argument("--inputdir1", "-i1", dest="input_dir1", help="path to input directory for top images")
    parser.set_defaults(input_dir2=".")
    parser.add_argument("--inputdir2", "-i2", dest="input_dir2", help="path to input directory for bottom images")
    parser.set_defaults(top_height_fraction=0.5)
    parser.add_argument("--top", "-t", type=float, dest="top_height_fraction", help="top images' fraction of output height")
    parser.set_defaults(output_width=1920)
    parser.add_argument("--width", "-ow", type=int, dest="output_width", help="output video width")
    parser.set_defaults(output_height=1080)
    parser.add_argument("--height", "-oh", type=int, dest="output_height", help="output video height")
    parser.set_defaults(fps=30)
    parser.add_argument("--fps", "-fps", type=int, dest="fps", help="output frames per second")
    parser.set_defaults(output_height=1080)
    parser.add_argument("--outputdir", "-o", dest="output_dir", help="path to output directory")
    parser.set_defaults(frames_only=False)
    parser.add_argument("--frames", "-f", dest="frames_only", action="store_true", help="output frame images instead of a video")
    args = parser.parse_args()

    print_args(args)
    check_args(args)

    ordered1 = order(args.input_dir1)
    ordered2 = order(args.input_dir2)

    output_size = (args.output_width, args.output_height)
    combine(ordered1, ordered2, args.top_height_fraction, output_size, args.output_dir, args.fps, args.frames_only)