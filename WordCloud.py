import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import string
import sys
from cv2 import imshow, waitKey


def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)




def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = f'''{string.punctuation}'''
    uninteresting_words = ["the", "a", "to", "if", "is", "in", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when",  "where", "how",  "all", "any", "both", "each", "few", "more"
                            , "some", "such", "no", "nor", "too", "very", "can", "will", "just", "also", "on"]

    non_punc_string = [word.lower() for word in "".join([char for char in file_contents if char not in punctuations]).split()]
    interesting_words = [word for word in non_punc_string if word not in uninteresting_words]
    word_dict_frequency = {word: interesting_words.count(word) for word in interesting_words}

    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_dict_frequency)
    return cloud.to_array()


if __name__ == "__main__":
    # _upload()
    file_loc = r'C:\Users\sskva\Desktop\coursera.txt'
    file_contents = open(file_loc)
    myimage = calculate_frequencies(file_contents)
    imshow("wordcloud", myimage)
    waitKey()

    #plt.imshow(myimage)
    #plt.axis('off')
    #plt.show()