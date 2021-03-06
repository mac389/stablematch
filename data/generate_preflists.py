#!/usr/bin/python

'''
Generates set of preference lists for Irving hospital-resident matching algorithm
Author: Vishnu Ravi

Output:
- Line 1: N, M, positive integers, numbers of residents and hospitals respectively
- Lines 2..N+1: the resident preference lists, each has form X : A B C ...
- Lines N+2..M+N+1: the hospital preference lists, each has form X : P : A B C ...
- Residents and hospitals are represented as [resident_prefix]1...[resident_prefix]N, [hospital_prefix]1...[hospital_prefix]M

'''

import random

#configure the data set
total_residents = 100
total_hospitals = 100
resident_rol_len = 10 #average length of resident preference list
resident_rol_sd = 3 #standard deviation of resident preference list 
hospital_num_positions = 6 #average number of positions per hospital
hospital_num_positions_sd = 2 #standard deviation of positions per hospital
hospital_prefix = 'H'
resident_prefix = 'R'
output_file = 'data.txt'


output = '' 
residentListOutput = ''
hospitalListOutput = ''

#pref lists
resident_prefs = [[] for _ in xrange(total_residents)]
hospital_prefs = [[] for _ in xrange(total_hospitals)]


#residents 'apply' to hospitals
for this_resident in xrange(total_residents):
		hospitals_randomized = list(range(total_hospitals))
		random.shuffle(hospitals_randomized)
		this_resident_rol_len = int(random.normalvariate(resident_rol_len, resident_rol_sd))
		for n in xrange(this_resident_rol_len):
			resident_prefs[this_resident].append(hospitals_randomized.pop())

		residentListOutput += resident_prefix + str(this_resident+1) + " :"
		for rank in xrange(len(resident_prefs[this_resident])):
			residentListOutput += " " + hospital_prefix  + str(resident_prefs[this_resident][rank]+1)
		residentListOutput += '\n'

#hospitals rank residents that have 'applied'
for this_hospital in xrange(total_hospitals):
		for resident in resident_prefs:
			if this_hospital in resident:
				hospital_prefs[this_hospital].append(resident_prefs.index(resident))


		this_hospital_num_positions = int(random.normalvariate(hospital_num_positions, hospital_num_positions_sd))
		hospitalListOutput += hospital_prefix + str(this_hospital+1) + " : " + str(this_hospital_num_positions) + " :"
		this_hospital_num_ranks = len(hospital_prefs[this_hospital])
		for rank in xrange(this_hospital_num_ranks):
			hospitalListOutput += " " + resident_prefix + str(hospital_prefs[this_hospital][rank]+1)
		hospitalListOutput += '\n'


#print output
output += str(total_residents) + " " + str(total_hospitals) + "\n" + residentListOutput + hospitalListOutput
print output

#write output to a file
datafile = open(output_file, "w")
datafile.write(output)
datafile.close()



