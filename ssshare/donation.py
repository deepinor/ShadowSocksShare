#!/usr/bin/env python3
decline = '我不加微信，有事还是email联系吧：）'
# info contains (number, message, name, reply)
info = [
    (2, "感谢无私分享", "QQTelnet"),
]


def parse(data):
    if len(data) == 1:
        number, message = data[0], ''
    else:
        number, message = data[:2]
    if message:
        message = '，并留言：<b>”{}“</b>'.format(message)
    if len(data) >= 3:
        name = '<b>' + data[2] + '</b>'
    else:
        name = '某位没有留下名字的'

    if len(data) >= 4:
        comment = '<br>to 这位朋友：<b>{}</b>'.format(data[3])
    else:
        comment = ''

    return_data = '<p>{name}朋友捐献了<b>{number}</b>元{message}：）<b>{comment}</b></p>'.format(
        name=name,
        number=number,
        message=message,
        comment=comment)
    return return_data


sum_people = len(info)
sum_money = '{:.2f}'.format(sum(list(zip(*info))[0]))
data = '\n'.join(map(parse, info))


if __name__ == '__main__':
    print("sum_people: ", sum_people)
    print("sum_money: ", sum_money)
