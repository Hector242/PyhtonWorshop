# Ciclo For
#
def ciclo(i, n):
    for i in range(n):
        calculation = 2**i
        if calculation < n:
            print("2**" + str(i) + "= " + str(calculation))
        else:
            return 0


def main():
    ciclo(0,1000)

if __name__ == "__main__":
    main()
################################
# Ciclo while
#
# def main():
#     LIMIT = 1000

#     count = 0
#     calculation = 2**count
#     while calculation < LIMIT:
#         print("2**" + str(count) + "= " + str(calculation))
#         count = count + 1
#         calculation = 2**count

# if __name__ == "__main__":
#     main()