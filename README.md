# Data generator
**Data generator** used for create csv files. User can specify number of columns and rows, type of data, headers name, etc...
## setup
>go to data_generator directory
```
$ cd <path to data_generator directory>
```
>activate virtual environment
```
$ source venv/bin/activate
```
>run `main.py` file 
```
(venv)$ python main.py
```
## data type
***COMMON***
```
[id] - unique number
[number,100,1000] - random number /ex. from 100 to 1000/
[string,10,20] - random string /ex. 10 to 20 characters/
[float,2,5] - random float number /min, max/
[word] - random word
[sentence,3] - random sentence with 3 words
[color] - random color /ex. yellow/
[timestamp,2015-01-01,2018-01-01] - random timestamp between /ex. 2003-12-18 16:35:17/
[date,2015-01-01,2018-01-01] - random date between /ex. 2003-12-18/
[time] - random time
[bool] - random boolean /True or False/
[special_char,5] - random set of special characters /number/
[food_group] - random group of food /ex. vegetables/
```
***PERSON***
```
[gender] - /male or female/
[name] - random first name and last name as one string /ex. Michelle Gibson/
[fname_male] - random first male name
[fname_female] - random first female name
[fname] - random first name /male or female
[lname] - random last name
[email] - random e-mail address /ex. address@gmail.com/
[job] - random job
[credit_card] - random credit card provider
[card_number] - random credit card number /ex 4459660909206004 /
[ssn] - random ssn number
[url] - random URL
[education] - random education /ex. Bachelors degree/
```
 ***ADDRESS*** 
 ```
 [country] - random country 
 [state] - random state 
 [city] - random city 
 [zipcode] - random zipcode
 [street] - random street address /ex. 52555 Pamela Rue Apt. 160/
 ```
## output
File `output.csv` is created in  `data_generator` directory
