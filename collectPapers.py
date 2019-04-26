# %% Imports
from urllib import request
import json, os, feedparser, math
import numpy as np

from labels import *





# %% Collect Paper Counts, create sampling counts
samplesPerCategory = 2000
url = 'http://export.arxiv.org/api/query?search_query=cat:{0}&max_results=0'

subjectPaperCounts = {k: int(feedparser.parse(url.format(k)).feed.opensearch_totalresults) for k in paperSubjects}
categoryPaperCounts = {k: 0 for k in paperCategories}
for k in paperSubjects:
    categoryPaperCounts[subjectCategoryDict[k]] += subjectPaperCounts[k]

subjectPaperSamples = {k: math.floor(subjectPaperCounts[k] * samplesPerCategory / categoryPaperCounts[subjectCategoryDict[k]])
                       for k in paperSubjects}

categorySampleUnderflows = {k: samplesPerCategory for k in paperCategories}
for k in paperSubjects:
    categorySampleUnderflows[subjectCategoryDict[k]] -= subjectPaperSamples[k]

for subject in paperSubjects:
    category = subjectCategoryDict[subject]
    if categorySampleUnderflows[category] > 0:
            subjectPaperSamples[subject] += 1
            categorySampleUnderflows[category] -= 1




# %% randomly collect papers from API
data = []
url = 'http://export.arxiv.org/api/query?search_query=cat:{0}&max_results=1&start={1}'

for subject in paperSubjects:
    samples = 0
    indices = list(range(subjectPaperCounts[subject])); np.random.shuffle(indices);

    for i in indices:
        paper = feedparser.parse(url.format(subject, i))
        try:
            data.append(
                {'id': paper.entries[0].id,
                 'category': subjectCategoryDict[subject],
                 'subject': subject,
                 'title': paper.entries[0].title,
                 'abstract': paper.entries[0].summary
                }
            )
        except: continue

        samples += 1
        if samples >= subjectPaperSamples[subject]: break

try: os.mkdir('data')
except: pass

json.dump(data, open('data/data.json', 'w+'))
