# -*- coding: UTF-8 -*-
import struct
import json
import sys

OP_OPEN, OP_CLOSE, OP_WRITE, OP_EXEC = 1, 2, 3, 4
TTYSTRUCT = '<iLiiLL'


def main(logfile):
    datas = []
    with open(logfile, 'rb') as fd:
        ssize = struct.calcsize(TTYSTRUCT)
        currtty, prevtime, prefdir = 0, 0, 0

        time_flag = 0
        while 1:
            sleeptime = 0
            try:
                (op, tty, length, dir, sec, usec) = struct.unpack(TTYSTRUCT, fd.read(ssize))
                data = fd.read(length)
            except struct.error:
                break

            if currtty == 0: currtty = tty

            if str(tty) == str(currtty) and op == OP_WRITE:
                # the first stream seen is considered 'output'
                if prefdir == 0:
                    prefdir = dir
                    # use the other direction
                if dir == prefdir:
                    curtime = float(sec) + float(usec) / 1000000
                    if prevtime != 0:
                        sleeptime = curtime - prevtime
                    prevtime = curtime
                    cmd_str = data.decode('utf-8')
                    if cmd_str.endswith('\n'):
                        cmd_str = cmd_str.replace('\n', '\r\n')
                    datas.append([float("%.6f" % time_flag), "o", cmd_str])
                    time_flag = time_flag + sleeptime
            elif str(tty) == str(currtty) and op == OP_CLOSE:
                break

    cast_file = logfile.split('.')[0] + '.cast'
    with open(cast_file, 'w') as f:
        f.write('{"version": 2, "width": 200, "height": 50, "timestamp": 1623049435, "env": {"SHELL": "/bin/bash", "TERM": "xterm-256color"}}')
        f.write("\n")
        for d in datas:
            f.write(json.dumps(d))
            f.write("\n")
    return cast_file


if __name__ == '__main__':
    main(sys.argv[1])
