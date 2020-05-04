from mycroft import MycroftSkill, intent_file_handler


class Religion(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('god.intent')
    def handle_religion(self, message):
        religion = self.settings.get('religion', 'dude')
        self.speak_dialog(religion + '.god')

    def stop(self):
        pass


def create_skill():
    return Religion()
