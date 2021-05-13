# -*- coding: UTF-8 -*-
import logging
import os
import sys

logging.basicConfig(
    format='',
    level=logging.INFO
)

"""
# tmp.time
convert -loop 0 -delay 26 /Users/beer/data/playlog/1/0.png -delay 6 /Users/beer/data/playlog/1/1.png -delay 6 /Users/beer/data/playlog/1/2.png -delay 6 /Users/beer/data/playlog/1/3.png -delay 6 /Users/beer/data/playlog/1/4.png -delay 6 /Users/beer/data/playlog/1/5.png -delay 6 /Users/beer/data/playlog/1/6.png -delay 6 /Users/beer/data/playlog/1/7.png -delay 6 /Users/beer/data/playlog/1/8.png -delay 46 /Users/beer/data/playlog/1/9.png -delay 6 /Users/beer/data/playlog/1/10.png -delay 6 /Users/beer/data/playlog/1/11.png -delay 6 /Users/beer/data/playlog/1/12.png -delay 6 /Users/beer/data/playlog/1/13.png -delay 6 /Users/beer/data/playlog/1/14.png -delay 13 /Users/beer/data/playlog/1/15.png -delay 6 /Users/beer/data/playlog/1/16.png -delay 6 /Users/beer/data/playlog/1/17.png -delay 13 /Users/beer/data/playlog/1/18.png -delay 46 /Users/beer/data/playlog/1/19.png -delay 19 /Users/beer/data/playlog/1/20.png -delay 13 /Users/beer/data/playlog/1/21.png -delay 13 /Users/beer/data/playlog/1/22.png -delay 6 /Users/beer/data/playlog/1/23.png -delay 100 /Users/beer/data/playlog/1/24.png -layers Optimize gif:- | gifsicle  -o /Users/beer/data/playlog/1 -

# result.time
file '/Users/beer/data/playlog/1/0.png'
duration 0.26
file '/Users/beer/data/playlog/1/1.png'
duration 0.06
file '/Users/beer/data/playlog/1/2.png'
duration 0.06
file '/Users/beer/data/playlog/1/3.png'
duration 0.06
file '/Users/beer/data/playlog/1/4.png'
duration 0.06
file '/Users/beer/data/playlog/1/5.png'
duration 0.06
file '/Users/beer/data/playlog/1/6.png'
duration 0.06
file '/Users/beer/data/playlog/1/7.png'
duration 0.06
file '/Users/beer/data/playlog/1/8.png'
duration 0.06
file '/Users/beer/data/playlog/1/9.png'
duration 0.46
file '/Users/beer/data/playlog/1/10.png'
duration 0.06
file '/Users/beer/data/playlog/1/11.png'
duration 0.06
file '/Users/beer/data/playlog/1/12.png'
duration 0.06
file '/Users/beer/data/playlog/1/13.png'
duration 0.06
file '/Users/beer/data/playlog/1/14.png'
duration 0.06
file '/Users/beer/data/playlog/1/15.png'
duration 0.13
file '/Users/beer/data/playlog/1/16.png'
duration 0.06
file '/Users/beer/data/playlog/1/17.png'
duration 0.06
file '/Users/beer/data/playlog/1/18.png'
duration 0.13
file '/Users/beer/data/playlog/1/19.png'
duration 0.46
file '/Users/beer/data/playlog/1/20.png'
duration 0.19
file '/Users/beer/data/playlog/1/21.png'
duration 0.13
file '/Users/beer/data/playlog/1/22.png'
duration 0.13
file '/Users/beer/data/playlog/1/23.png'
duration 0.06
"""


def main(path):
    str_arr = []
    with open(path, 'r') as f:
        for _ in f.read():
            str_arr.append(_)
    s = ''.join(str_arr)

    paths = path.split('/')
    paths[-1] = 'result.time'
    with open('/'.join(paths), 'w') as f:
        for _ in s.split('-delay'):
            if _.strip().endswith("png"):
                s = _.strip().split(' ')
                f.write("file '{}'".format(s[1]))
                f.write('\n')
                f.write('duration {}'.format(float(s[0]) / 100.0))
                f.write('\n')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        logging.info('Must set .time file')
        exit()
    p = sys.argv[1]
    if not os.path.exists(p):
        logging.info('Error path: {}'.format(p))
        exit()
    main(p)
