def get_path_list():
    path_list = ['/bot_class/chk/', '/bot_class/jsres/', '/bot_class/ask/']
    return path_list


def uri_func(http_obj):
    path_list = get_path_list()
    if http_obj.path in path_list:
        import importlib
        uri_section = http_obj.path.split("/")
        class_name = ""
        for word in uri_section[1].split("_"):
            class_name = class_name + word.capitalize()
        module = importlib.import_module(uri_section[1])
        my_class = getattr(module, class_name)
        newClass = my_class()
        return getattr(newClass, uri_section[2])(http_obj)


def poc(var):
    print(var)