import argparse
import os
import subprocess


if __name__ == "__main__":
    """
    This script is used to stitch together stills into an mp4 video using ffmpeg.
    This script requires ffmpeg to be installed (you can install ffmpeg using the
    command `apt-get install ffmpeg`.

    Usage:
        python stitchVideo.py <video name> \
            --input-dir <input directory> \
            --output-dir <output directory>

    This command will stitch together stills found in <input directory>, and
    output a video titled `MM_Tech_720_<video_name>.mp4` in the <output
    directory>.
    """
    parser = argparse.ArgumentParser(description="Process input video")
    parser.add_argument(
        "name", metavar="name", type=str, help="Name of the video (excluding ext)"
    )
    parser.add_argument(
        "--input-dir",
        help="The input image directory of frames to stitch together.",
        required=True,
    )
    parser.add_argument(
        "--output-dir", help="The output directory to save video to.",
        default='video'
    )
    args = parser.parse_args()

    assert os.path.exists(args.input_dir), "`{}` does not exist".format(args.input_dir)
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    subprocess.run(
        "ffmpeg -r 30 -pattern_type glob -i '{}/*.png' -vcodec libx264 -crf 10 -vf scale=720:540,setsar=1:1 -pix_fmt yuv420p ./{}/MM_Teco_720_{}.mp4".format(
            args.input_dir, args.output_dir, args.name
        ),
        shell=True,
        check=True,
    )
