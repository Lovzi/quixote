import time
import requests


def get_citydata(self):
    if len(self.citytoaircode) > 0:
        return
    url = 'http://www.flycua.com/app/hierarchy/hotCity'
    time_data = {"_": int(time.time() * 1000)}
    response = requests.get(url, data=time_data, timeout=self.timeout)
    citysrc = response.json()
    city_dict = {}
    for k, v in citysrc.items():
        if k in ["D_hotCity", "I_hotCity", "Asia"]:
            for i in v:
                city_dict[i["Name"]] = (i["cityCode"], i["airCode"])

        if k in ["ABCD", "EFGHJ", "KLMNOP", "QRSTW", "XYZ"]:
            for j in v:
                for k1, v1 in j.items():
                    for i in v1:
                        s = []
                        s.append(i["cityCode"])
                        s.append(i["airCode"])
                        city_dict[i["Name"]] = s
                        del s
    for k, v in city_dict.items():
        self.citytoaircode[k] = v[0]
        self.airnametocode[k] = v[1]




