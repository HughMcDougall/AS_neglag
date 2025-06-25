import numpy as np
import glob
import pandas as pd


def load_and_save(targ, outtarg):

    print("Processing from %s to %s" %(targ, outtarg))
        

    f = open(targ,'r')

    N1 = -1
    N2 = -1
    params = None

    keys = ['tau','b','z','amp','r','lag','lag_two']

    for i, line in enumerate(f):
        if i==0:
            params = line.replace('\n',"").split(' ')
            params = {k:float(p) for k,p in zip(keys, params)}
        elif i==2: N1 = int(line)
        elif N1 is not None and i==N1+3: N2 = int(line)
        else: continue

    T1, Y1, E1 = np.zeros(N1), np.zeros(N1), np.zeros(N1)
    T2, Y2, E2 = np.zeros(N2), np.zeros(N2), np.zeros(N2)

    f.seek(0)
    j = 0
    for i, line in enumerate(f):
        if i>2 and i<N1+2+1:
            T1[j], Y1[j], E1[j] = [float(x) for x in line.replace('\n',"").split(' ')]
            j += 1
    print("\t Assigned %i/%i values for lc 1" %(j,N1))

    f.seek(0)
    j = 0
    for i, line in enumerate(f):
        if i>2+N1+1:
            T2[j], Y2[j], E2[j] = [float(x) for x in line.replace('\n',"").split(' ')]
            j += 1
    print("\t Assigned %i/%i values for lc 2" %(j,N2))

    f.close()


    D1 = np.vstack([T1, Y1, E1]).T
    D2 = np.vstack([T2, Y2, E2]).T
    df = pd.DataFrame.from_dict(params, orient="index")
    
    np.savetxt(outtarg+"_cont.csv", D1, delimiter = ",")
    np.savetxt(outtarg+"_resp.csv", D2, delimiter = ",")
    

targs = glob.glob("*txt")
targs.remove('README.txt')

for targ in targs:
    out_targ = "./out/"+targ.replace(".txt","")
    load_and_save(targ, out_targ)
    
