# split-screen-video

## Summary

This script combines two sets of frames into a split-screen video (with one set above the other).  Sparse sampling in the frames is expanded, as illustrated in this example.  The first set contains six frames, `001.png` through `006.png`:
<p align="center">
<img src="example-input1.png">
</p>

The second set contains only two frames, `002.png` and `004.png`:
<p align="center">
<img src="example-input2.png">
</p>

The combined result aligns the two sets by frame number and expands the sparse sampling in the second set:
<p align="center">
<img src="example-output.png">
</p>

## Installation

This script uses the [Pillow](https://anaconda.org/conda-forge/pillow) package for resizing input images, and the [OpenCV](https://anaconda.org/conda-forge/opencv) package for writing them to video, with OpenCV using [FFMpeg](https://anaconda.org/conda-forge/ffmpeg). An easy way to install these dependencies is to use [Conda](https://docs.conda.io/en/latest/miniconda.html).  Here is how to create a new Conda environment named "video", and to install the dependencies in this environment:

```
conda create --name video
conda activate video
conda install -c conda-forge pillow ffmpeg opencv
```

It is important to install with the option: `-c conda-forge`.  Without it, Pillow and OpenCV will install, but the use of `cv2.VideoWriter` will fail, producing error messages mentioning "OpenCV | GStreamer warning: cannot link elements".

## Usage

The following command will read the first set of input frames from `/tmp/framesA` and the second set from `/tmp/framesB`, and will write an output video `/tmp/AB/split-screen-video.avi`, with the first set of input frames occupying the top half of the video, and the video having a standard 1080P resolution (1920 horizontal, 1080 vertical, 30 frames per second):
```
python split-screen-video/splitScreenVideo.py -i1 /tmp/framesA -i2 /tmp/framesB -o /tmp/AB
```

The `-t` argument changes the fraction occupied by the first set of frames, for example, to the top quarter of the video:
```
python split-screen-video/splitScreenVideo.py -i1 /tmp/framesA -i2 /tmp/framesB -o /tmp/AB -t 0.25
```

The `-ow` and `-oh` arguments change the output width and height, for example, to 780P:
```
python split-screen-video/splitScreenVideo.py -i1 /tmp/framesA -i2 /tmp/framesB -o /tmp/AB -ow 1280 -oh 780
```

The `-fps` argument changes the frames per second:
```
python split-screen-video/splitScreenVideo.py -i1 /tmp/framesA -i2 /tmp/framesB -o /tmp/AB -fps 60
```

The `-f` argument causes the individual frames to be written to the output directory (e.g., `/tmp/AB`) in place of the assembled video:
```
python split-screen-video/splitScreenVideo.py -i1 /tmp/framesA -i2 /tmp/framesB -o /tmp/AB -f
```

## Testing

Run the unit tests as follows:
```
python split-screen-video/test_splitScreenVideo.py
```
