import os

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

if __name__ == '__main__':
    print(CheckDirectories.check_main_directory())
    print(CheckDirectories.check_sub_directories())

    GetFilenames.get_filenames_in(sample_directory+'sample1/')