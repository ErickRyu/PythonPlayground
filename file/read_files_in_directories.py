import os
import glob

sample_directory = './test_samples/'


class CheckDirectories():
    @staticmethod
    def check_main_directory():
        if not os.path.exists(sample_directory):
            return False
        return True

    @staticmethod
    def check_sub_directories():
        if not os.path.exists(sample_directory+'sample1/'):
            return False
        if not os.path.exists(sample_directory+'sample2/'):
            return False
        return True


class GetFilenames():
    @staticmethod
    def get_filenames_in(path):
        files = os.listdir(path)

        for name in files:
            print(name)

        filtered_files = glob.glob(path+'*.json')
        numbers = list()
        for filtered_name in filtered_files:
            print(filtered_name)
            numbers = filtered_name.split('/')[-1].split('_')[0]

        return numbers

if __name__ == '__main__':
    print(CheckDirectories.check_main_directory())
    print(CheckDirectories.check_sub_directories())

    GetFilenames.get_filenames_in(sample_directory+'sample1/')
    GetFilenames.get_filenames_in(sample_directory+'sample2/')
