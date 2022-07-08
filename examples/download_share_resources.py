import os.path

import tos

ak = "AKLTNTMxYzE5NWFkYWM3YzBmYzA2ZWI2OGQ0MjRmMTVmYzE"
sk = "TUdKbVpUUmxOVFZsWm1Zd05EaGlNekk1TWpVM1kyTTFOekpoWXpnME5XSQ=="
endpoint = "tos-cn-beijing.volces.com:80"
region = "cn-beijing"


client = tos.TosClient(tos.Auth(ak, sk, region), endpoint)

# toutiao-中台架构-API组资源共享TOS（李晨）
bucket_name = "test-toutiao-tos-lichen"

# 查看已有文件内容
resp = client.list_objects(Bucket=bucket_name)
for x in resp.object_list:
    print("文件名: {}".format(x.key))


# 下载文件

# bytedance catower平台接入文档（toutiao 版）
key = "API-catower.bytedance-toutiao.md"

save_path = os.path.join('output/tos', key)
resp = client.get_object(Bucket=bucket_name, Key=key)
with open(save_path, 'wb') as f:
    f.write(resp.read())