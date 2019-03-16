import sys
import argparse

if __name__ == "__main__":

    print(sys.argv)
    parser = argparse.ArgumentParser()

    parser.add_argument('items', metavar='N', type=str, nargs='+', help='items to show')
    parser.add_argument('-c', '--client_id', type=str, default='', help='input client_id if it has')

    args = vars(parser.parse_args())
    print(args['client_id'])
    print(args)

    #print("Hi there {}, it's nice to meet you!".format(args["name"]))
