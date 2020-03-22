# CMT114 Coursework
# student number:C1937813

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
with open('nobelprizes.json','r') as file_object:
    d = json.load(file_object)


def report(nobelprizeDict): #type report(d) to test this function
    # your code here
    # All the people in 'laureates' are awarded nobel prizes. Thus, if the value in 'laureates' is NaN, nobody is awarded in that year.

    nobelprizeDict = pd.DataFrame(d)
    df = nobelprizeDict[['year','category','laureates']]
    df.fillna(False, inplace = True)

    # change the datatype of each value in column 'year' to int
    for i in range(df.shape[0]):
        df.iloc[i,0] = int(df.iloc[i,0])

    # assign each value that is not False in column 'laureates' to True.
    for i in range(df.shape[0]):
        if df.iloc[i,2] != False:
            df.iloc[i,2] = True

    df = df.rename({'laureates':'awarded_or_not'}, axis = 1)
    return df


def get_laureates_and_motivation(nobelprizeDict, year, category): #you should input string in parameters of 'year' and 'category', e.g. '2019', 'chemistry'
                                                                  #type get_laureates_and_motivation(d, '2019', 'chemistry') to test this function
    # your code here
    #

    nobelprizeDict = pd.DataFrame(d)
    res = []
    for i in range(nobelprizeDict.shape[0]):
        if (nobelprizeDict.iloc[i,0] == year) & (nobelprizeDict.iloc[i,1] == category):

            # check if overallMotivation is null
            if pd.isnull(nobelprizeDict.iloc[i,-1]):
                overall_motivation = np.NaN
            else:
                overall_motivation = nobelprizeDict.iloc[i,-1]

            #check if laureates is null
            #if nobelprizeDict['laureates'][i] is np.NaN: #pd.isnull(nobelprizeDict['laureates'][i])
                #return overall_motivation

            if nobelprizeDict['laureates'][i] is not np.NaN:
                laureates = nobelprizeDict['laureates'][i]
                #extract information in laureates.
                for item in laureates:
                    temp = []

                    #check if "firstname" and "surname" are null
                    if "firstname" in item.keys():
                        if "surname" in item.keys():
                            temp.extend([category, int(year), item["id"], item["firstname"] + " " + item["surname"], item["motivation"], overall_motivation])
                        else:
                            temp.extend([category, int(year), item["id"], item["firstname"], item["motivation"], overall_motivation])
                    else:
                        if "surname" in item.keys():
                            temp.extend([category, int(year), item["id"], item["surname"], item["motivation"], overall_motivation])
                        else:
                            temp.extend([category, int(year), item["id"], "", item["motivation"], overall_motivation])
                    res.append(temp)
                df = pd.DataFrame(res, columns = ["category", "year", "id", "laureate", "motivation", "overall_motivation"])
                return df

    #normal example
    #get_laureates_and_motivation(nobelprizeDict, '2019', 'chemistry')

    #example for firstname exist while surname is null
    #get_laureates_and_motivation(nobelprizeDict, '2017', 'peace')

    #example for 'No Nobel Prize was awarded this year'
    #get_laureates_and_motivation(nobelprizeDict, '1972', 'peace')


def plot_freqs(nobelprizeDict): #type plot_freqs(d) to test this function
    # your code here
    #

    nobelprizeDict = pd.DataFrame(d)

    #append each not null content of 'laureates' into a list
    res_chemistry = []
    for i in range(nobelprizeDict.shape[0]):
        if nobelprizeDict.iloc[i,1] == 'chemistry':
            laureates = nobelprizeDict['laureates'][i]
            if laureates is not np.NaN:
                for n in range(len(laureates)):
                    temp = []
                    temp.append(laureates[n]['motivation'])
                    res_chemistry.append(temp)

    res_economics = []
    for i in range(nobelprizeDict.shape[0]):
        if nobelprizeDict.iloc[i,1] == 'economics':
            laureates = nobelprizeDict['laureates'][i]
            if laureates is not np.NaN:
                for n in range(len(laureates)):
                    temp = []
                    temp.append(laureates[n]['motivation'])
                    res_economics.append(temp)

    res_literature = []
    for i in range(nobelprizeDict.shape[0]):
        if nobelprizeDict.iloc[i,1] == 'literature':
            laureates = nobelprizeDict['laureates'][i]
            if laureates is not np.NaN:
                for n in range(len(laureates)):
                    temp = []
                    temp.append(laureates[n]['motivation'])
                    res_literature.append(temp)

    res_peace = []
    for i in range(nobelprizeDict.shape[0]):
        if nobelprizeDict.iloc[i,1] == 'peace':
            laureates = nobelprizeDict['laureates'][i]
            if laureates is not np.NaN:
                for n in range(len(laureates)):
                    temp = []
                    temp.append(laureates[n]['motivation'])
                    res_peace.append(temp)

    res_physics = []
    for i in range(nobelprizeDict.shape[0]):
        if nobelprizeDict.iloc[i,1] == 'physics':
            laureates = nobelprizeDict['laureates'][i]
            if laureates is not np.NaN:
                for n in range(len(laureates)):
                    temp = []
                    temp.append(laureates[n]['motivation'])
                    res_physics.append(temp)

    res_medicine = []
    for i in range(nobelprizeDict.shape[0]):
        if nobelprizeDict.iloc[i,1] == 'medicine':
            laureates = nobelprizeDict['laureates'][i]
            if laureates is not np.NaN:
                for n in range(len(laureates)):
                    temp = []
                    temp.append(laureates[n]['motivation'])
                    res_medicine.append(temp)


    #extract whitelist.txt into a list without "\n"
    keyword_list = []

    with open('whitelist.txt','r') as f:
        for line in f:
            keyword_list.append(line.replace("\n",""))

    #append each sentence of res_chemistry into a list
    chemistry_motivation_templist = []
    for i in range(len(res_chemistry)):
        for string in res_chemistry[i]:
            chemistry_motivation_templist.append(string.replace("\"","").split(" "))

    #append each word of sentences into a list
    chemistry_motivation_words = []
    for each in chemistry_motivation_templist:
        for word in each:
            chemistry_motivation_words.append(word)

    #count the words' frequency in chemistry
    chemistry_keyword_frequency = []
    for word in keyword_list:
        total = 0
        num = chemistry_motivation_words.count(word)
        total += num
        chemistry_keyword_frequency.append(total)

    #test outcomes: chemistry: discovery,30; discoveries,7; concerning,14; work,24; development,42

    #append each sentence of res_economics into a list
    economics_motivation_templist = []
    for i in range(len(res_economics)):
        for string in res_economics[i]:
            economics_motivation_templist.append(string.replace("\"","").split(" "))

    #append each word of sentences into a list
    economics_motivation_words = []
    for each in economics_motivation_templist:
        for word in each:
            economics_motivation_words.append(word)

    #count the words' frequency in economics
    economics_keyword_frequency = []
    for word in keyword_list:
        total = 0
        num = economics_motivation_words.count(word)
        total += num
        economics_keyword_frequency.append(total)

    #test outcomes: economics: discovery,1; discoveries,0; concerning,1; work,6; development,8


    #append each sentence of res_literature into a list
    literature_motivation_templist = []
    for i in range(len(res_literature)):
        for string in res_literature[i]:
            literature_motivation_templist.append(string.replace("\"","").split(" "))

    #append each word of sentences into a list
    literature_motivation_words = []
    for each in literature_motivation_templist:
        for word in each:
            literature_motivation_words.append(word)

    #count the words' frequency in literature
    literature_keyword_frequency = []
    for word in keyword_list:
        total = 0
        num = literature_motivation_words.count(word)
        total += num
        literature_keyword_frequency.append(total)

    #test outcomes: literature: discovery,0; discoveries,0; concerning,0; work,5; development,0


    #append each sentence of res_peace into a list
    peace_motivation_templist = []
    for i in range(len(res_peace)):
        for string in res_peace[i]:
            peace_motivation_templist.append(string.replace("\"","").split(" "))

    #append each word of sentences into a list
    peace_motivation_words = []
    for each in peace_motivation_templist:
        for word in each:
            peace_motivation_words.append(word)

    #count the words' frequency in peace
    peace_keyword_frequency = []
    for word in keyword_list:
        total = 0
        num = peace_motivation_words.count(word)
        total += num
        peace_keyword_frequency.append(total)

    #test outcomes: peace: discovery,0; discoveries,0; concerning,0; work,30; development,3


    #append each sentence of res_physics into a list
    physics_motivation_templist = []
    for i in range(len(res_physics)):
        for string in res_physics[i]:
            physics_motivation_templist.append(string.replace("\"","").split(" "))

    #append each word of sentences into a list
    physics_motivation_words = []
    for each in physics_motivation_templist:
        for word in each:
            physics_motivation_words.append(word)

    #count the words' frequency in physics
    physics_keyword_frequency = []
    for word in keyword_list:
        total = 0
        num = physics_motivation_words.count(word)
        total += num
        physics_keyword_frequency.append(total)

    #test outcomes: physics: discovery,92; discoveries,25; concerning,12; work,20; development,30


    #append each sentence of res_medicine into a list
    medicine_motivation_templist = []
    for i in range(len(res_medicine)):
        for string in res_medicine[i]:
            medicine_motivation_templist.append(string.replace("\"","").split(" "))

    #append each word of sentences into a list
    medicine_motivation_words = []
    for each in medicine_motivation_templist:
        for word in each:
            medicine_motivation_words.append(word)

    #count the words' frequency in medicine
    medicine_keyword_frequency = []
    for word in keyword_list:
        total = 0
        num = medicine_motivation_words.count(word)
        total += num
        medicine_keyword_frequency.append(total)

    #test outcomes: medicine: discovery,69; discoveries,127; concerning,88; work,15; development,14


    #generate df_chemistry for plot

    df_chemistry_kwf = pd.DataFrame({'keyword':keyword_list, 'frequency':chemistry_keyword_frequency})
    df_chemistry_kwf = df_chemistry_kwf.sort_values(by='frequency', ascending=False)
    df_chemistry = pd.concat([df_chemistry_kwf.iloc[0:1,:], df_chemistry_kwf.iloc[9:50:10,:]])


    #generate df_economics for plot

    df_economics_kwf = pd.DataFrame({'keyword':keyword_list, 'frequency':economics_keyword_frequency})
    df_economics_kwf = df_economics_kwf.sort_values(by='frequency', ascending=False)
    df_economics = pd.concat([df_economics_kwf.iloc[0:1,:], df_economics_kwf.iloc[9:50:10,:]])


    #generate df_literature for plot

    df_literature_kwf = pd.DataFrame({'keyword':keyword_list, 'frequency':literature_keyword_frequency})
    df_literature_kwf = df_literature_kwf.sort_values(by='frequency', ascending=False)
    df_literature = pd.concat([df_literature_kwf.iloc[0:1,:], df_literature_kwf.iloc[9:50:10,:]])


    #generate df_peace for plot

    df_peace_kwf = pd.DataFrame({'keyword':keyword_list, 'frequency':peace_keyword_frequency})
    df_peace_kwf = df_peace_kwf.sort_values(by='frequency', ascending=False)
    df_peace = pd.concat([df_peace_kwf.iloc[0:1,:], df_peace_kwf.iloc[9:50:10,:]])


    #generate df_physics for plot

    df_physics_kwf = pd.DataFrame({'keyword':keyword_list, 'frequency':physics_keyword_frequency})
    df_physics_kwf = df_physics_kwf.sort_values(by='frequency', ascending=False)
    df_physics = pd.concat([df_physics_kwf.iloc[0:1,:], df_physics_kwf.iloc[9:50:10,:]])


    #generate df_medicine for plot

    df_medicine_kwf = pd.DataFrame({'keyword':keyword_list, 'frequency':medicine_keyword_frequency})
    df_medicine_kwf = df_medicine_kwf.sort_values(by='frequency', ascending=False)
    df_medicine = pd.concat([df_medicine_kwf.iloc[0:1,:], df_medicine_kwf.iloc[9:50:10,:]])

    #Generate Subplots
    fig = plt.figure(figsize=(18, 9))
    fig.suptitle('The 1st, 10th, 20th, 30th, 40th and 50th most frequent word\nacross the motivation sections', fontsize = 20)

    #chemistry_plot
    fig.add_subplot(231)
    chemistry_plot = plt.scatter(df_chemistry.iloc[:,0], df_chemistry.iloc[:,1], s = 50, c = 'r', marker = 's', label='chemistry')
    plt.xticks(rotation = -45, fontsize=12)
    plt.yticks(range(0,141,20))
    plt.grid(which = 'major', axis = 'y', c='grey', linestyle='--')
    plt.title('chemistry', fontsize=16)
    plt.ylabel('frequency', fontsize=16)
    for a,b in zip(df_chemistry['keyword'], df_chemistry['frequency']):
        plt.text(a, b+5, '%.0f' %b, ha='center', va= 'bottom',fontsize=11)

    #economics_plot
    fig.add_subplot(232)
    economics_plot = plt.scatter(df_economics.iloc[:,0], df_economics.iloc[:,1], s = 50, c = 'b', marker = 'o')
    plt.xticks(rotation = -45, fontsize=12)
    plt.yticks(range(0,141,20))
    plt.grid(which = 'major', axis = 'y', c='grey', linestyle='--')
    plt.title('economics', fontsize=16)
    plt.ylabel('frequency', fontsize=16)
    for a,b in zip(df_economics['keyword'], df_economics['frequency']):
        plt.text(a, b+5, '%.0f' %b, ha='center', va= 'bottom',fontsize=11)

    #literature_plot
    fig.add_subplot(233)
    literature_plot = plt.scatter(df_literature.iloc[:,0], df_literature.iloc[:,1], s = 50, c = 'c', marker = 'x')
    plt.xticks(rotation = -45, fontsize=12)
    plt.yticks(range(0,141,20))
    plt.grid(which = 'major', axis = 'y', c='grey', linestyle='--')
    plt.title('literature', fontsize=16)
    plt.ylabel('frequency', fontsize=16)
    for a,b in zip(df_literature['keyword'], df_literature['frequency']):
        plt.text(a, b+5, '%.0f' %b, ha='center', va= 'bottom',fontsize=11)

    #peace_plot
    fig.add_subplot(234)
    peace_plot = plt.scatter(df_peace.iloc[:,0], df_peace.iloc[:,1], s = 50, c = 'g', marker = 'p')
    plt.xticks(rotation = -45, fontsize=12)
    plt.yticks(range(0,141,20))
    plt.grid(which = 'major', axis = 'y', c='grey', linestyle='--')
    plt.title('peace', fontsize=16)
    plt.ylabel('frequency', fontsize=16)
    for a,b in zip(df_peace['keyword'], df_peace['frequency']):
        plt.text(a, b+5, '%.0f' %b, ha='center', va= 'bottom',fontsize=11)

    #physics_plot
    fig.add_subplot(235)
    physics_plot = plt.scatter(df_physics.iloc[:,0], df_physics.iloc[:,1], s = 150, c = 'y', marker = '*')
    plt.xticks(rotation = -45, fontsize=12)
    plt.yticks(range(0,141,20))
    plt.grid(which = 'major', axis = 'y', c='grey', linestyle='--')
    plt.title('physics', fontsize=16)
    plt.ylabel('frequency', fontsize=16)
    for a,b in zip(df_physics['keyword'], df_physics['frequency']):
        plt.text(a, b+5, '%.0f' %b, ha='center', va= 'bottom',fontsize=11)

    #medicine_plot
    fig.add_subplot(236)
    medicine_plot = plt.scatter(df_medicine.iloc[:,0], df_medicine.iloc[:,1], s = 50, c = 'm', marker = '^')
    plt.xticks(rotation = -45, fontsize=12)
    plt.yticks(range(0,141,20))
    plt.ylim(0,140)
    plt.grid(which = 'major', axis = 'y', c='grey', linestyle='--')
    plt.title('medicine', fontsize=16)
    plt.ylabel('frequency', fontsize=16)
    for a,b in zip(df_medicine['keyword'], df_medicine['frequency']):
        plt.text(a, b+5, '%.0f' %b, ha='center', va= 'bottom',fontsize=11)


    fig.legend(handles = [chemistry_plot,economics_plot,literature_plot,peace_plot,physics_plot,medicine_plot],labels = ['chemistry','economics','literature','peace','physics','medicine'], loc = 'center right', fontsize = 12)
    plt.subplots_adjust(left=0.12, bottom=None, right=0.88, top=0.85, wspace=None, hspace=0.55)

    plt.show()


#Test in Terminal by typing: python Q2.py
print(report(d))
print(get_laureates_and_motivation(d, '2019', 'chemistry'))
plot_freqs(d)
