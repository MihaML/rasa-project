## greet
* greet
  - utter_greet

## goodbye
* goodbye
  - utter_goodbye

## thanks
* thanks
  - utter_thanks

## Covid-19 Symptoms Explanation
* covid_symptoms
  - utter_covid_symptoms

## What is Covid-19
* covid_whatis
  - utter_covid_explain

## Covid-19 safety measures
* covid_protection
  - utter_covid_prevention

## Covid-19 treatment
* treatment
  - utter_covid_treatment

## Symptoms duration
* symptom_duration
  - utter_symptoms_duration

## Available Covid-19 Tests
* covid_tests
  - utter_covid_tests

## why is it called Covid-19
* covid19_name
  - utter_covid_name

## what is a novel coronavirus
* novel_coronavirus
  - utter_novel_coronavirus

## how is it spread
* how_spread
  - utter_how_spread

## bot challenge
* bot_challenge
  - utter_iamabot

## covid check
* covid_check
  - utter_developer_updating

## How many cases + location
* how_many_cases
  - utter_developer_updating

## How many deaths + location
* how_many_deaths
  - utter_developer_updating

## How many recovered + location
* how_many_recovered
  - utter_developer_updating




<!-- ## not UK
* covid_check
  - utter_covid_checker
  - utter_question_1
* deny
  - utter_cant_help_uk

## covid check happy path
* greet
  - utter_greet
* covid_check
  - utter_covid_checker
  - symptoms_form
  - form{"name": "symptoms_form"}
  - form{"name": "null"}

## test 1
* covid_check
  - utter_covid_checker
  - utter_question_1
* affirm
  - symptoms_form
  - form{"name": "symptoms_form"}
  - form{"name": null}
  - slot{"severe_symptom_one": true}
  - action_how_many_symptoms

## test 2
* covid_check
  - utter_covid_checker
  - utter_question_1
* deny
  - symptoms_form
  - form{"name": "symptoms_form"}
  - form{"name": null}
  - slot{"severe_symptom_one": false}
  - action_how_many_symptoms
 -->
<!-- ## deny moderate symptoms + affirm more help
  - utter_no_severe_symptoms
* deny
  - utter_more_help
* affirm
  - utter_how_can_help

## deny moderate symptoms + deny more help
  - utter_no_severe_symptoms
* deny
  - utter_more_help
* deny
  - utter_glad_of_service
 -->

 <!-- ## severe symptoms affirm all
* covid_check
  - utter_covid_checker
  - utter_question_1
* affirm
  - utter_severe_symptom_1
* affirm
  - utter_severe_symptom_2
* affirm
  - utter_severe_symptom_3
* affirm
  - utter_severe_symptom_4
* affirm
  - action_how_many_symptoms

## severe symptoms deny all
* covid_check
  - utter_covid_checker
  - utter_question_1
* affirm
  - utter_severe_symptom_1
* deny
  - utter_severe_symptom_2
* deny
  - utter_severe_symptom_3
* deny
  - utter_severe_symptom_4
* deny
  - action_how_many_symptoms

## severe symptoms affirm one
* covid_check
  - utter_covid_checker
  - utter_question_1
* affirm
  - utter_severe_symptom_1
* affirm
  - utter_severe_symptom_2
* deny
  - utter_severe_symptom_3
* deny
  - utter_severe_symptom_4
* deny
  - action_how_many_symptoms -->