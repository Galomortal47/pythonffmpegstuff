import os
import subprocess
from moviepy.editor import VideoFileClip

while (True):
    x = input("enter key:")
    print('[change directory]')
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system('cd ' + os.getcwd())
    
    clip = VideoFileClip(x+'.gif')
    print( clip.duration )
    os.system('ffmpeg -i '+x+'.gif -r 20 -c:v libx264 -b:v '+str(15000.0/clip.duration*8.0)+'K -vf "scale=2564:1444:flags=neighbor" -pix_fmt yuv420p '+x+'.mp4')
    os.system('ffmpeg -i '+x+'.gif -filter:v fps=16 -ss 0 -t 4 '+x+'2.gif')  
    os.system('ffmpeg -i '+x+'.gif -c:v libvpx -auto-alt-ref 0 -b:v '+str(3.0/clip.duration*8.0)+'M '+x+'.webm')  


    
