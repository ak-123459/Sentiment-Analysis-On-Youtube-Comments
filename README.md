
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
7. [Limitations](#Limitations)
8. [Conclusion](#Conclusion)
9. [Contributors](#Contributors)
10. [Faq](#Faq)

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
16) `transformers`
  
</div>




***
<div align= "start">
 
&nbsp; &nbsp; <a href="https://imgbb.com/"><img src="https://i.ibb.co/5hBTLK6/rocket.png" alt="rocket" width="50" border="0"></a>

</div>

- ## **Installation**


#### python installation for web scraping -:

In the very first step we need to install  [python](https://www.python.org/downloads/release/python-31011/) script that will extract the data from from Youtube websites.in the very first step you need to download python 3.10.11 you can download from this link like :- [python](https://www.python.org/downloads/release/python-31011/)

- ensure python installed on your system by running these following commands:-
  #### open command prompt in your system and run

  - python


#### creating virtual environment:-

`python -m venv venv`
`source venv/bin/activate`     # On Linux/Mac
`venv\Scripts\activate `       # On Windows


  #### Manually python package installations for jupyter notebook/pycharm -:
  
  `pip install ---`

#### install packages using requirements.txt:-

`pip install --upgrade -r requirements.txt`



  #### playwright  chromium  browser installations for jupyter notebook/pycharm -:

 `playwright install chromium`

**Note:-** - 1) first you need to install playwright and after chromium.
       

<div align= "start">
  
#### run script using git-:

- you need to download git in your system:-
- [how to install github](https://www.techrepublic.com/article/how-to-install-github-desktop/)
  
`git clone https://github.com/ak-123459/Sentiment-Analysis-On-Youtube-Comments.git`

`cd https://github.com/ak-123459/Sentiment-Analysis-On-Youtube-Comments/`

`python main.py`


</div>






***
<div align= "start">
 
&nbsp; &nbsp; <a href="https://imgbb.com/"><img src="https://i.ibb.co/DDYn9zS/icons8-structure-48.png" width="50" alt="icons8-structure-48" border="0"></a><br /><a target='_blank' href='https://imgbb.com/'></a><br />
</div>



<div align= "start">
  
 - ## **Project Structure**


- **Main/**

  - `main.py`: main python file.
  - `Youtube_Scraping.py`
    
- **Main/Sentiment analysis notebooks.zip/**
  
  - `Classical_Sentiment_analysis.ipynb`: notebook contains code for sentiment analysis using a classical methods. .
  - `sentimet_analysis_LLM.ipynb`: notebook contains code for sentiment analysis using a large language models.
 
    
- **Main/**
  - `requirement.txt`: software requirements.

  
   </div>




  
***
<div align= "start">

&nbsp; &nbsp; <a href="https://imgbb.com/"><img src="https://i.ibb.co/SyNZJd3/icons8-skills-64.png" width="50" alt="icons8-skills-64" border="0"></a>

</div>


<div align= "start">

- ### **Methodology**


- steps for sentiment analysis.

  **Data collection-**:- after running the  main.py script using python data will be collect in .csv format in the Data Extraction folder.

  ***Classical_sentiment_analysis_approach-***
  
  **Data loading-**:- specify the extracted comments data path in classical sentiment analysis approach.

  **Data transformations-** data cleaning, created new columns,remove stop words by stopwords.json data.

  **sentiment analysis-** using prebuilt textblob library calculate [postitive negative subjectivity score](https://stackabuse.com/sentiment-analysis-in-python-with-textblob/) etc.

  **visualizations-** 
  



   ***LLM_sentiment_analysis_approach-***
  
  **Data loading-**:- specify the extracted comments data path in llm sentiment analysis approach.

  **Data transformations-** data cleaning, created new columns,remove stop words by stopwords.json data.

  **sentiment analysis-** using pretrained [LLM](https://www.geeksforgeeks.org/large-language-model-llm/) [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) model downloaded from [huggingface](https://www.geeksforgeeks.org/hugging-face-transformers/) open source models library etc.

  **Keyword/entity extraction-**- trump/biden to classify each comments sentiment score.

  **Descriptive analysis-** calculate the median postive,median negative score.
  


</div>


***
<div align= "start">

&nbsp; &nbsp; <a href="https://imgbb.com/"><img src="https://i.ibb.co/nsvy86z/warning.png" alt="warning" width ="50" border="0"></a>

</div>



<div align= "start">

- ### **Limitations**

- master in playwright and beautiful soup library is require.
- gpu needs to use llm for predictions.
- speed will be slow for llm sentiment analysis compare to textblob because of alot of computations.
- basics knowledge require about [LLM(large laguage model)](https://www.geeksforgeeks.org/large-language-model-llm/)



</div>








  
***
<div align= "start">

&nbsp; &nbsp; <a href="https://imgbb.com/"><img src="https://i.ibb.co/wMD5NBc/conclusion.png" width="50" alt="conclusion" border="0"></a>

</div>



<div align= "start">



- ### **Conclusion**

- playwright and beautifulsoup both are very good for fast web scraping.
- llm are better compare to classical sentiment analysis method.
- llm have contextual result for text analysis because they was trained on large amount of text data.
  




</div>










***

<div align= "start">


 &nbsp; &nbsp; <a href="https://imgbb.com/"><img src="https://i.ibb.co/wJ6kKqM/problem-solving.png" alt="problem-solving" width="50" border="0"></a><br /><a target='_blank' href='https://imgbb.com/'></a><br />
 
</div>


<div align= "start">

 - ## **Contributors** 
 [**Akash Prasad Mishra**](https://github.com/ak-123459)
   

</div>




***


<div align= "start">

&nbsp; &nbsp; <a href="https://imgbb.com/"><img src="https://i.ibb.co/mS6MjVT/faq.png" width="50" alt="faq" border="0"></a>

</div>



<div align= "start">

- ### **Faq**





</div>










