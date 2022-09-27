# This is a program to calculate the price of x cups
def main(): #<-- Don't change this line!
    # Write your code below. It must be indented!


    # input: price of one cup-number of cups
    price_of_one_cup = 3.25
    tax_rate = 1.15
    print("Welcome to nscc coffee shop")
    print("We sell coffee for $ " + str(price_of_one_cup) + " per cup!")
    number_of_cups = input("please enter the number of cups:")


    # processing: total_pre_tax = price of one cup * number of cups
                 # total_post_tax = total_pre_tax * tax_rate
    total_pre_tax = price_of_one_cup * int(number_of_cups)
    total_post_tax = total_pre_tax * tax_rate
    # output: Total cost

    #print("your total pre-tax is: $" + str(total_pre_tax))
    #print("your total post-tax is: $" + str(total_post_tax))
    #print("your total pre-tax is: $ {0} ".format(total_pre_tax))
    print("your total pre-tax is: ${0} and your total post tax is ${1} ".format(total_pre_tax, total_post_tax))

#Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()



