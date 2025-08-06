import speedtest as st

def run_speedtest():
    test = st.Speedtest()
    
    downspeed = test.download() 
    downspeed = round(downspeed/ 1_000_000, 2)
    print(f"Download Speed: {downspeed} Mbps")
    
    upspeed = test.upload()
    upspeed = round(upspeed / 1_000_000, 2)
    print(f"Upload Speed: {upspeed} Mbps")
run_speedtest()
