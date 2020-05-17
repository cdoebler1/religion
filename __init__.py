from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import random


class Religion(MycroftSkill):

    @intent_handler(IntentBuilder('Doyoubelieveingod').require('believe').
                    require('god'))
    def handle_god(self, message):
        religion = self.settings.get('religion', 'dude')
        self.speak_dialog(religion + '.god')

    @intent_handler(IntentBuilder('ReciteDDC').require('recite').
                    require('ddc'))
    def handle_ddc(self, message):
        self.speak_dialog('intro')
        a = random.randint(1, 4)
        with open('skills/religion.cdoebler1/dialog/en-us/ddc_' + str(a)
                  + '.dialog') as file_object:
            book = file_object.read()
            self.speak("From the Dude de Ching, Verse " + str(a))
            self.speak(book)

    def stop(self):
        pass

def create_skill():
    return Religion()
