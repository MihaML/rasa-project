from rasa.nlu.training_data import load_data
from rasa.nlu import config
from rasa.nlu.model import Trainer

data = load_data('./data/nlu.md')
trainer = Trainer(config.load('./config.yml'))

trainer.train(data)

model_directory = trainer.persist('./models')