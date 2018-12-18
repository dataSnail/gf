import argparse

def parameter_parser():

    parser = argparse.ArgumentParser(description = "Run GF.")

    parser.add_argument('--input_file_name',
                        nargs = '?',
                        default = './data/network_friends_all.txt',
                        help = 'Input file name.')

    parser.add_argument('--output_file_name',
                        nargs = '?',
                        default = './data/network_friends_test.txt',
                        help = 'The output file name.')
                    
    return parser.parse_args()
    
def madd(x,y):
    print('woc')
    return x+y

# print(madd(1,2))

