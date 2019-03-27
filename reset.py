from shutil import copyfile
import shutil
import os

root = os.path.dirname(os.path.abspath(__file__))

incoming_folder = os.path.join(root, 'incoming/')
analyzed_folder = os.path.join(root, 'analyzed/')
results_folder = os.path.join(root, 'results/')

shutil.rmtree(incoming_folder)
shutil.rmtree(analyzed_folder)
shutil.rmtree(results_folder)
os.mkdir(incoming_folder)
os.mkdir(analyzed_folder)
os.mkdir(results_folder)

source = (os.path.join(root, "all_results_template.csv"))
dest = (os.path.join(results_folder, "all_results.csv"))
copyfile(source, dest)