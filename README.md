# nobel_prize_data_mining

### Question 1
Implement a function report(), which takes as input the json file loaded as a Python dictionary (which is the default data structure returned by the json.load() method). This function should return a Pandas DataFrame, where you include the years and categories in which a Nobel Prize was awarded and those in which it was not. You are not expected to infer any missing information, you should only include years and categories for which there is an explicit entry in the original dataset. The result should be of the following form (made up values):

![Image of Q1-Example](https://github.com/Tsoikwokwing/nobel_prize_data_mining/blob/master/Q1-Example.png)

Further instructions:
* There is no field called ‘awarded_or_not’ in the dataset, you have to find this information elsewhere. Discuss your solution in the code as comments.
* Years should be represented as integers, categories as strings and awarded_or_not values should be boolean.
* Column names should be ‘year’, ‘category’ and ‘awarded_or_not’.

### Question 2
Write a function get_laureates_and_motivation() which takes as input three arguments: the nobel prize dictionary (same as in Q2.1), year (a string) and category (a string). This function returns a Pandas DataFrame containing one row per laureate (i.e., a person who has won the Nobel prize). The returned DataFrame should be of the form below (made up values):

![Image of Q2-Example](https://github.com/Tsoikwokwing/nobel_prize_data_mining/blob/master/Q2-Example.png)

Further instructions:
* The id values refer to the laureate id as per their identifier in the original dataset.
* Overall motivations are reasons for awarding Nobel prizes which apply to more than one person in the same batch. However, not all laureates have an overall motivation associated. In those cases, you should insert a NaN value in their ‘overall_motivation’ field.
* Categories, laureates and motivation should be strings, years and ids should be integers, and overall_motivation should be either string or NaN.
* Use the column names shown in the sample table above, do not change them.

### Question 3
Write a function plot_freqs() which generates six plots, one for each category. The xaxis should contain the 1st, 10th, 20th, 30th, 40th and 50th most frequent word across the motivation sections for each category. The y-axis should refer to the frequency of each word in that category. The resulting plot should have a similar arrangement as the one below.

![Image of Q3-Example](https://github.com/Tsoikwokwing/nobel_prize_data_mining/blob/master/Q3-Example.png)

Further instructions:
* You should only count the words provided in whitelist.txt, a text file available in learning central, with one word per line. Do not count others.
* Your figures should have a title, legend, the frequency of each word, tick marks, labels in the x axis for each word, be readable (e.g., big enough fonts), etc.
