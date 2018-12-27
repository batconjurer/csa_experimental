from collections import namedtuple
import numpy as np

PyConn = namedtuple("PyConn", " depart_time, arrive_time, depart_station, arrive_station")
PyNode = namedtuple("PyNode", "score current previous")
speed = 1.4

def csa(dep_stn, arr_stn, conns, table):
    earliest_arrival = {dep_stn: 0}
    for conn in conns:
        if conn.arrive_time > earliest_arrival.get([conn.arrive_station], 0):
            continue
        for neighbor, distance in table[conn.depart_station]:
            if earliest_arrival[neighbor] + distance / speed < conn.depart_time:
                earliest_arrival[conn.arrive_station] = conn.arrive_time
        check = earliest_arrival.get(arr_stn, None)
        if check and check < conn.depart_time:
            return check



if __name__ == '__main__':


