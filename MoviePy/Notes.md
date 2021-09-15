# Moviepy

## Preface

> MoviePy is a Python module for video editing, which can be used for basic operations (like cuts, concatenations, title insertions), video compositing (a.k.a. non-linear editing), video processing, or to create advanced effects. It can read and write the most common video formats, including GIF.
>
> Visit the [official website](https://zulko.github.io/moviepy/index.html) to learn more.





## Application

### 1. Concatenate

```python
from moviepy.editor import *
import os

L = [VideoFileClip(file) for file in os.listdir(".")]
# Custom file rules 
concat = concatenate_videoclips(L)
concat.to_videofile("./concat.mp4", fps=24, remove_temp=False)
```

