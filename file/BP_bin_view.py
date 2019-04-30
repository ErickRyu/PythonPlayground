
filename = '1555916357_rawHexBPfile.bin'
path_to_file = './test_samples/' + filename


def read_raw_hex():
    with open(path_to_file, "rb") as binary_file:
        return binary_file.read()


if __name__ == "__main__":

    plain_txt = read_raw_hex()

    for i in range(int(len(plain_txt)/20)):
        #print(plain_txt[i*20:i*20+20])
        print('Ccnt: ', int(plain_txt[i*20 + 12]), '\tVcnt: ', int(plain_txt[i*20 + 17]), '\tSeq: ', int(plain_txt[i*20 + 18]))
