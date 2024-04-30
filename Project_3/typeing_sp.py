# from time import *
# import random as r


# def mistake(partest,usertest):
#     erros = 0
#     for i in range(len(partest)):
#         try:
#             if partest[i] != usertest[i]:
#                 erros += 1
#         except:
#             erros += 1
#     return erros

# def speed_time(time_s,time_e,user_in):
#     time_delay = time_e - time_s
#     time_R = round(time_delay,2)
#     speed = len(user_in)/time_R
#     return round(speed)


# test = ["Hello i am Mohammad ali sk and i love to write to code in python language",'i am from India','what are you eating']

# test1 = r.choices(test)
# print("***** Typing Speed *****")
# print(test1)
# print()
# print()


# time_1 = time()
# testinput = input("Enter : ")
# time_2 = time()

# print(f"Speed : {speed_time(time_1,time_2,testinput)}, w/sec")
# print(f"Error : {mistake(test1,testinput)}")



import qrcode as qr

img = qr.make(9883367897)
img.save("Phonepiay.png")