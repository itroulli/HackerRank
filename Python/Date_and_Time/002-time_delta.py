# Name: Time Delta
# Problem: https://www.hackerrank.com/challenges/python-time-delta/problem
# Score: 30

from datetime import datetime


for _ in range(int(input())):
    dt1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    dt2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(int(abs((dt1-dt2).total_seconds())))


# OR if you want to keep the template provided by HackerRank:

# #!/bin/python3
#
# from datetime import datetime
#
#
# # Complete the time_delta function below.
# def time_delta(t1, t2):
#     dt1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
#     dt2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
#     return str(int(abs((dt1-dt2).total_seconds())))
#
#
# if __name__ == '__main__':
#
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input())
#
#     for t_itr in range(t):
#         t1 = input()
#
#         t2 = input()
#
#         delta = time_delta(t1, t2)
#
#         fptr.write(delta + '\n')
#
#     fptr.close()
