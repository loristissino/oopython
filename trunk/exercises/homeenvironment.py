import sys
import time
from datetime import date

name=input('Scrivi il tuo nome: ')
print()

print('Date: %s' % date.today().isoformat())

print('Rapporto per il calcolatore di %s' % name)
print('path: %s' % sys.path)
print('executable: %s' % sys.executable)
print('platform: %s' % sys.platform)
print('version: %s' % sys.version)
