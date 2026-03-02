# הגדרת משתנים.
SS = 0.0036 #(p^2)
num_gen = 500
q_S = SS ** 0.5

# פתיחת קובץ.
sickle_cell_freq = open('results/csv.Sickle_cell_freq_het', 'w')

sickle_cell_freq.write("Generation\tFreq_S\tFreq_SS\tFreq_AS\tFreq_AA\n")

# הגדרת לולאה שבה התוכנית מחשבת את תדירות הגנוטיפים והאללים החדשה עבור כל דור.
for i in range(1, num_gen+1):
    
    p_A = 1 - q_S
    AS = 2*p_A*q_S
    AA = p_A**2
    SS = q_S**2

    # חישוב שכיחות האלל HbS בדור הבא
    q_S = q_S / (0.98*p_A + 2*q_S)

    sickle_cell_freq.write(f"{i}\t{round(q_S,5)}\t{round(SS,5)}\t{round(AS,5)}\t{round(AA,5)}\n")

sickle_cell_freq.close()
    