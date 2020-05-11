'''
    format
'''
users = ['ratan tata','mukesh ambani','jack maa','sunder pichai']
computers = ['aurduino','rasberry pi','window','android']
template = 'computer used by {} is {}'

for i in range(0,len(users)):
    print(template.format(users[i],computers[i]))

