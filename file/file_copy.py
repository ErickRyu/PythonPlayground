import shutil
import os
import glob
import logging


src_dir = './201812'
dest_dir = './Leuven/201812'

if __name__ == "__main__":
    logging.basicConfig(filename='copy.log', level=logging.INFO)
    for filename in glob.glob(os.path.join(src_dir, '*.*')):
        try:
            shutil.copy(filename, dest_dir)
        except Exception as e:
            logging.error(e)