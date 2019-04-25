import os

poppler_path = os.path.join(os.path.abspath(__file__), 'poppler-0.68.0/bin')
path_cmd = 'setx path "%path%;' + poppler_path + '"'
os.system('pip install flask')
os.system('pip install Pillow')
os.system('pip install pandas')
os.system('pip install pdf2image')
os.system(path_cmd)