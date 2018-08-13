'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.

###Examples:

### Python ###

tickets([25, 25, 50]) # => YES
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
'''


def tickets(people):
    change = list()
    price = 25
    for x in people:
        rc = x - price
        if rc < 0:
            return "NO"
        elif rc > 0:
            sort_change = sorted(change)
            for i, c in enumerate(sort_change):
                if rc in change:
                    change.pop(change.index(rc))
                    change.append(x)
                    rc = 0
                    break
                rc -= c
                if rc == 0:
                    change.append(x)
                    break
                elif rc < 0:
                    return "NO"
                change = sort_change[i+1:]
            if rc > 0:
                return "NO"
        else:
            change.append(x)
    return "YES"
