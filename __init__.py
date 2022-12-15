from mycroft import MycroftSkill, intent_file_handler


class TemysEmergencyCall(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('call.emergency.temys.intent')
    def handle_call_emergency_temys(self, message):
        self.speak_dialog('call.emergency.temys')


def create_skill():
    return TemysEmergencyCall()

