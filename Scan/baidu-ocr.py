from aip import AipOcr

# 调用baidu-ocr接口，使用你自己申请的
api_key = ''
app_id = ''
secret_key = ''
options = {"language_type": "CHN_ENG", "detect_direction": "true", "detect_language": "true"}

client = AipOcr(app_id, api_key, secret_key)
with open('身份证.jpg', 'rb') as f:
    image = f.read()
    inf = client.basicGeneral(image, options)
    for words in inf['words_result']:
        print(words['words'])
