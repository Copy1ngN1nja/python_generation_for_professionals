import cairosvg
import os
input_path = os.path.expanduser('~/Downloads/hakathon_bashnya.svg')
output_path = os.path.expanduser('~/Downloads/output.pdf')

with open(input_path, 'rb') as svg_file:
    cairosvg.svg2pdf(file_obj=svg_file, write_to=output_path)