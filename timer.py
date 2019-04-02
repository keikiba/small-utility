import time

class Timer:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
        self.lap_time = 0
        self.result = 0

    def start(self):
        self.start_time= time.time()

    def stop(self):
        self.stop_time = time.time()
        self.result = self.stop_time - self.start_time

    def get_result(self):
        secs = int(self.result)
        msec = self.result - secs
        hr = int(secs / 3600)
        mn = int((secs % 3600) / 60)
        se = int(secs % 60)
        ms = (self.result - secs) * 1000
        return (hr, mn, se, ms)

    def get_result_string(self):
        (hr, mn, se, ms) = self.get_result()
        s = ''
        if hr > 0:
            s += "{}hour ".format(hr)
        if mn > 0:
            s += "{}min ".format(mn)
        if se > 0:
            s += "{}sec ".format(se)
        s += "{:.3f}ms".format(ms)
        return s

def test_main():
    pass

if __name__ == "__main__":
    test_main()
