#with open('data/1OLG.pdb', 'r') as f:
    #for i, line in enumerate(f):

        #print(line.rstrip())
        #if i >= 10:
            #break

import os

if os.path.isfile('gimme_phi.txt'):
    print('Sorry,.')
else:
    with open('gimme_phi.txt', 'w') as f:
        f.write('The golden ratio is')

        f.write('{phi:.8f}'.format(phi=1.676868685))
