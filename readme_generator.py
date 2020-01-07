import os
import functools


def get_folder_names(path):
    folders = []
    for item in os.listdir(path):
        if not os.path.isfile(item) and item not in ('.git', '.idea'):
            folders.append(item)
    return folders


def get_file_names(path):
    files = os.listdir(path)
    return sorted(files)


def get_filename_url_score(path):
    inFile = open(path, 'r', encoding='utf-8')
    name = inFile.readline().split()[2:]
    url = inFile.readline().split()[-1]
    score = inFile.readline().split()[-1]
    inFile.close()
    return name, url, score


def get_total_num_problems():
    totalNumber = 0
    folders = get_folder_names(os.getcwd())
    for folder in folders:
        subfolders = get_folder_names(os.path.join(os.getcwd(), folder))
        for subfolder in subfolders:
            totalNumber += len(get_file_names(os.path.join(os.getcwd(), folder, subfolder)))
    return totalNumber


readmeFile = open('README.md', 'w', encoding='utf-8')

print('<p align="center"><a href="https://www.hackerrank.com/htrul18"><img src="https://i0.wp.com/gradsingames.com/wp-content/uploads/2016/05/856771_668224053197841_1943699009_o.png" width="400"></a></p>', file=readmeFile)
print(file=readmeFile)
print('# Solutions to Hackerrank problems', file=readmeFile)
print('This repository contains ' + str(get_total_num_problems()) + ' solutions to Hackerrank problems with Python 3 and MySQL.', file=readmeFile)
print(file=readmeFile)
print('Inspired by [Alexander Marinskiy](https://github.com/marinskiy) and his repository [HackerankPractice](https://github.com/marinskiy/HackerrankPractice), I decided to document my HackerRank journey in this repository.', file=readmeFile)
print(file=readmeFile)
print("In addition, this README file was automatically generated using [readme_generator.py](https://github.com/itroulli/HackerRank/blob/master/readme_generator.py) which is a modification of Alexander's [Automated readme generation.py](https://github.com/marinskiy/HackerrankPractice/blob/master/Automated%20readme%20generation.py).", file=readmeFile)
print(file=readmeFile)
print('[![GitHub last commit](https://img.shields.io/github/last-commit/itroulli/HackerRank.svg)](https://github.com/itroulli/HackerRank) ', file=readmeFile)
print('[![GitHub commit activity the past month](https://img.shields.io/github/commit-activity/m/itroulli/HackerRank.svg)](https://github.com/itroulli/HackerRank)', file=readmeFile)
print(file=readmeFile)
print('Frequently updated as it is work in progress! If you find it helpful please press a star!', file=readmeFile)
print(file=readmeFile)
print('## Table of Contents', file=readmeFile)
print(file=readmeFile)
folders = get_folder_names(os.getcwd())
for folder in folders:
    print('- ### ' + folder.replace('_',' ') + '\n', file=readmeFile)
    subfolders = get_folder_names(os.path.join(os.getcwd(), folder))
    for subfolder in subfolders:
        print('    - **' + subfolder.replace('_',' ') + '**', file=readmeFile)
        files = get_file_names(os.path.join(os.getcwd(), folder, subfolder))
        for file in files:
            name, url, score = get_filename_url_score(os.path.join(os.getcwd(), folder, subfolder, file))
            print('        - ' + ' '.join(name)
                  + ' | [Problem](' + url
                  + ')'
                  + ' | [Solution]'
                  + '(https://github.com/itroulli/HackerRank/blob/master/'
                  + folder.replace(' ', '%20') + '/' + subfolder.replace(' ', '%20') + '/'
                  + file.replace(' ', '%20') + ')'
                  + ' | Score: ' + str(score), file=readmeFile)

readmeFile.close()
