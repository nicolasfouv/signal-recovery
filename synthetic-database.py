# LIBRARIES
import pandas as pd
import numpy as np
import random as rnd

# GENERATING AND FORMATTING THE DATA WITH PILE-UP (for .csv file)
n_signals = 10000
n_samples = 7

rand_num = np.random.uniform(0.0, 1000.0, n_signals * n_samples)

pulses = []
pileUp = []
pattern = [0, 0, 0, 0, 0.0172, 0.4524, 1, 0.5633, 0.1493, 0.0424, 0, 0, 0]
pulse_loc = 0
for i in range(0, n_signals * n_samples):
    aux = []
    for j in range(0, n_samples):
        aux.append(rand_num[i] * pattern[6 + j - pulse_loc])
    pulses.append(aux)
    pulse_loc += 1

    if pulse_loc//n_samples != 0:
        aux_pileUp = []
        for j in range(0, n_samples):
            aux_sum = 0
            for k in range(0, n_samples):
                aux_sum += pulses[i - k][j]
            aux_pileUp.append(aux_sum)
        pileUp.append(aux_pileUp)
        pulse_loc = 0

aux_db = []
db = []
pulse_loc = 0
pileUp_count = 0
for i in range(0, len(pulses)):
    db.append({'Amplitude': rand_num[i], 'pulse(1)': pulses[i][0], 'pulse(2)': pulses[i][1], 'pulse(3)': pulses[i][2],
               'pulse(4)': pulses[i][3], 'pulse(5)': pulses[i][4], 'pulse(6)': pulses[i][5], 'pulse(7)': pulses[i][6]})
    pulse_loc += 1

    if pulse_loc//n_samples != 0:
        db.append({'Amplitude': f'pileUp_{pileUp_count + 1}', 'pulse(1)': pileUp[pileUp_count][0] + rnd.gauss(0, 1),
                   'pulse(2)': pileUp[pileUp_count][1] + rnd.gauss(0, 1), 'pulse(3)': pileUp[pileUp_count][2] + rnd.gauss(0, 1),
                   'pulse(4)': pileUp[pileUp_count][3] + rnd.gauss(0, 1), 'pulse(5)': pileUp[pileUp_count][4] + rnd.gauss(0, 1),
                   'pulse(6)': pileUp[pileUp_count][5] + rnd.gauss(0, 1), 'pulse(7)': pileUp[pileUp_count][6] + rnd.gauss(0, 1)})
        pileUp_count += 1
        pulse_loc = 0

database = pd.DataFrame(db)
database.to_csv('./database/db_name.csv')