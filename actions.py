# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

# ----------------------------------------------------------------------------------------------------------------------------------------

class ActionHowManySymptoms(Action):

	def name(self) -> Text:
		return "action_how_many_s_symptoms"

	def run (self, dispatcher, tracker, domain):

		severe_symptom1 = tracker.get_slot('severe_symptom_one')
		severe_symptom2 = tracker.get_slot('severe_symptom_two')
		severe_symptom3 = tracker.get_slot('severe_symptom_three')
		severe_symptom4 = tracker.get_slot('severe_symptom_four')

		severe_symptoms_list = [severe_symptom1, severe_symptom2, severe_symptom3, severe_symptom4]
		
		true = 1
		false = 0

		if sum(severe_symptoms_list) >= 2:
			dispatcher.utter_message(response="utter_some_severe_symptoms")
		elif sum(severe_symptoms_list) == 1:
			dispatcher.utter_message(response="utter_one_severe_symptoms")
		else:
			dispatcher.utter_message(response="utter_no_severe_symptoms")			

		return[]

class ActionHowManyModerateSymptoms(Action):

	def name(self) -> Text:
		return "action_how_many_m_symptoms"

	def run (self, dispatcher, tracker, domain):

		moderate_symptom1 = tracker.get_slot('moderate_symptom_one')
		moderate_symptom2 = tracker.get_slot('moderate_symptom_two')
		moderate_symptom3 = tracker.get_slot('moderate_symptom_three')
		moderate_symptom4 = tracker.get_slot('moderate_symptom_four')

		moderate_symptoms_list = [moderate_symptom1, moderate_symptom2, moderate_symptom3, moderate_symptom4]

		true = 1
		false = 0

		if sum(moderate_symptoms_list) >= 2:
			dispatcher.utter_message(response="utter_some_moderate_symptoms")
		elif sum(moderate_symptoms_list) == 1:
			dispatcher.utter_message(response="utter_one_moderate_symptoms")
		else:
			dispatcher.utter_message(response="utter_no_moderate_symptoms")

		return[]

		# if severe_symptom1 == "True":
		# 	dispatcher.utter_message(text="Symptom True")
		# elif severe_symptom1 == "False":
		# 	dispatcher.utter_message(text="Symptom False")
		# elif severe_symptom1 == 'false':
		# 	res = "Symptom False"

		# if severe_symptom_1 is True and severe_symptom_2 is True and severe_symptom_3 is True and severe_symptom_4 is True:
		# 	dispatcher.utter_message("utter_some_severe_symptom")
		# elif severe_symptom_1 is True and severe_symptom_2 is False and severe_symptom_3 is False and severe_symptom_4 is False:
		# 	dispatcher.utter_message("utter_one_severe_symptom")
		# elif severe_symptom_1 is False and severe_symptom_2 is False and severe_symptom_3 is False and severe_symptom_4 is False:
		# 	dispatcher.utter_message("utter_no_severe_symptoms")

		# return []		

# ----------------------------------------------------------------------------------------------------------------------------------------

# class ActionHospitalInfo(Action):

#     def name(self) -> Text:
#         return "action_hospital_info"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         mydb = mysql.connector.connect(host="localhost",user="root",password="12345",database="products")
#         mycursor = mydb.cursor()
#         location = tracker.get_slot("location")
#         mycursor.execute("select name,city,phone from hospitals.hospital_info where city = '"+location+"'")
#         results = mycursor.fetchone()
#         dispatcher.utter_message(text=str(results[0])+" " + str(results[1]))

#         return []

# ----------------------------------------------------------------------------------------------------------------------------------------

# class SymptomsForm (FormAction):

# 	def name (self) -> Text:

# 		return "symptoms_form"

# 	@staticmethod
# 	def required_slots(tracker: Tracker) -> List[Text]:

# 		return ["severe_symptom_one"]
# # , "severe_symptom_two", "severe_symptom_three", "severe_symptom_four"
# 	def slot_mappings(self):

# 		return{
# 			"severe_symptom_one": [
# 		            self.from_intent(intent="affirm", value=True),
# 		            self.from_intent(intent="deny", value=False),
		        # ]
	# 	    "severe_symptom_2": [
	# 	            self.from_entity(entity="severe_symptom_two"),
	# 	            self.from_intent(intent="affirm", value=True),
	# 	            self.from_intent(intent="deny", value=False),
	# 	        ],
	# 	    "severe_symptom_3": [
	# 	            self.from_entity(entity="severe_symptom_three"),
	# 	            self.from_intent(intent="affirm", value=True),
	# 	            self.from_intent(intent="deny", value=False),
	# 	        ],
	# 	    "severe_symptom_4": [
	# 	            self.from_entity(entity="severe_symptom_four"),
	# 	            self.from_intent(intent="affirm", value=True),
	# 	            self.from_intent(intent="deny", value=False),
	# 	        ]  
		# }

# 	def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:

#         dispatcher.utter_message(template="utter_submit")
#         return []