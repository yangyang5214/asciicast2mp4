# -*- coding: UTF-8 -*-


def main(path: str):
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
    path = '/Users/beer/data/playlog/2/tmp.ts'
    main(path)
