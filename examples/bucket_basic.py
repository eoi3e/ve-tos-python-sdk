import tos

ak = "AKLTNTMxYzE5NWFkYWM3YzBmYzA2ZWI2OGQ0MjRmMTVmYzE"
sk = "TUdKbVpUUmxOVFZsWm1Zd05EaGlNekk1TWpVM1kyTTFOekpoWXpnME5XSQ=="
endpoint = "tos-cn-beijing.volces.com:80"
region = "cn-beijing"
bucket_name = "test-toutiao-tos-lichen-beijing"
key_name = "test"


client = tos.TosClient(tos.Auth(ak, sk, region), endpoint)
try:
    resp = client.create_bucket(Bucket=bucket_name, ACL="public-read")
    assert resp.status == 200

    resp = client.list_buckets()
    assert resp.status == 200

    bucket_names = []
    for bucket in resp.bucket_list:
        bucket_names.append(bucket.name)
    if bucket_name not in bucket_names:
        assert False

    resp = client.head_bucket(Bucket=bucket_name)
    assert resp.status == 200
    assert resp.region != ''
except Exception as e:
    print(e)
finally:
    resp = client.delete_bucket(Bucket=bucket_name)
    assert resp.status == 204
