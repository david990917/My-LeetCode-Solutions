# -*- coding:utf-8 -*-
import os
path='./'
files=os.listdir(path)

fb=open('basic.md', 'r')
f=open('index.md','w')
for line in fb.readlines():
	f.write(line)




lc_easy=[]
lc_medium=[]
lc_hard=[]
lc_offer=[]
lc_contest=[]
for file in files:
	if os.path.isfile(file):
		file,ext=os.path.splitext(file)
		# print(type(file))
		# print(file)
		if file.startswith('easy'):
			file=int(file[5:])
			lc_easy.append(file)
		elif file.startswith('medium'):
			file=int(file[7:])
			lc_medium.append(file)
		elif file.startswith('hard'):
			file=int(file[5:])
			lc_hard.append(file)
		elif file.startswith('offer'):
			file=int(file[6:])
			lc_offer.append(file)
		elif file.startswith('contest'):
			file=int(file[8:])
			lc_contest.append(file)


lc_easy.sort()
print("easy: ",lc_easy,end='\n\n')

lc_medium.sort()
print("medium: ",lc_medium,end='\n\n')

lc_hard.sort()
print("hard: ", lc_hard,end='\n\n')

lc_offer.sort()
print("offer: ",lc_offer,end='\n\n')

lc_contest.sort()
print("contest: ",lc_contest)

f.write('# Easy\n')
f.write('*{} easy problems are recorded here.*\n'.format(len(lc_easy)))
easy_count=0	
for url in lc_easy:
	url='easy-'+str(url)
	f.write('[{}]({})\t'.format(url,'https://github.com/david990917/My-LeetCode-Solutions/blob/master/leetcode/'+url+'.md'))
	easy_count+=1
	if easy_count%8==0:
		f.write('\n')
f.write('\n\n---\n')

f.write('# Medium\n')
f.write('*{} medium problems are recorded here.*\n'.format(len(lc_medium)))
medium_count=0
for url in lc_medium:
	url='medium-'+str(url)
	f.write('[{}]({})\t'.format(url,'https://github.com/david990917/My-LeetCode-Solutions/blob/master/leetcode/'+url+'.md'))
	medium_count+=1
	if medium_count%5==0:
		f.write('\n')
f.write('\n\n---\n')

f.write('# Hard\n')
f.write('*{} hard problems are recorded here.*\n'.format(len(lc_hard)))
hard_count=0
for url in lc_hard:
	url='hard-'+str(url)
	f.write('[{}]({})\t'.format(url,'https://github.com/david990917/My-LeetCode-Solutions/blob/master/leetcode/'+url+'.md'))
	hard_count+=1
	if hard_count%8==0:
		f.write('\n')
f.write('\n\n---\n')

f.write('# Offer\n')
f.write('*{} offer problems are recorded here.*\n'.format(len(lc_offer)))
offer_count=0
for url in lc_offer:
	url='offer-'+str(url)
	f.write('[{}]({})\t'.format(url,'https://github.com/david990917/My-LeetCode-Solutions/blob/master/leetcode/'+url+'.md'))
	offer_count+=1
	if offer_count%4==0:
		f.write('\n')
f.write('\n\n---\n')

f.write('# Contest\n')
f.write('*{} contest problems are recorded here.*\n'.format(len(lc_contest)))
contest_count=0
for url in lc_contest:
	url='contest-'+str(url)
	f.write('[{}]({})\t'.format(url,'https://github.com/david990917/My-LeetCode-Solutions/blob/master/leetcode/'+url+'.md'))
	contest_count+=1
	if contest_count%4==0:
		f.write('\n')
f.write('\n\n---\n')

f.write('These solutions are also updated on my [Github](https://github.com/david990917/My-LeetCode-Solutions).\n')
f.write('***Stay Foolish, Stay Hungry!***')



#################################################
######       DO IT AGAIN FOR REAMDME       ######
#################################################
fb=open('README_BASE.md', 'r')
f=open('README.md','w')
for line in fb.readlines():
	f.write(line)


f.write('## Easy\n\n')
f.write('*{} easy problems are recorded here.*\n'.format(len(lc_easy)))
easy_count=0	
for url in lc_easy:
	url='easy-'+str(url)
	f.write('[{}]({})\t'.format(url,'https://github.com/david990917/My-LeetCode-Solutions/blob/master/leetcode/'+url+'.md'))
	easy_count+=1
	if easy_count%8==0:
		f.write('\n')
f.write('\n\n---\n')

f.write('## Medium\n\n')
f.write('*{} medium problems are recorded here.*\n'.format(len(lc_medium)))
medium_count=0
for url in lc_medium:
	url='medium-'+str(url)
	f.write('[{}]({})\t'.format(url,'https://github.com/david990917/My-LeetCode-Solutions/blob/master/leetcode/'+url+'.md'))
	medium_count+=1
	if medium_count%5==0:
		f.write('\n')
f.write('\n\n---\n')

f.write('## Hard\n\n')
f.write('*{} hard problems are recorded here.*\n'.format(len(lc_hard)))
hard_count=0
for url in lc_hard:
	url='hard-'+str(url)
	f.write('[{}]({})\t'.format(url,'https://github.com/david990917/My-LeetCode-Solutions/blob/master/leetcode/'+url+'.md'))
	hard_count+=1
	if hard_count%8==0:
		f.write('\n')
f.write('\n\n---\n')

f.write('# Offer\n\n')
f.write('*{} offer problems are recorded here.*\n'.format(len(lc_offer)))
offer_count=0
for url in lc_offer:
	url='offer-'+str(url)
	f.write('[{}]({})\t'.format(url,'https://github.com/david990917/My-LeetCode-Solutions/blob/master/leetcode/'+url+'.md'))
	offer_count+=1
	if offer_count%4==0:
		f.write('\n')
f.write('\n\n---\n')

f.write('# Contest\n\n')
f.write('*{} contest problems are recorded here.*\n'.format(len(lc_contest)))
contest_count=0
for url in lc_contest:
	url='contest-'+str(url)
	f.write('[{}]({})\t'.format(url,'https://github.com/david990917/My-LeetCode-Solutions/blob/master/leetcode/'+url+'.md'))
	contest_count+=1
	if contest_count%4==0:
		f.write('\n')
f.write('\n\n---\n')

f.write('***Stay Foolish, Stay Hungry!***')
f.close()

##### Move to Github #####
import shutil
shutil.copy2('README.md','D:\Starky\Documents\GitHub\My-LeetCode-Solutions')
shutil.copy2('index.md','C:\Hexo\source\leetcode')
##### Move to Github #####