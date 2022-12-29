
import subprocess
from pathlib import Path
from typing import Dict
import random
import hashlib
##import pyexiv2

print(hashlib.md5(open('merged.mp4','rb').read()).hexdigest())
""" file = open('merged.mp4', 'rb').read()
with open('new_video.mp4', 'wb') as new_video:
  new_video.write(file+'\0')  #here we are adding a null to change the file content

hashlib.md5(open('new_video.mp4','rb').read()).hexdigest() """
#image = pyexiv2.ImageMetadata('cert.jpg')
#image.read()
#image['Exif.Image.ImageDescription'] = '%030x' % random.randrange(256**15)
#image.write()
#hashlib.md5('photo.jpg')

def add_metadata(video: Path, meta: Dict[str, str], save_path: Path = None, overwrite: bool = True):
    print(video,meta,save_path,overwrite)
    if not save_path:
        save_path = video.with_suffix('.metadata' + video.suffix)

    metadata_args = []
    for k, v in meta.items():
        metadata_args.extend([
            '-metadata', f'{k}={v}'
        ])

    args = [
        'ffmpeg',
        '-v', 'quiet',
        '-i', str(video.absolute()),
        '-movflags', 'use_metadata_tags',
        '-map_metadata', '0',
        *metadata_args,
        '-c', 'copy',
        str(save_path)
    ]
    if overwrite:
        args.append('-y')
    proc = subprocess.run(args, stdout=subprocess.PIPE, shell=True)
    proc.check_returncode()


if __name__ == '__main__':
    vid = Path(r'merged.mp4')
    add_metadata(
        vid,
        meta=dict(
            title=vid.stem,
            comment=vid.stem,
            year=2020,
            size = 20,
        ),
    )
