import os
import gettext

popath = os.path.join(os.path.dirname(__file__), 'p1')
translation = gettext.translation("p1", popath, fallback=True)
_, ngettext = translation.gettext, translation.ngettext

while s := input():
    print(ngettext('{} word entered', '{} words entered', len(s.split())).format(len(s.split())))
