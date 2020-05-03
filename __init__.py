from mycroft import MycroftSkill, intent_file_handler
import subprocess


class SmallTalk(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('winston.about.intent')
    def handle_winston_about(self, message):
        self.speak_dialog('winston.about')

    def stop(self):
        pass


def create_skill():
    return SmallTalk()
