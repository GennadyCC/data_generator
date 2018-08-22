from faker import Faker
from random import choice
import random as r
import datetime
import radar 
f = Faker()

columnTypeList = []
columnHeaderList = []
delimeter = ','
rowNum = 0
columnNum = 0
fileName = './output.csv'

def data_number(min, max):
    num = f.random_int(min=int(min), max=int(max))
    return num

def data_word():
    fake = f.word(ext_word_list=None)
    return fake

def random_data(num, data_type):
    d = data_type.split(',')
    
    if d[0] == 'id':
        r_data = num + 1
    if d[0] == 'number':
        r_data = f.random_int(min=int(d[1]), max=int(d[2]))
    if d[0] == 'string':
        r_data = f.pystr(min_chars=int(d[1]), max_chars=int(d[2]))
    if d[0] == 'float':
        # r_data = f.pyfloat(left_digits=int(d[1]), right_digits=int(d[2]), positive=str(d[3]))
        r_data = r.uniform(int(d[1]), int(d[2]))
    if d[0] == 'word':
        r_data = f.word(ext_word_list=None)
    if d[0] == 'sentence':
        r_data = f.sentence(nb_words=int(d[1]), variable_nb_words=True, ext_word_list=None)
    if d[0] == 'color':
        r_data = f.safe_color_name()
    if d[0] == 'timestamp':
        r_data = radar.random_datetime(start=str(d[1]), stop=str(d[2]))
    if d[0] == 'date':
        r_data = radar.random_datetime(start=str(d[1]), stop=str(d[2]))
        r_data = str(r_data).split(' ')[0]
    if d[0] == 'time':
        r_data = radar.random_datetime(start='2017-01-01', stop='2018-01-01')
        r_data = str(r_data).split(' ')[1]
    if d[0] == 'bool':
        r_data = str(f.pybool())
    if d[0] == 'special_char':
        spec = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','[',']','}','\\','|',':',';','"',',','<','>','.','?','/','~','`',' ','  ']
        r_data = r.sample(spec, int(d[1]))
        r_data = ''.join(r_data)
    if d[0] == 'food_group':
        food_group = ["breads", "cereals", "rice", "pasta","vegetables","fruit","milk", "yoghurt", "cheese", "meat", "fish", "eggs", "nuts"]
        r_data = r.choice(food_group)
    if d[0] == 'gender':
        gender = ["male", "female"]
        r_data = r.choice(gender)
    if d[0] == 'name':
        r_data = f.name()
    if d[0] == 'fname_male':
        r_data = f.first_name_male()
    if d[0] == 'fname_female':
        r_data = f.first_name_female()
    if d[0] == 'fname':
        r_data = f.first_name()
    if d[0] == 'lname':
        r_data = f.last_name()
    if d[0] == 'email':
        r_data = f.email()
    if d[0] == 'job':
        r_data = f.job()
    if d[0] == 'credit_card':
        r_data = f.credit_card_provider(card_type=None)
    if d[0] == 'card_number':
        r_data = f.credit_card_number(card_type=None)
    if d[0] == 'ssn':
        r_data = f.ssn(taxpayer_identification_number_type="SSN")
    if d[0] == 'url':
        r_data = f.url(schemes=None)
    if d[0] == 'education':
        education = ['High school','Associate degree','Bachelors degree','Masters degree','PhD', "Other"]
        r_data = r.choice(education)
    if d[0] == 'country':
        r_data = f.country()
    if d[0] == 'state':
        r_data = f.state_abbr()
    if d[0] == 'city':
        r_data = f.city()
    if d[0] == 'zipcode':
        r_data = f.zipcode()
    if d[0] == 'street':
        r_data = f.street_address()

    return r_data


def create_row(id, col):
    csv_line = ''
    for i in range(len(col)):
        data_type = col[i].strip()
        data_value = random_data(id, data_type)
        csv_line = csv_line + str(data_value)
        if i != len(col)-1:
            csv_line = csv_line + str(delimeter)
    csv_line = csv_line + '\n'
    return csv_line

def create_header(col):
    csv_line = ''
    for i in range(len(col)):
        data = col[i].strip()
        # data_value = random_data(id, data_type)
        csv_line = csv_line + str(data)
        if i != len(col)-1:
            csv_line = csv_line + str(delimeter)
    csv_line = csv_line + '\n'
    return csv_line

def input_file_name():
    global fileName
    fileName = raw_input('''
=========================================================================================
|Provide Name and Path for output csv file                                              |
|/ex: ./output.csv/ or press Enter -> ./data_test.csv will create                       |
=========================================================================================
>>> : ''')

def input_delimeter():
    global delimeter
    delimeter = str(raw_input('''
=========================================================================================
|Provide delimeter for csv fale                                                         |
|options: [ , ][ ; ][ : ]                                                               |
=========================================================================================
>>> : '''))

def input_row_number():
    global rowNum
    rowNum = int(input('''
=========================================================================================
|Provide Number of Rows                                                                 |
|options: [10] /ex. 10 rows/                                                            |
=========================================================================================
>>> : '''))

def input_column_number():
    global columnNum
    columnNum = int(input('''
=========================================================================================
|Provide number of Columns                                                              |
|options: [5] /ex. 5 columns                                                            |
=========================================================================================
>>> : '''))

def input_column_type(i):
    global columnType
    # for i in range(columnNum):
    columnType = raw_input('''
=========================================================================================
| ***COMMON***                                                                          |
| [id] - unique number                                                                  |
| [number,100,1000] - random number /ex. from 100 to 1000/                              |
| [string,10,20] - random string /ex. 10 to 20 characters/                              |
| [float,2,5] - random float number /min, max/                                          |
| [word] - random word                                                                  |
| [sentence,3] - random sentence with 3 words                                           |
| [color] - random color /ex. yellow/                                                   |
| [timestamp,2015-01-01,2018-01-01] - random timestamp between /ex.2003-12-18 16:35:17/ |
| [date,2015-01-01,2018-01-01] - random date between /ex.2003-12-18/                    |
| [time] - random time                                                                  |
| [bool] - random boolean /True or False/                                               |
| [special_char,5] - random set of special characters /number/                          |
| [food_group] - random group of food /ex. vegetables/                                  |
|                                                                                       |
| ***PERSON***                                                                          |
| [gender] - /male or female/                                                           |
| [name] - random first name and last name as one string /ex. Michelle Gibson/          |  
| [fname_male] - random first male name                                                 |
| [fname_female] - random first female name                                             |
| [fname] - random first name /male or female                                           |
| [lname] - random last name                                                            |
| [email] - random e-mail address /ex. address@gmail.com/                               |
| [job] - random job                                                                    |
| [credit_card] - random credit card provider                                           |
| [card_number] - random credit card number /ex. 4459660909206004 /                     |
| [ssn] - random ssn number                                                             |
| [url] - random URL                                                                    |
| [education] - random education                                                        |
|                                                                                       |
| ***ADDRESS***                                                                         |
| [country] - random country                                                            |
| [state] - random state                                                                |
| [city] - random city                                                                  |
| [zipcode] - random zipcode                                                            |
| [street] - random street address /ex. 52555 Pamela Rue Apt. 160/                      |
|                                                                                       |
|---------------------------------------------------------------------------------------|
   Provide Data Type for column # {}                                                    
=========================================================================================
>>> data type for column #{}: '''.format(i+1, i+1))
        # columnType.strip()
        # columnTypeList.append(columnType)
    # type_list = ['id','number','string','float','word','sentence','color','timestamp','']
    # if columnType in type_list:
    #     return True
    # else:
    #     return False

def input_column_header(i):
    global columnHeaderList
    columnHeaderList.append(raw_input('''
=========================================================================================
|Provide Name (header) for column #{}                                                   |
|/ex: 'first_name' / or enter 'no' if header is not needed                              |
=========================================================================================
>>> header for column #{}: '''.format(i+1, i+1)))


def main():

    # input_file_name()
    input_delimeter()
    input_row_number()
    input_column_number()
    for i in range(columnNum):
        input_column_type(i)
        columnType.strip()
        columnTypeList.append(columnType)
        try:
            if columnHeaderList[0] != 'no':
                input_column_header(i)
        except:
            input_column_header(i)
        finally:
            pass        
    # print(columnHeaderList)


    with open(fileName, 'w') as csv_file:
        if columnHeaderList[0] != 'no':
            line = create_header(columnHeaderList)
            # print(line)
            csv_file.writelines(line)
        for i in range(rowNum):
            line = create_row(i, columnTypeList)
            # print(line)
            csv_file.writelines(line)  
    print('File '+ fileName + ' was created')


#  test
# if __name__ == '__main__':

main()


