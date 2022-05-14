#!/usr/bin/python

from datetime import datetime


def control_sum(str):
    return sum(map(ord, list(str)))


def check(reply):
    def _is_number(str):
        try:
            int(str)
            return True
        except ValueError:
            return False

    if "Control sum:" not in reply:
        return False
    parts = reply.split("Control sum:")
    received_current_time = parts[0].strip()
    received_control_sum = parts[1].strip()
    if not _is_number(received_control_sum):
        return False
    else:
        received_control_sum = int(received_control_sum)
    expected_control_sum = control_sum(received_current_time)
    return expected_control_sum == received_control_sum


current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(current_time)
print("Control sum: " + str(control_sum(current_time)))

#print check(current_time + '\n' + "Control sum: " + str(control_sum(current_time)))