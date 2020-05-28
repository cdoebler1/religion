from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import random


class Religion(MycroftSkill):

    @intent_handler(IntentBuilder('Doyoubelieveingod').require('believe').
                    require('god'))
    def handle_god(self, message):
        religion = self.settings.get('religion', 'pasta')
        self.speak_dialog(religion + '.god')

    @intent_handler(IntentBuilder('ReciteDDC').require('recite').
                    require('ddc'))
    def handle_ddc(self, message):
        self.speak_dialog('intro')
        a = random.randint(1, 15)
        with open('skills/religion.cdoebler1/dudeism/ddc_' + str(a)
                  + '.txt') as file_object:
            book = file_object.read()
            self.speak("From the Dude de Ching, Verse " + str(a))
            self.speak(book)

    @intent_handler(IntentBuilder('ReciteIRRUD').require('recite').
                    require('irrud'))
    def handle_irrud(self, message):
        a = random.randint(1, 8)
        a = self.get_response('What verse would you like to hear?')
        with open('skills/religion.cdoebler1/pasta/irrud_' + str(a)
                  + '.txt') as file_object:
            book = file_object.read()
            self.speak("""From the Gospel of the Flying Spaghetti Monster,
            I'd really rather you didn't"""
                       + str(a))
            self.speak(book)

    def stop(self):
        pass


def create_skill():
    return Religion()
