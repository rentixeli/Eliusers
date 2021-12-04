Well.. It will generate a wordlist based on the given wordlist.
it will take the first letter\last letter change them mix them scramble to generate some user names to enumerate on the active directory.
well its nice for red team operations and shit idk do whatever u want with it i developed this shit in like 5 min just because i was lazy to manual writing user names and mix them

example:
users.txt has some users for example ill show on 1 user from the list what the output will be(Boris Lorenso)
```bash
python3 eliusers.py -w users.txt
```
the output:
```
borisl
boris.l
boris.lor
borislor
blorenso
b.lorenso
b.lor
borislorenso
boris.lorenso
blor
borl
bor.l
borlor
bor.lor
borlorenso
bor.lorenso
lorensob
lorenso.b
lorenso.bor
lorensobor
lboris
l.boris
l.bor
lorensoboris
lorenso.boris
lbor
lorb
lor.b
lorbor
lor.bor
lorboris
lor.boris
```
