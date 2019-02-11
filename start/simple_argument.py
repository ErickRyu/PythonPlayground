import argparse
p = argparse.ArgumentParser()
p.add_argument('foo')
p.add_argument('bar')


if __name__ == "__main__":
    args = p.parse_args()
    print(**vars(args))

