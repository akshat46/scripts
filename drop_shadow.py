import sys
import subprocess

#convert input.png \( +clone -background black -shadow 60x5+5+5 \) +swap -background white -layers merge +repage output.png
file_name = sys.argv[1]
subprocess.check_output(['convert', str(file_name), '\( +clone', '-background', 'black', '-shadow', '60x5+5+5', '\)', '+swap', '-background', 'white', '-layers', 'merge', '+repage', 'output.png'])
