# -*- coding: utf-8 -*-
from difflib import SequenceMatcher

listA = ['АТКалининскаяАЭС']
listB = ['АТКалАЭС']


def compare_strings(mylist):
    if (len(mylist) < 2):
        return 0.00
    else:
        cnt = 0
        total = 0.0
        for i in range(len(mylist)):
            for j in range(i + 1, len(mylist)):
                val = SequenceMatcher(None, mylist[i], mylist[j]).ratio()
                total += val
                cnt += 1
        return (total / cnt)


print("Sting simalarity in list 1 is %.5f" % (compare_strings(listA)))
print("Sting simalarity in list 2 is %.5f" % (compare_strings(listB)))
