from aip import AipOcr

# 调用baidu-ocr接口
api_key = 'y54FBquGQL7zkHjKwzOl2gTP'
app_id = '25578790'
secret_key = 'eeDTMB756FHp5gsxTs1rgUY7yUjL7FOl'
options = {"language_type": "CHN_ENG", "detect_direction": "true", "detect_language": "true"}

client = AipOcr(app_id, api_key, secret_key)
with open('身份证.jpg', 'rb') as f:
    image = f.read()
    inf = client.basicGeneral(image, options)
    for words in inf['words_result']:
        print(words['words'])
