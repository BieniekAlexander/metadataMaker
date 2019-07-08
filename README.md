# metadataMaker
## Introduction

In this project, we explore the topic of classifying papers according to categories with a paper's abstract as input. Originally, we seeked to generate metadata, such as keyphrases, from the abstract of an article, but we found paper classification alone to be nontrivial. With that, we explore different architectures using various text representations and compare performances within the space of academic literature abstracts.

---

## Workspace

Our work is publically available in our Google Drive workspace, linked below. One can access our notebooks and run them. Please note that our tests make use of GPUs and assume [CUDA](https://developer.nvidia.com/cuda-downloads) is installed in one's workspace.

[Google Drive Workspace](https://drive.google.com/open?id=1B_YdLzaOxdMvOt4npWr9k-T8b3WJtgbc)

Some of the notebooks contain experiments of the experiments, and thus are largely irrelevant for outsiders. The major notebooks pertaining experiments with LSTM/RNNs architectures are
 - [RNN_IntermediateResultsExploration](./RNN_IntermediateResultsExploration.ipynb) was the main file used to generate the results for the intermediate report
 - [RNN_longExperiment](./RNN_longExperiment.ipynb) is the file that contains that longest experiments which feed _whole_ abstracts into an LSTM network
 - [TwitterExperiment](./TwitterExperiment.ipynb) is the file with dozens of experiments in search of hyperparameters & abstract lengths that allow an LSTM network to produce promising results
 
The main notebooks pertaining experiments with CNN architectures are
 - [finalCNNexperiment](./finalCNNexperiment.ipynb) has the majority of the experiments with CNN networks and includes the best-performing model for input sizes of $140$ characters
 - [CNN_shortenAbstracts](./CNN_shortenAbstracts.ipynb) contains the study of performance VS input length where we see how the best model of the `finalCNNexperiment` file behaves as we reduce/increase the input size, from 50 characters all the way up to 270
 - [CNN_dropEcon](./CNN_dropEcon.ipynb) contains the experiments when we dropped the category of "Economics" from our dataset, in order to remove the most under-represented category
 - [CNN_MaPhCS](./CNN_MaPhCS.ipynb) is the notebook containing the experiments where we only used the three biggest categories available: Mathematics, Physics and Computer Science
 
The [word2vec_lstm](./word2vec_lstm.ipynb) notebook used a pretrained word2vec from Google in conjunction with an LSTM architecture to create an experiment with word embeddings, as opposed to the character encodings we used everywhere else.
 
The `.py` and `.json` files were used to scrape [arxiv](arxiv.org) for our dataset of more than 550.000 papers.
