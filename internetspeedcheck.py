import speedtest
test=speedtest.Speedtest()
dl=test.download()
ul=test.upload()
print(f"Download Speed: {round(dl/(8e+6),1)} MBps")
print(f"Upload Speed: {round(ul/(8e+6),1)} MBps")
