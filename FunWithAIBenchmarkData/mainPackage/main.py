# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

# Name: Ryan Dew, JD Poindexter
# email: dewrm@mail.uc.edu, 
# Assignment Number: 07
# Due Date:  10/22/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: 

# Brief Description of what this module does. 
# Citations:
# Anything else that's relevant: 



from readingLevelPackage.readingLevel import Reading_Level
from utilitiesPackage.utilities import *
from utilitiesPackage.CSV_Utilities import *
from PDFPackage.PDFUtilities import *

if __name__ == "__main__":

    CSV_Processor = MMLU_CSV_Processor("dataPackage/MMLU/data/", ["management_test.csv"])
    questions = CSV_Processor.read_data()
    print(len(questions), "questions read")

 
    myPDF = PDFUtilities()
    myPDF.create_question_PDF("Management Test", "MMLU", questions)
   
    print("The first question:")
    print(questions[0])
    
    text = convert_dictionaries_to_string(questions, ["prompt", "possible answers"])
    #print("\ntext from dictionaries:", text[0:500])

    #0. Append all the prompts into a big string - See utilities.convert_dictionaries_to_string()
    
    
    #1. Perform reading level analysis on the big string and print the results to the console.
    Reading_Level.compute_readability_indices("MMLU", text)

    #2. Process the big string to find the longest word
    # Feel free to uee AI
    longest_word = ""
    for word in text.split():
        if len(word) > len(longest_word):
            longest_word = word

    print('Longest Word = ', longest_word)

    #3. Process the big string to find the most prevalent word
    words = dict()
    for word in text.split(" "):
        try:
            words[word] += 1 # Increment the count for this word. Will fail
        except: # If I get here, the lookup failed
            words[word] = 1
    # When I get here, I have a dictionary of key/values pairs. The key is a words
    # the value is the count of that word in text
    # print(words)
    # I still need to sort the dictionary by values
    # 

    #4. Use the VS debugger: set a breakpoint somewhere to pause the project when a prompt containing the word "PEST" is read from the original CSV file
    




    #5. ********************************* Perform some data visualization on the text. Research Data Vis libraries and apply one ********************************************************************************************************************
import matplotlib.pyplot as plt
from collections import Counter

# Assuming 'words' dictionary is already populated with word frequencies
# Sort the dictionary by frequency (value) in descending order
sorted_words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))

# For simplicity, let's plot the top 10 most frequent words
top_words = dict(list(sorted_words.items())[:10])

# Prepare data for plotting
word_list = list(top_words.keys())
count_list = list(top_words.values())

# Create a bar chart
plt.figure(figsize=(10, 5))
plt.bar(word_list, count_list, color='skyblue')

# Add title and labels
plt.title("Top 10 Most Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")

# Show plot
plt.show()

# **************************************************************************************************************************************************************************


    #6a. Write all the questions and possible answers (without the correct answer) to a text file. Use a CSV format and create a unique identifier field for each question.
    #6b. Write the question identifier (see 6a, above) and the correct answer to another text file. Use a CSV format.
questions_written = write_questions_to_text_files("MMLU", questions)
print(questions_written, "questions written to the file.")
    
"""
    #Reading_Level.test01()

    text = "This is a sentence that we can use to test the reading level computations. "
    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
    for key in reading_level_indices.keys():
        print(key, ":", reading_level_indices[key])
            
    # A test with text at a higher reading level
    text = "Birds, employing a combination of aerodynamic principles and specialized anatomical adaptations, achieve flight through the generation of lift, which counteracts the force of gravity."
    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
    for key in reading_level_indices.keys():
        print(key, ":", reading_level_indices[key])
    """
