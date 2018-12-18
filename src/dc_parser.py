import argparse

def parameter_parser():

    parser = argparse.ArgumentParser(description = "Run GF.")

    '''
    data cleaning
    '''
    parser.add_argument('--input_file_name',
                        nargs = '?',
                        default = './data/network_friends_all.txt',
                        help = 'Input file name of data cleaning.')

    parser.add_argument('--output_file_name',
                        nargs = '?',
                        default = './data/mid_network_friends.txt',
                        help = 'The output file name of data cleaning.')

    '''
    calculate perception
    '''
    parser.add_argument('--start_id',
                        nargs = '?',
                        default = 0,
                        type = int,
                        help = 'The start node id of calculating perception.')

    parser.add_argument('--end_id',
                        nargs = '?',
                        default = 5,
                        type = int,
                        help = 'The end node id of calculating perception.')

    parser.add_argument('--worker_id',
                        nargs = '?',
                        default = 0,
                        type = int,
                        help = 'The worker id of calculating perception.')

    return parser.parse_args()
