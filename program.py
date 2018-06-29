from tasks import get_stock_info, call_back, short_call_back
from celery import group, chord


def group_test():
    my_group = group((get_stock_info.s(delay) for delay in [4, 5, 8]), queue="dev")
    res = my_group()
    resp = res.get()
    print("We are done")


def chord_test():
    header = (get_stock_info.subtask((delay,)) for (delay) in [4, 5, 10])
    callback = call_back.subtask()
    # res = chord((add.s(i, i) for i in xrange(10)), xsum.s())()

    header_1 = (get_stock_info.subtask((delay,)) for delay in [1, 1, 1])
    callback_1 = short_call_back.subtask()

    res = chord(header)(callback)
    res_1 = chord(header_1)(callback_1)


    print(res.get())
    print(res_1.get())
    print("We are done")


def chord_queue():
    header = (get_stock_info.subtask((delay,)) for delay in [4, 5, 4])
    callback = call_back.subtask(kwargs={'zoom':10, 'name':'whatsup'})
    res = chord(header,queue='dev')(callback)

    # header_1 = (get_stock_info.subtask((delay,)) for delay in [4, 5, 4])
    # callback_1 = call_back.subtask()
    # res_1 = chord(header_1, queue='dev')(callback_1)

    #print(res.get())
    #print(res_1.get())
    print("We are done")


def queue_test():
    res = get_stock_info.apply_async((4,), queue="dev")
    res.get()


if __name__ == '__main__':
    # group_test()
    # chord_test()
    # queue_test()
    chord_test()
    # chord_queue()
