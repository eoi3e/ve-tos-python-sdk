import os.path

import tos

ak = ""
sk = "=="
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

# # bytedance catower平台接入文档（toutiao 版）
# key = "API-catower.bytedance-toutiao.md"

# # 抖音旧版本APK，测试用
# key = "aweme_update_v20.8.0_bate.apk"

# # 头条旧版本APK，测试用
# key = "NewsArticle_update_v8.2.5_beta.apk"

# 备份速查表
key = "速查表-20220720.md"

save_path = os.path.join('output/tos', key)
resp = client.get_object(Bucket=bucket_name, Key=key)
with open(save_path, 'wb') as f:
    f.write(resp.read())