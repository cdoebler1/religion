from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from word2number import w2n
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
        with open('skills/winston-religion.cdoebler1/dudeism/ddc_' + str(a)
                  + '.txt') as file_object:
            book = file_object.read()
            self.speak("From the Dude de Ching, Verse " + str(a))
            self.speak(book)

    @intent_handler(IntentBuilder('ReciteIRRUD').require('recite').
                    require('irrud'))
    def handle_irrud(self, message):
        a = self.get_response('What verse would you like to hear?')
        if a == "all" or a == "everything":
            i = 1
            while i < 9:
                with open('skills/winston-religion.cdoebler1/pasta/irrud_' + str(i)
                          + '.txt') as file_object:
                    book = file_object.read()
                    self.speak("""From the Gospel of the Flying Spaghetti Monster,
                    I'd really rather you didn't, number """
                               + str(i))
                    self.speak(book)
                i = i + 1
        else:
            try:
                a = w2n.word_to_num(a)
            except Exception:
                a = random.randint(1, 8)
            if a < 1 or a > 8:
                a = random.randint(1, 8)
            with open('skills/winston-religion.cdoebler1/pasta/irrud_' + str(a)
                      + '.txt') as file_object:
                book = file_object.read()
                self.speak("""From the Gospel of the Flying Spaghetti Monster,
                I'd really rather you didn't, number """
                           + str(a))
                self.speak(book)

    def stop(self):
        pass


def create_skill():
    return Religion()
