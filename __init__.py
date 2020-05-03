from mycroft import MycroftSkill, intent_file_handler


class Religion(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('religion.intent')
    def handle_religion(self, message):
        self.speak_dialog('religion')

    def stop(self):
        pass


def create_skill():
    return Religion()
