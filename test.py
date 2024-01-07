import requests

url = "https://sun3-7.userapi.com/impf/zAfxasKjFiiSFI1FLBaRb-MKtO5t3a29rL4biw/tC_rR_c__dk.jpg?size=1000x1000&quality=95&sign=1a95d2a6fdb2456417753578fb8de6ea&c_uniq_tag=TmI2pm1SMjqVCnLNE0Ap4Db6sSc1W4bEm2EGVR5zMT8&type=album"
response = requests.get(url)
if response.status_code == 200:
    with open("./media/users/sample.jpg", 'wb') as f:
        f.write(response.content)