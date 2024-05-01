import re

import cv2
from pathlib import Path


with open('readme.md', encoding='utf8') as f:
    s = f.read()
s = re.sub(r'\.((png)|(jpg))\b', '.webp', s)
with open('readme.md', 'w', encoding='utf8') as f:
    f.write(s)


for i in [*Path('.').glob('*.jpg'), *Path('.').glob('*.png')]:
    img = cv2.imread(str(i))
    if max(img.shape) > 400:
        r = 400 / max(img.shape)
        img = cv2.resize(img, [int(img.shape[1]*r), int(img.shape[0] * r)], interpolation=cv2.INTER_AREA)
    for q in range(80, 20, -10):
        cv2.imwrite(str(i.with_suffix('.webp')), img, [cv2.IMWRITE_WEBP_QUALITY, q])
        if i.with_suffix('.webp').stat().st_size < 512 * 1024:
            break
