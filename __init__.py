from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class Religion(MycroftSkill):

    @intent_handler(IntentBuilder('Doyoubelieveingod').require('believe').
                    require('god'))
    def handle_god(self, message):
        religion = self.settings.get('religion', 'dude')
        self.speak_dialog(religion + '.god')

    def stop(self):
        pass


def create_skill():
    return Religion()
