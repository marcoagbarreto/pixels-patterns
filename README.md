# pixels-patterns

This is a program to generate random pixel patterns.
Random patterns are useful in computer vision by serving as markers for orienting objects in 3D space.
* If you want to check out the stand-alone version, visit **[pixelsPatterns.exe](https://github.com/marcoagbarreto/pixelsPatterns.exe)**
* [Click here for the live version](https://pixels-patterns.onrender.com/generate)

## Example

1. Run [pixels-patterns](https://pixels-patterns.onrender.com/generate).
2. Hit Generate.
3. Profit.
4. Save the image.

![example](pixelspatterns.gif)

## Code Usage

clone the repository (no installation required, source files are sufficient):
        
[//]: # (    https://github.com/marcoagbarreto/pixelsPatterns.git)

dependencies:

    from flask import Flask, render_template, request, jsonify
    from PIL import Image
    import base64
    import webcolors
    import io
    import random

[//]: # (or [download and extract the zip]&#40;https://github.com/marcoagbarreto/pixelsPatterns/archive/main.zip&#41; into your project folder.)

## Known limitations:
* Images are upscale x10 from original resolution, this might add noise to the image.

