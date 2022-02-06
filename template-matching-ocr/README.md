# 信用卡识别
所需要的arguments
```python
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
ap.add_argument("-t", "--template", required=True,
                help="path to template OCR-A image")
```

运行示例代码
`python orc_template_match.py -i images/credit_card_01.png -t ocr_a_reference.png`

项目采用模板匹配的方法来做识别，运行实例结果如下

![running picture](screenshot.png)

**注意图片路径中不能含中文**
