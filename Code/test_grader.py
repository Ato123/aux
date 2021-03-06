# Complete and working test grader
# Verified as of 4/29/2021

import os
import glob


print('MAKE SURE ANSWER FILES ARE UPDATED WITH THE RIGHT ANSWERS!!!')

directory = os.path.dirname(os.path.abspath('test_grader.py'))

print('format for divisions: alg1, geo, alg2, precal, calc, stats')
print('What division is currently being graded?')
div = input()

print('\nClear previous grades for this division? (y/n)')
if input().lower().strip() == 'y':
    for f in glob.glob(directory+'/Graded_Submissions/'+div+'/*'):
        os.remove(f)

ans = open(directory+'/Test_Answers/'+div+'.txt').readline()

print('Grading...')

for f in glob.glob(directory+'/Student_Submissions/'+div+'/*'):
    sub = open(f).readline()
    filename = f[f.rindex('\\')+1:]

    print('grading', filename)

    graded = open(directory+'/Graded_Submissions/'+div+'/'+filename, 'w')

    score = 0
    checked = ''
    wrongs = []
    for i in range(30):
        if sub[i] == ans[i]:
            score += 5
            checked += 'r'
        elif sub[i] == 'x':
            score += 1
            checked += 'b'
        else:
            checked += 'w'
            wrongs.append(i+1)
    graded.write(str(score))
    graded.write('\n'+checked)

    for wrong in wrongs:
        graded.write('\n'+str(wrong))

    print(score)

    graded.close()

print('Done!')
