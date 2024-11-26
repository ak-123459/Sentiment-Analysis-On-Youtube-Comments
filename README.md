
<div align="center">

<a href="https://ibb.co/h2brqy0"><img src="https://i.ibb.co/j3mqpTt/1607027171-youtube-5-story.jpg" width="1000" alt="1607027171-youtube-5-story" border="0"> </a> 

</div> 


<br> </br>

The main objective of this project to classify the viewers sentiment(Positive,negative,neutral) from  the youtube comments source and perform analysis on them.In this project we are going to use both  sentiment analysis by classical method approach and llm approach.




***

 <div align= "start">
  
  &nbsp; &nbsp; <a href="https://imgbb.com/"><img src="https://i.ibb.co/Ksw7GWz/list.png" width="50" alt="list" border="0"></a> <div/>

  <div align= "start">

- ## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Prerequisites](#Prerequisites)
4. [Project Structure](#Project-Structure)
5. [Installation](#Installation)
6. [Methodology](#Methodlogy)
7. [Data Visualisation](#Data-Visualisation)
8. [Key Findings](#KeyFindings)
9. [Recommendations](#Recommendations)
10. [Conclusion](#Conclusion)
11. [Contributors](#Contributors)

 <div/>






***


<div align= "start">
 
  &nbsp; &nbsp; <a href="https://imgbb.com/"><img src="https://i.ibb.co/x2mBdn3/file.png"  width="50" alt="file" border="0"></a> <div/>
  
<div align= "start">


 
- ## **Project Overview**
YouTube's user count of 2.49 billion places it second on the list of most-used social media platforms.
Not only youtube there are more social media platforms like facebook,instagram,x(Twitter) etc.
that have billions of users.so these are the source of alot of unstructured data like text ,image and videos.
So in this projects we had worked on text data like comments from youtube video.
We perform [sentiment analysis](https://www.ibm.com/topics/sentiment-analysis) on a youtube video joe biden and donald trump presidential debate video that was broadcast  
live on wall street journal channel this is the video link  [TRUMP VS BIDEN](https://www.youtube.com/watch?v=qqG96G8YdcE) .actually we have used this video comments for example purpose how to perform sentiment analysis on youtube comments.the project aim is simple we need to understand the opinion of public using comments on this presidential debate,we want to know which candidates viewers wants to see the president of USA.In this project first we will classify sentiment using textblob and in the second approach we will use pretrained Large language model(LLM) to predict the sentiment.in overall project we have done alot of  steps from [ETL(extract transform load)](https://www.geeksforgeeks.org/etl-process-in-data-warehouse/) to data analysis.
After the project compilation we will compare the both approach and analyse the result.I found in this project llm performance  are better compare to simple classic classifications method.easy to implement and alot of boiler plate code reduced.
In the llm sentiment analysis we have implemented pattern matching using [regular expression](https://docs.python.org/3/howto/regex.html) and extracting of entity/keyword from the text.
Keyword/entity extraction is crucial for sentiment score analysis on  more specific
Entities.

 <div/>
 
<br></br>





 
***

<div align= "start">
&nbsp; &nbsp; <a href="https://imgbb.com/"><img src="https://i.ibb.co/D9vKsxH/dataset.png" alt="dataset" border="0"  width="50"></a> <div/>
 

  
 <div align= "start">
   
- ## **Dataset**



***Note***:- we have collected data from youtube using web scraping you need to run main.py file in terminal/command line. follow the below instructions for data extractions.

&nbsp; &nbsp; **Dataset Structure -**

 | Column Name       | Data Type | Description                              |
|-------------------|-----------|------------------------------------------|
| `comments`              | String   | comments from each users         
  
  </div>






***
<div align= "start">
 
&nbsp; &nbsp; <a href="https://imgbb.com/"><img src="https://i.ibb.co/9TTK8Gc/icons8-requirements-64.png" width="50" alt="icons8-requirements-64" border="0"></a>

</div>



<div align= "start">
  
 - ## **Prerequisites**
   

### Technical skills

- `web scraping`
- `descriptive statatics`
- `Data visualization`
- `Statatics`
- `ETL(Extract transform load)`
- `command prompt (windows)`
- `github`



### Resource Prerequisites:-

1) `playwright`
2) `beautiful soup`
4) `python 3.10.11 =>`
5) `pycharm IDE or google colab`
6) `pandas`
7) `numpy`
8  `windows/ios 64 bit minimum 8gb ram`
9) `google colab`
11) `LLm(large language model)`
12) `textblob`
13) `matplotlib`
14) `seaborn`
15) `spacy`

  
</div>




***
<div align= "start">
 
&nbsp; &nbsp; <a href="https://imgbb.com/"><img src="🚀" width="50" alt="icons8-requirements-64" border="0"></a>

</div>

- ## **Installation**


### python installation for web scraping -:

In the very first step we need to install  [python](https://www.python.org/downloads/release/python-31011/) script that will extract the data from from Youtube websites.in the very first step you need to download python 3.10.11 you can download from this link like :- [python](https://www.python.org/downloads/release/python-31011/)

- ensure python installed on your system by running these following commands:-
  #### open command prompt in your system and run

  - python

<div align= "start">
  
### run script using git-:

- you need to download git in your system:-
- [how to install github](https://www.techrepublic.com/article/how-to-install-github-desktop/)
  
`git clone https://github.com/ak-123459/Sentiment-Analysis-On-Youtube-Comments.git`

`cd https://github.com/ak-123459/Sentiment-Analysis-On-Youtube-Comments/Data Extractions`

`python main.py`


</div>








