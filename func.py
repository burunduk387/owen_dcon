def calc_chk(s):
    sum = 0
    for c in s:
        sum += ord(c)
    sum = sum % 256
    return '%2X' % (sum & 0xFF)
def ask_value_cmd(device_address, channel):
    device_address = hex(device_address)[2:]
    channel = str(channel)
    cmd = "#" + device_address + channel
    cmd = cmd + calc_chk(cmd) + "\r"
    return cmd.encode("utf-8")
def read_mv():
    ans = ""
    for i in range(32):
        ch = ser.read().decode("ascii")
        ans += ch
        if ch == "\r":
            break
    return ans[1:-3]
