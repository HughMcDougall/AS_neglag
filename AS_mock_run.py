'''
Slurm-friendly batch job to fit multilag model

HM 25/6
'''

import litmus.fitting_methods
from neglag_model import model_twolag
from load_lcs import *
import pickle

test_names = lc_names
tests = [lc1_2, lc32801_8, lc33_2, lc348_2, lc363_2, lc38_2, lc5_5, lc898_8, lc9390_8]

import argparse

parser = argparse.ArgumentParser(description="Parse a single integer input.")
parser.add_argument("i", type=int, help="An integer input")
args = parser.parse_args()
i = args.i

print("Running job %i", flush=True)

name = lc_names[i]
lc_1, lc_2, true_params= tests[i]

print("Job name %s" %name, flush=True)

model = model_twolag()


fitter = litmus.fitting_methods.nested_sampling(model,
                                                num_live_points=(model.dim()+1)*4*10,
                                                verbose=10,
                                                warn=10,
                                                debug=10,
						num_parallel_samplers = 4,
                                                )

data = model.lc_to_data(lc_1, lc_2)

print("Starting fit", flush=True)
fitter.fit(lc_1, lc_2)


print("Doing analysis", flush=True)
lt = litmus.LITMUS(fitter)
lt.plot_parameters(truth=true_params, dir = "./out_figs/%s.png" %name)
lt.save_chain("./out_chains/%s.csv" %name)

print("Saving pickle", flush=True)
pkl_file = open('./out_pickles/%s.pkl' %name, 'wb')
pickle.dump(fitter, output)
pkl_file.close()


print("Done. Closing", flush=True)
