import codecs
import sadisplay
from app import models

desc = sadisplay.describe([getattr(models, attr) for attr in dir(models)])
with codecs.open('schema_models.dot', 'w', encoding='utf-8') as f:
    f.write(sadisplay.dot(desc))