#picker for names
#flags for names
#random pick
#Define names, have flags, 

import random as rand

def picks(name,gifter):
	while len(name)>0:
		picknum=rand.randint(0,len(name))
		picked = name[picknum]
		print picked
		if picked not in gifter:
			gifter.append(picked)
			name.remove(picked)
		else:
			next


names = ['Foo','Bar','Spam']
gifts = []

print picks(names,gifts)
#for q, a in zip(names, gifts):
#	print('{0} has {1} for presents.'.format(q, a))