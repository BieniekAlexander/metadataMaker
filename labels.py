# %% Collect subjects, map subjects to categories
import json

paperSubjects = json.load(open('paperSubjects.json', 'r'))
paperCategories = ["Physics", 'Mathematics', 'Computer Science',
                   'Quantitative Biology', 'Quantitative Finance', 'Statistics',
                   'Electrical Engineering and Systems Science', 'Economics']

subjectCategoryDict = {}
for subject in paperSubjects:
    if subject.startswith('astro') or subject.startswith('cond') or \
     subject.startswith('gr-qc') or subject.startswith('hep') or subject.startswith('nlin') or \
     subject.startswith('nucl') or subject.startswith('physics') or subject.startswith('quant-ph'):
        subjectCategoryDict[subject] = 'Physics'
    if subject.startswith('math'):
        subjectCategoryDict[subject] = 'Mathematics'
    if subject.startswith('cs'):
        subjectCategoryDict[subject] = 'Computer Science'
    if subject.startswith('q-bio'):
        subjectCategoryDict[subject] = 'Quantitative Biology'
    if subject.startswith('q-fin'):
        subjectCategoryDict[subject] = 'Quantitative Finance'
    if subject.startswith('stat'):
        subjectCategoryDict[subject] = 'Statistics'
    if subject.startswith('eess'):
        subjectCategoryDict[subject] = 'Electrical Engineering and Systems Science'
    if subject.startswith('econ'):
        subjectCategoryDict[subject] = 'Economics'





