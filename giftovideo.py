import os
import subprocess

while (True):
    x = input("enter key:")
    print('[change directory]')
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system('cd ' + os.getcwd())
    os.system('ffmpeg -i '+x+'.gif -r 20 -c:v libx264 -b:v 15M -vf "scale=2564:-1:flags=neighbor" -pix_fmt yuv420p '+x+'.mp4')
    os.system('ffmpeg -i '+x+'.gif -filter:v fps=16 -ss 0 -t 4 '+x+'2.gif')  
    os.system('ffmpeg -i '+x+'.gif -c:v libvpx -auto-alt-ref 0 -b:v 3M '+x+'.webm')  


    
