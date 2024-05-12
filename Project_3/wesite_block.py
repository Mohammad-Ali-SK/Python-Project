import speedtest


def speedchech():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + "Mbps"
    print(down)
speedchech()