oaid = "askdasjdjalsdkj"
outlet_key = "dazn-italy"
feed_base_url = 'https://api.daznfeeds.com/livestream'

feed_url = (
    f'{feed_base_url}/{outlet_key}/{oaid}'
    '?_rt=b&_fmt=json'
    '&_fld=desc,oid,sid,sts,set,sst,oaId,al,ptr,cc,lnk.urn:perform:mfl:fixture,rid'
    )

print(feed_url)

m2a_cloud_api = "http://google.com"
organisation = "org12121"
target_account = "ta23232"
m2a_cloud_event_id="ev23131"
m2a_cloud_url = (
        f"{m2a_cloud_api}/api/connect/v1",
        f"/organisations/{organisation}",
        f"/target-accounts/{target_account}",
        f"/events/{m2a_cloud_event_id}"
    )

print("".join(m2a_cloud_url))