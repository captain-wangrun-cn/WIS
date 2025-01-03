import data,secure

def allowed_file(filename):
    # 检查文件扩展名是否允许
    return '.' in filename and \
           filename.split('.', 1)[1].lower() in data.get_value("allowed_extensions")

def get_paths() -> dict:
    # 获取文件夹路径
    return data.get_value("path")

def get_path_by_key(key: str) -> str:
    # 根据 key 获取文件夹路径
    return data.get_value("path")[key]

def save_file(path: str, content: bytes):
    # 保存文件
    with open(path, 'wb+') as file:
        file.write(content)

def get_encrypted_file(path: str) -> bytes:
    # 获取文件
    with open(path, 'rb') as file:
        return secure.decrypt(file.read())
