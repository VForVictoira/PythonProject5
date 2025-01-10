import json


html_json = '{"success": true, "code": "\u884c\u52a8\u4ee3\u53f7\uff1a\u54ce\u54df\u4e0d\u9519\u54e6"}'
html_dict = json.loads(html_json)
print(html_dict)