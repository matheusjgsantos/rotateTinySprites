# rotateTinySprites
Python script to rotate sprites created using Jannone's [TinySprite](http://msx.jannone.org/tinysprite/tinysprite.html) webtool

##Usage

 - Create a single slot sprite in the TineSprite site
 - Export the sprite as backup
 - Copy the exported data and paste it in a text editor
 - Save the file at the same directory where the script is located
 - Finally, run the script passing the sprite file name at the --input parameter
 - The output file can be used in Tiny Sprite using the load backup option

```./rotateSprite.py --help
usage: rotateSprite.py [-h] --input INPUT [--output OUTPUT] [--theta THETA]
                       [--interval INTERVAL] [--frames FRAMES]

Rotate sprites from tinysprite

optional arguments:
  -h, --help           show this help message and exit
  --input INPUT        Backup file from tinysprite. Default is tinysprite.spr
  --output OUTPUT      Destination file
  --theta THETA        Angle value
  --interval INTERVAL  Time interval between frames. Defaul=0.2
  --frames FRAMES      Number of frames to generate. Default=6.2
  --angle ANGLE        Value for the initial angle. Default=0
```


##Example

This is a small sample from the rotating script results:

![Rotating plane](pics/rotating_plane.gif)

##Troubleshoot

 - If the scripts fails due to missing **env** program just run it using `python3 ./rotateSprite.py`
