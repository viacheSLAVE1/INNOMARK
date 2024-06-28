import requests


counter7 = 0
counter3 = 0
counter = 0
counter2 = 0
counter4 = 0
counter5 = 0
lst=[]
lst_task_id = []
lst_real_points = []
lst_dif_points = []
lst_dif_points_end = []
lst3 = []
lst_id_promo = []
lst_betw_time = []
lst_quest_1 = []
lst_quest_2 = []
lst_quest_3 = []
lst_quest_4 = []
def average(lst):
    counter6 = 0
    for i in lst:
        counter6 += int(i)
    if len(lst) != 0:
        ab = counter6 / len(lst)
        return ab
    else:
        return 0
def get_time(time):
    lst4 = ''
    for i in time:
        if i.isdigit():
            lst4 += i
    if int(lst4[2:4]) % 2 == 0:
        f = 30
    elif int(lst4[2:4]) == 2:
        f = 28
    else:
        f = 31

    a = int(int(lst4[8:10]) * 60 + int(lst4[10:12]) + int(lst4[0:2]) * 60 * 60 * 60 + int(lst4[2:4]) * 60 * 60 * 60 * f + int(lst4[4:8]) * 60 * 60 * f * 60 * 12)
    return a


def get_question(task_id):
    base_url = f"https://api.innoprog.ru:3000/task/{task_id}"
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()

        return data['type']


    else:
        print({"Error": "API3 request failed"})


def get_answer(user_id):

    base_url = f"https://bot.innoprog.ru/dataset/detailed/{user_id}"
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()

        return data


    else:
        print({"Error": "API1 request failed"})

def get_all_information(user_id):
    base_url = f'https://bot.innoprog.ru/dataset/general/{user_id}'
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data


    else:
        print({"Error": "API2 request failed"})

data1 = get_answer(5790141925)
data2 = get_all_information(5790141925)

print(data1)
for i in data1:
    lst.append(i['time'])
    if i['task_id'] not in lst_task_id:
        lst_task_id.append(i['task_id'])

for i in data2:
    lst_real_points.append(int(i['real_points']))
    list2 = []
    lst_transform_time = ''
    lst_transform_time_proto = []
    list2.append(int(i['real_points']))
    list2.append(int(i['points']))
    lst_dif_points.append(list2)
    if '+' in i['real_time']:
        b = int(i['real_time'][:-1])
    elif '<' in i['real_time']:
        b = int(i['real_time'][1:])
    else:
        for j in i['real_time']:
            if j.isdigit():
                lst_transform_time += j
            lst_transform_time_proto.append(j)


        v = int(lst_transform_time_proto.index('-'))
        b = (int(lst_transform_time[:v]) + int(lst_transform_time[v:])) // 2


    lst3.append(b)
for i in lst_dif_points:
    a = i[0] - i[1]
    lst_dif_points_end.append(a)

for i in lst3:
    counter += int(i)
for i in lst_dif_points_end:
    counter3 += i

for i in lst_real_points:
    counter2 += i
for i in lst_task_id:
    new_lst = []
    new_lst.append(i)
    new_lst.append(0)
    lst_id_promo.append(new_lst)


for i in data1:
    for j in range(len(lst_id_promo)):
        if lst_id_promo[j][0] == i['task_id']:
            lst_id_promo[j].append(get_time(i['time']))
            lst_id_promo[j][1] += 1
            break
for i in lst_id_promo:
    for j in range(len(i)):
        if j > 1 and j != len(i) - 1:
            lst_betw_time.append(i[j + 1] - i[j])

for i in lst_betw_time:
    if int(i) != 0:
        if int(i) < 0:
            i = int(i) * -1
        else:
            i = int(i)
        counter4 += i
        counter5 += 1

for i in lst_id_promo:
    if get_question(i[0]) == "С вариантами ответов":
        lst_quest_1.append(i[1])
    elif get_question(i[0]) == "Открытый вопрос":
        lst_quest_2.append(i[1])
    elif get_question(i[0]) == "Написание кода":
        lst_quest_3.append(i[1])
    elif get_question(i[0]) == "Дополнение кода":
        lst_quest_4.append(i[1])
def succ(lst):
    if not lst:
        return "Not done"
    else:
        counter7 = 0
        for i in lst:
            i = int(i)
            if i == 1:
                counter7 += 1
        return round(counter7 / len(lst_quest_1) * 100, 2)
print(lst_quest_3)
success1 = succ(lst_quest_1)
success2 = succ(lst_quest_2)
success3 = succ(lst_quest_3)
success4 = succ(lst_quest_4)
attemp1 = round(average(lst_quest_1), 2)
attemp2 = round(average(lst_quest_2), 2)
attemp3 = round(average(lst_quest_3), 2)
attemp4 = round(average(lst_quest_4), 2)
average_batween = round(counter4 // counter5, 2)
average_diff = round(counter3 // len(lst_dif_points_end), 2)
average_points = round(counter2 / len(lst_real_points), 2)
average_time = round((counter // len(lst3)), 2)
quanity_of_taks = len(lst_task_id)




'''print('There are ', quanity_of_taks, 'tasks, which are done')
print('Average time: ', average_time)
print('Average_points: ', average_points)
print('Point differnce: ', average_diff)
print('Average time(between): ', average_batween)
print('Attempts of quest1: ', attemp1)
print('Attempts of quest2: ', attemp2)
print('Attempts of quest3: ', attemp3)
print('Attempts of quest4: ', attemp4)
print('Success1: ', success1)
print('Success2: ', success2)
print('Success3: ', success3)
print('Success4: ', success4)'''
