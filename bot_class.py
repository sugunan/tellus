import logging
import configparser


class BotClass:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read("app.properties")
        self.conf_log_path = self.config.get("LogSection", "log.path")
        self.conf_log_level = self.config.get("LogSection", "log.level")

        logging.basicConfig(filename=self.conf_log_path,
                            filemode='w',
                            format='%(name)s - %(levelname)s - %(message)s',
                            level=int(self.conf_log_level))
        logging.debug('Object instantiated')

    def chk(self, http_obj):
        import util_func as uf
        uf.poc("Invoked")
        logging.debug('Check function called')
        http_obj.wfile.write(b"Web output")

    def jsres(self, http_obj):
        import simplejson
        data = simplejson.loads(http_obj.data_string)
        print("{}".format(data))
        http_obj.wfile.write(http_obj.data_string)

    def ask(self, http_obj):
        from nltk.chat.util import Chat, reflections
        from bot_data import BotData
        import simplejson
        data = simplejson.loads(http_obj.data_string)

        obj_bot_data = BotData()

        reflections = obj_bot_data.reflections
        pairs = obj_bot_data.pairs

        chat = Chat(pairs, reflections)
        res = chat.respond(data['chat_text'])

        if res is None:
            res = "Couldn't understand. Could you please more specific?"
        http_response = '{"response": "' + res + '"}'

        http_obj.wfile.write(http_response.encode())

