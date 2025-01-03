# WIS（W Image Storage）
## 📃简介
一个简易的图床，支持对文件进行加密（AES-256）
## ⚙️配置
在`config.json`中配置API信息
```
{
    "path": {
        "REQUEST_PATH_1": "PATH_TO_YOUR_LOCAL_DIR_1",
        "REQUEST_PATH_2": "PATH_TO_YOUR_LOCAL_DIR_2"
    },
    "allowed_extensions": ["jpg", "png", "webp", "jpeg", "gif"],

    "access_key": "ACCESS_KEY_ID",
    "secret_key": "SECRET_ACCESS_KEY"
}
```
- `path`字段是一个字典，代表`请求路径`对应的`本地文件夹`
- `allowed_extensions`字段是一个列表，代表允许上传的文件后缀名
- `access_key`和`secret_key`字段代表你的API密钥，这个秘钥在第三方程序请求到你的服务器时会使用
## 🚀使用
### 1. 上传文件
>`/api/upload`
>
>请求方式：POST
>
>请求参数（JSON）：
>
>| 字段 | 类型 | 说明 |
>| --- | --- | ---|
>| filename | str | 文件名|
>| path | str | 上传路径 |
>| file | str | 图片base64字符串 |
>| need_secure | bool | 是否需要加密 |
### 2. 获取文件
>`/api/get_img?filename=xxx&path=xxx`
>
>请求方式：GET | POST
>请求参数（URL）：
>| 字段 | 类型 | 说明 |
>| --- | --- | ---|
>| filename | str | 文件名|
>| path | str | 路径 |
## 🍻开源协议
```
MIT License

Copyright (c) 2025 WANGRUN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
