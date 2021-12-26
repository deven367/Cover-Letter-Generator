from bs4 import BeautifulSoup as bsp
import requests
import re
# from clean_plot import rm_useless_spaces
from fastai.text.core import rm_useless_spaces
from fastcore.foundation import L
import unidecode

if __name__ == "__main__":
    # url = input("Enter job url: ")
    url = 'https://www.linkedin.com/jobs/view/2850269027/?alternateChannel=search&refId=P8bd%2Bd0gNV%2B2qAm0LL49Yw%3D%3D&trackingId=L5oS6e0LALiYn0E7e6jFDg%3D%3D'
    response = requests.get(url)
    print(response)
    soup = bsp(response.text, "html.parser")
    # print(soup.prettify())

    out = []
    for div in soup.find_all('li',limit = 20):

        # some text cleaning to remove \n and whitespaces
        raw = div.get_text()
        all_cleaned = raw.replace('\n', ' ')
        all_cleaned = rm_useless_spaces(all_cleaned)
        all_cleaned = all_cleaned.strip()
        all_cleaned = unidecode.unidecode(all_cleaned)

        # final check to based on length of the string
        if len(all_cleaned) > 2:
            # clean_text =
            print(all_cleaned)
            out.append(all_cleaned)
            # break
    # print(len(out))


    ## Output from the scapper, looks like this
    """
    <Response [200]>
    Jobs
    People
    Learning
    Report this job
    Build state of the art machine learning models using data mining, big data, deep learning, content understanding, language understanding, and more.
    Maintain and optimize machine learning platform, identify new ideas to evolve it, develop new features and benchmark possible solutions
    Build machine learning capabilities using technologies such as REST web services, micro-services, Caffe, Tensorflow, Spark, Elastic, AWS, Kafka, Deep Learning, Matlab, R, and more
    MS or PhD in Computer Science, Data Science or related degree
    Relevant experience with some machine learning frameworks - Scikit, MLPack, TF, SparkMLib, Caffe, etc
    Familiar with Java, Python, and/or C++
    Modeling and Distributed Systems experience
    Knowledge of Big Data processing, REST APIs, AWS, and Microservices
    Experience with open source libraries such as Sklearn, Tensorflow, and PyTorch
    Relevant internship or academic experience with machine learning and/or deep learning methods
    Past internship experience a plus
    Seniority level Internship
    Employment type Full-time
    Job function Engineering and Information Technology
    """

    ## this output then goes in the hf text generation pipline
    # from transformers import pipeline, set_seed
    # generator = pipeline('text-generation', model='gpt2')
    # set_seed(42)
    # generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5)
