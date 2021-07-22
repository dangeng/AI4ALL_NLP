{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Python_Worksheet.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "iQo8LbxsP0v0",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import sys\n",
        "IN_COLAB = 'google.colab' in sys.modules\n",
        "\n",
        "if IN_COLAB:\n",
        "    from google.colab import drive\n",
        "    drive.mount('/content/drive')\n",
        "    %cd '/content/drive/My Drive/AI4All-UM-NLP'"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MWucLu2PQceB",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "%load_ext autoreload\n",
        "%autoreload 2\n",
        "import lib"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ht2Osg_8Zj3_",
        "colab_type": "text"
      },
      "source": [
        "# Intro\n",
        "This notebook is intended to make you more comfortable with some of the key tools that we need for our project: conditionals, loops, lists, sets, and dictionaries.\n",
        "\n",
        "There are lots of examples of how to do things, and also exercises for you to complete. \n",
        "\n",
        "The exercises may have a max number of lines specified. These are lines of running code that _you add_, and don't involve comments. Try to fit your answer in the specified number of lines, as that is the answer that will help you learn the most generalizable python constructs!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Lgeuu4bneiSK",
        "colab_type": "text"
      },
      "source": [
        "# Conditionals\n",
        "You may know conditionals as \"if-statements\". This is when you write `if`, `elif`, or `else` to control the flow of your code, and are very important to understand!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "O6BYv8Z6ez4I",
        "colab_type": "text"
      },
      "source": [
        "## Basic if\n",
        "Here is an example of a basic if statement, using mathematical operators."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5itb76oJezGj",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "x = 200\n",
        "\n",
        "if x < 200:\n",
        "  print('small!')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QfvhHvqPe_gw",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Write an if statement that prints 'huge' if `x` is greater than 500"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "r_QGGlr1fWSU",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "x = 50\n",
        "\n",
        "## your work here\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "n_oLM--KfZ_8",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Write an if statement that prints 'exactly!' if `x` is exactly equal to 300"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yyyL3p1Rflpt",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "x = 299.5\n",
        "\n",
        "## your work here\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NMd1mUGJggq3",
        "colab_type": "text"
      },
      "source": [
        "## If-Else\n",
        "If-else is used to do something \"else\" if the `if` condition turns out to be false. Here's an example:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KQErrgb6gvjQ",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "x = 200\n",
        "\n",
        "if x == 300:\n",
        "  print('Nope, this is not the case')\n",
        "else:\n",
        "  print('We ended up in the else block this time!')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_FJqJyJkgurX",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Before, you wrote an `if` statement to check if a number was equal to exactly 300. Set `x` so that 'exactly' ends up printing!"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "k7mVBxZYhW8S",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "## write your code here!\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qzkCBkHdhZty",
        "colab_type": "text"
      },
      "source": [
        "## If-Elif-Else\n",
        "Elif is used in special cases where you need more than one condition. This is often the case if you have more than two values that a variable can be set to.\n",
        "\n",
        "Here's an example where `elif` is used.\n",
        "\n",
        "Use your imagination to imagine that `color` can represent any color. Here, we print which of the three primary colors it is, if it is one. If it is not one, we print 'it is not a primary color'."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wl6crTqYiF4G",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "color = 'red'\n",
        "\n",
        "if color == 'blue':\n",
        "  print('it is blue!')\n",
        "elif color == 'red':\n",
        "  print('it is red!')\n",
        "elif color == 'yellow':\n",
        "  print('it is yellow!')\n",
        "else:\n",
        "  print('it is not a primary color')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sZAr6kL8jI5w",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Create a new version of the code above, that only uses `if` and `else`. If the color is primary, print 'it is a primary color', otherwise, print 'it is not a primary color'.\n",
        "\n",
        "Hint: I recommend using `or` for this exercise. If you're confused about using `or`, look at the paper worksheet."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "o404OEIMj2RS",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "## write your code here\n",
        "## try setting `color` to different values, so that you get all of the different strings to print!\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "V7t5X-IKkBnC",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Here we will try to figure out if `elif` is really necessary, or if we can do everything with `if` and else.\n",
        "\n",
        "Try to write the whole if-statement above (that prints about blue, red, yellow, and not primary) above, using only `if` and `else`.\n",
        "\n",
        "There are two things that you can do here\n",
        "1. Use `if` and `else` to write equivalent code. Use as many lines as you want. Hint: _use nested `if` statements_\n",
        "1. (challenge) If you want to challenge yourself even more, write code that is equivalent **using only five lines of code** including where `color` is defined. This will require using `+` to concatenate strings\n",
        "\n",
        "This exercise is a bit more challenging than the other ones, so please let us know if you need help!"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vT24NfA3k8Oe",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "## your work here\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SAVE-t2ak8bL",
        "colab_type": "text"
      },
      "source": [
        "Hopefully, you've found that you don't really _need_ elif, but it is useful to make your code look cleaner!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-FQaiixpcekR",
        "colab_type": "text"
      },
      "source": [
        "# Loops\n",
        "Loops are key when you are programming in python, and are one of the first things that you will want to get comfortable with. Here we will go over basic loops, and later we will go over loops through lists, sets, and dictionaries!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "a4J7BGAEcydY",
        "colab_type": "text"
      },
      "source": [
        "## For Loops\n",
        "The most basic for loop uses `range` with a single parameter, the max value (exclusive). By exclusive, we mean that the `range` excludes the max, only including `max - 1`.\n",
        "\n",
        "When you use range, the value for `i` starts from 0 unless you specify otherwise."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "odENP99Ncxg2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# 10 is the max value for the loop\n",
        "# the code on line 6 will be run 10 TIMES (the number you used in range)\n",
        "# this means that i will take on values 0, 1, 2, 3, 4, 5, 6, 7, 8, 9\n",
        "for i in range(10):\n",
        "  # will print 1, then 2, then 3... all the way up to 9.\n",
        "  print(i)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vbd3IHP0dktd",
        "colab_type": "text"
      },
      "source": [
        "In a slightly more complicated loop, we can start from a non-zero number!"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZjsmcOo6dt75",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# 10 is the max value for the loop\n",
        "# the code on line 6 will be run 5 TIMES (10 - 5, the numbers you used in range)\n",
        "# this means that i will take on values 5, 6, 7, 8, 9\n",
        "for i in range(5, 10):\n",
        "  # will print 5, 6, 7, 8, 9\n",
        "  print(i)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XqcGsqBLeD71",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Write a for loop that prints all of the numbers from 0 to 25 **including 25**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1HpNLXHbeRi-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "## write your solution here\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8vrKm5_sfyrk",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "\n",
        "Write a for loop that prints all of the **even** numbers from 6 to 20, not including 20. A skeleton is provided, which helps to figure out if something is even"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Qlj4ugjxgOz3",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "for ... # finish this line!\n",
        "  even = i % 2 == 0 # you don't need to understand this line. even is a boolean, if it is True, the number is even\n",
        "  # finish the exercise by checking if even is True, and printing only if it is!\n",
        "  "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MOky4S8aROwW",
        "colab_type": "text"
      },
      "source": [
        "# Lists\n",
        "Here we'll go over the tools you need to work with lists.\n",
        "\n",
        "There are ton of other things that you can do with lists... insert in the middle, combine two lists together, remove things... but for us, we will only focus on the most important things to get comfortable using them!\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3nTf8fD-lc3r",
        "colab_type": "text"
      },
      "source": [
        "## Creating lists\n",
        "Here are some examples of how to create lists. There are two main ways: creating a list with things in it, and creating an empty list and adding to it as you go. You can also create a list with things in it _and_ add as you go, of course!"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "54nBYIk0lnuR",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# how to create a new list with things in it\n",
        "lst = [0, 1, 2]\n",
        "\n",
        "print(lst)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1HUXLpxIRLxL",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# how to create a new (empty) list\n",
        "lst = []\n",
        "\n",
        "# add 0, 1, and 2 to the list\n",
        "# append puts something at the end of the list\n",
        "# comments show what is in the list at each point\n",
        "\n",
        "# []\n",
        "lst.append(0)\n",
        "\n",
        "# [0]\n",
        "\n",
        "lst.append(1)\n",
        "\n",
        "# [0, 1]\n",
        "\n",
        "lst.append(2)\n",
        "\n",
        "# [0, 1, 2]\n",
        "\n",
        "print(lst)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PxFZtbe2Rix3",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# how to add 0, 1, and 2 to the list with a loop\n",
        "\n",
        "lst = []\n",
        "\n",
        "for i in range(3): # --> range(3) will make i = 0, 1, and 2 in that order\n",
        "  lst.append(i)\n",
        "    \n",
        "print(lst)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NlirTLs2egO6",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Add all even numbers from 0 to 8 to a list\n",
        "\n",
        "You can do this by multiplying numbers between 0 and 4 by 2!\n",
        "\n",
        "Alternatively, you can use the trick we used above to check if something is even.\n",
        "\n",
        "Try to do this with and without a loop.\n",
        "\n",
        "Print your list at the end to confirm that your code is correct."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UZCnUXdme8Q-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "## write your solution here\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zmga8mCVl1_4",
        "colab_type": "text"
      },
      "source": [
        "Don't print this list before answering the question below"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "s48H97Sde96-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "lst = []\n",
        "for i in range(3):\n",
        "  lst.append(i - 5)\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "B1kmwGztfDYT",
        "colab_type": "text"
      },
      "source": [
        "what is in lst now?"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0jv9wX1MfG2F",
        "colab_type": "text"
      },
      "source": [
        "your answer:"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CTzKuBJZzk8V",
        "colab_type": "text"
      },
      "source": [
        "Now, print the list to confirm your answer"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MDng97CvznY4",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "y6-1ddv9nRMf",
        "colab_type": "text"
      },
      "source": [
        "## Reading from a List\n",
        "To read an element from a list, we use its index. Remember, in python, indexes start from 0, and are numbers that point us to a specific item in a list. The first item is item 0, the second is item 1, and so on...\n",
        "\n",
        "Here are some examples using indexing"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rgH6kc3KncIv",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "lst = [7, 8, 9, 10, 11, 12]\n",
        "\n",
        "# will print 8\n",
        "print(lst[1])\n",
        "\n",
        "# will print 11\n",
        "print(lst[4])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sNpABxS8nyNF",
        "colab_type": "text"
      },
      "source": [
        "### Backwards Indexing\n",
        "You can also index using negative numbers. This will start from the back of the list. Keep in mind, these start at -1, not 0."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pJneWKIjn7rq",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# will print 12\n",
        "print(lst[-1])\n",
        "\n",
        "# will print 11\n",
        "print(lst[-2])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bal1A0fIoEdx",
        "colab_type": "text"
      },
      "source": [
        "## Exercise\n",
        "Given the list below, print 4, 7, and 9. Make sure that you use the list in each of your print statements!\n",
        "\n",
        "An example is given that prints 6.\n",
        "\n",
        "Challenge: use both forward and backwards indexing"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8jd108w-oQQ_",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "lst = [1, 3, 9, 6, 7, 2, 8, 4]\n",
        "\n",
        "print(lst[3])\n",
        "\n",
        "## your work here\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lln35OD9aI0R",
        "colab_type": "text"
      },
      "source": [
        "## Checking if Something is in a List\n",
        "You may want to check if something is included in a list. This is how it's done. You use the python `in` operator.\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dVeQ_ZyTadek",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "lst = [4, 5, 20, 50, 15]\n",
        "\n",
        "print(40 in lst) # --> should print 'False'\n",
        "print(4 in lst)  # --> should print 'True'"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2z16pMApamO3",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "check if `20` is in your list"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mOtbeKirasBb",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "## write your solution here\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0PkXxxDJbKPZ",
        "colab_type": "text"
      },
      "source": [
        "## Calculating the Length of a List\n",
        "To calculate the length of a list, use the `len` operator, like this. Before running it, what do you think it should print? Confirm that your answer is correct by running the code."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sWbnJurdbWGC",
        "colab_type": "text"
      },
      "source": [
        "Answer:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "n4hu7aqUbRAy",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "lst = [4, 5, 20, 50, 15]\n",
        "\n",
        "print(len(lst))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kHlSK9okbXh9",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Modify the list so that the following code prints `10`"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Q4BUGMgsbhLS",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# modify this list\n",
        "lst = [4, 5, 20, 50, 15]\n",
        "\n",
        "# don't modify anything after this point!\n",
        "print(len(lst))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SJRGT7EnfUbM",
        "colab_type": "text"
      },
      "source": [
        "## Looping through a list\n",
        "You can also loop through a list and do something with each element. There are two main ways to do it."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PKP7csWzfFuV",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "lst = [4, 5, 20, 50, 15]\n",
        "\n",
        "# method 1: you can use range(len(lst))\n",
        "# this is like what we did before with range\n",
        "for i in range(len(lst)):\n",
        "  print(lst[i])\n",
        "  \n",
        "  \n",
        "# method 2: you can loop through elements directly\n",
        "# this means that you don't need to use an index, like lst[i]\n",
        "for element in lst:\n",
        "  print(element)\n",
        "  \n",
        "  \n",
        "# these blocks of code both do the same thing!"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vLsg_utvmWhZ",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Loop through the list that is defined below, and add all items that are greater than 10 to `lst_2`. Print out `lst_2` at the end."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ier0XF3umi0H",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "lst = [16, 17, 20, 18, 3, 4, 27, 9, 3, 50]\n",
        "\n",
        "lst_2 = []\n",
        "# write your for loop here"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nwgnPfoTXgmI",
        "colab_type": "text"
      },
      "source": [
        "# Sets\n",
        "Sets are kind of like lists, but they only contain one of each item, and are _unordered_! Even if you try to add something a second time, it will only be put in in the set one time."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FMR8XTXMXrYE",
        "colab_type": "text"
      },
      "source": [
        "## Creating sets\n",
        "Like lists, there are a few ways to create sets. We will show a few of them below. They will all create the same set!"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5cdK7uTRX3qz",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# method 1: creating a set using brackets\n",
        "# you can create a set using brackets if you already know what will be in it\n",
        "s = {4, 5, 6}\n",
        "\n",
        "print(s)\n",
        "\n",
        "# method 2: creating a set then adding things to it\n",
        "s = set() # --> WARNING: you can't create an empty set using {} because it will create a dictionary\n",
        "s.add(4)\n",
        "s.add(6)\n",
        "s.add(5)\n",
        "\n",
        "print(s)\n",
        "\n",
        "# method 3: you can create a set from a list\n",
        "# this is a good thing to do if you want to know all of the unique items in a list\n",
        "# making it into a set will remove all non-unique items\n",
        "l = [4, 6, 6, 4, 5]\n",
        "s = set(l)\n",
        "\n",
        "print(s)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "G24__V9SYx6o",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "What will this print?"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uv6wBXt3ZVIN",
        "colab_type": "text"
      },
      "source": [
        "Answer:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wBECmI0wZW3d",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# add a print statement to check you work!\n",
        "l = [10, 9, 8, 7, 6, 6, 5, 4, 3]\n",
        "s = set(l)\n",
        "print(len(s))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3-MQuWovZAtx",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Create a set with numbers numbers 0-10 in it. **Your solution should use a loop and no more than 5 lines of code, including prints**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jx9dVMh8ZAK1",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "## write your solution here\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Zh2JH3hGYpVm",
        "colab_type": "text"
      },
      "source": [
        "## Checking if Something is in a Set\n",
        "This is basically the same as checking if something is in a set, but a nice thing is that it is faster because of how sets are implemented! However, you don't need to worry much about speed unless you have a huge list/set!"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fhTvtHXYYogS",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "s = {4, 5, 6}\n",
        "\n",
        "print(40 in s) # --> should print 'False'\n",
        "print(4 in s)  # --> should print 'True'"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EcOSgwQkbBd4",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Check if 50 is in your set"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eA-ZqZjTbA1Q",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "## write your solution here\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CvgjhvuCbp5o",
        "colab_type": "text"
      },
      "source": [
        "## Looping Through Sets\n",
        "You loop through a set the same way that you loop through a list using an item directly. Because they are unordered, **you can not use an index**."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wAlEaSdVrvbk",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "s = {1, 2, 3, 4}\n",
        "\n",
        "## good way to loop through a set\n",
        "for item in s:\n",
        "  print(item)\n",
        "  \n",
        "## bad way to loop through a set\n",
        "## there will be an exception\n",
        "for i in range(len(s)):\n",
        "  print(s[i])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Tl6f9fyIr9Vu",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Fix this code block so that it does not have any exceptions, and prints out all numbers in the set that are less than 10."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ys72d6FIsKGm",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "s = {5, 3, 2, 28, 6, 7, 8, 1, 11, 19, 24}\n",
        "\n",
        "## fix this code so that it works!\n",
        "for i in range(len(s)):\n",
        "  if s[i] < 10:\n",
        "    print(s[i])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "C_UsnG2l63CW",
        "colab_type": "text"
      },
      "source": [
        "# Dictionaries\n",
        "Here we will go over how to use dictionaries.\n",
        "\n",
        "A dictionary is made up of **keys** and **values**.  A key is used to look up a value.\n",
        "\n",
        "There are a few common uses of dictionaries in our code:\n",
        "\n",
        "1. keys are demographic properties (i.e. 'married') and values are counts.  \n",
        "    Dictionaries are very useful when you want to count things up. We'll see how to do that later on.\n",
        "1. keys are demographic property names (i.e. 'age') and values are demographic properties (i.e. 27)  \n",
        "    Dictionaries are a way to store information about a thing with clear labels.\n",
        " \n",
        " \n",
        " Dictionaries are _unordered_, so do not worry about the order they print in!"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XyGH2o107OZx",
        "colab_type": "text"
      },
      "source": [
        "### Construction\n",
        "There are a few ways to construct a dictionary. Here, we'll imagine that our dictionary is keeping track of items at a store."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fw38xBGa8nra",
        "colab_type": "text"
      },
      "source": [
        "Creating an empty dictionary and adding all items"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hapR9Uva62NW",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# create an empty dictionary\n",
        "d = {}\n",
        "\n",
        "# add pasta\n",
        "d['pasta'] = 40\n",
        "\n",
        "# add juice\n",
        "d['juice'] = 35\n",
        "\n",
        "# add salad\n",
        "d['salad'] = 4\n",
        "\n",
        "# print out the dictionary\n",
        "print(d)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9KCC9vso8rph",
        "colab_type": "text"
      },
      "source": [
        "Creating a dictionary with things in it"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WDO2H66d8rJ7",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# you can also create a dictionary that already has things in it!\n",
        "# you would do this if you already know the keys and values\n",
        "d = {'pasta': 40, 'juice': 35, 'salad': 4}\n",
        "\n",
        "print(d)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Mf9t4IDq92Gj",
        "colab_type": "text"
      },
      "source": [
        "#### Exercise\n",
        "Construct a dictionary to represent the following stock table for a store:\n",
        "\n",
        "| Item       | Count |\n",
        "|------------|-------|\n",
        "| Cherries   | 239   |\n",
        "| Hamburgers | 158   |\n",
        "| Cheetos    | 400   |\n",
        "| Milk       | 325   |\n",
        "| Cookies    | 47    |\n",
        "\n",
        "Do it both ways"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hYefKgPc59lo",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "## write your solution here\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VHQ9gJOq-rrI",
        "colab_type": "text"
      },
      "source": [
        "## Reading From A Dictionary\n",
        "\n",
        "To read from a dictionary, you put the key you want to read in square brackets, like this"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1A3IT22a-ykF",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# defining out stock dictionary\n",
        "d = {'pasta': 40, 'juice': 35, 'salad': 4}\n",
        "\n",
        "# reads the pasta key\n",
        "print(d['pasta'])"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "T2f_X9Zf-7EA",
        "colab_type": "text"
      },
      "source": [
        "#### Exercise\n",
        "Print how much juice there is at the store by reading from the dictionary"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tMqbZnfT-39-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "## write your solution here\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rMZEclLA_Egs",
        "colab_type": "text"
      },
      "source": [
        "## Updating a Dictionary\n",
        "\n",
        "We also want to be able to change values in a dictionary. If we know the new value, it is easy to set it directly"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ujOMKmau_Bn9",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# defining out stock dictionary\n",
        "d = {'pasta': 40, 'juice': 35, 'salad': 4}\n",
        "\n",
        "# update pasta to be 45. we could do this if we counted wrong initially and confirmed that there are 45 pastas\n",
        "d['pasta'] = 45\n",
        "\n",
        "# when we print, we should see 'pasta': 45\n",
        "print(d)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Y1O-zpJzAPHF",
        "colab_type": "text"
      },
      "source": [
        "We can also add to or subtract from the number of things in the dictionary"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "dCCBMV-IAOoB",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# defining our stock dictionary\n",
        "d = {'pasta': 40, 'juice': 35, 'salad': 4}\n",
        "\n",
        "# add more pasta\n",
        "d['pasta'] += 1\n",
        "\n",
        "# add more pasta another way\n",
        "d['pasta'] = d['pasta'] + 5\n",
        "\n",
        "# subtract a bottle of juice\n",
        "d['juice'] -= 1\n",
        "\n",
        "# subtract five bottles of juice another way\n",
        "d['juice'] = d['juice'] - 5"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "e7--ifZZPhvn",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "What will be printed out below? How many of each item will be in the dictionary?"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ILGAaQnpPoA0",
        "colab_type": "text"
      },
      "source": [
        "Pasta:\n",
        "\n",
        "Juice:\n",
        "\n",
        "Salad:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AsS3-acEPhH0",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# print the dictionary here to check your answer!\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PmGNwLcyUvHq",
        "colab_type": "text"
      },
      "source": [
        "## Checking if Something is in a Dictionary\n",
        "You may want to check if something is included in a dictionary. This is how you do it (it is about the same as lists and sets, and only applies to keys)."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5RCwhcCGU5GH",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# defining our stock dictionary\n",
        "d = {'pasta': 40, 'juice': 35, 'salad': 4}\n",
        "\n",
        "# check if 'pasta' is in the dictionary\n",
        "print('pasta' in d) # --> should print 'True'\n",
        "\n",
        "# check if 'sardines' is in the dictionary\n",
        "print('sardines' in d) # --> should print 'False'"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DXNQU2CKVHUX",
        "colab_type": "text"
      },
      "source": [
        "## Exercise\n",
        "What would the code below print?"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GXdDBcyoVMAJ",
        "colab_type": "text"
      },
      "source": [
        "Your answer:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "E79J_sVeVPPt",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# defining our stock dictionary\n",
        "d = {'pasta': 40, 'juice': 35, 'salad': 4}\n",
        "\n",
        "print('juicy juice' in d)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "em25kUFOPuUX",
        "colab_type": "text"
      },
      "source": [
        "## Looping Through Dictionaries\n",
        "There are a few ways to loop through dictionaries. Here I will show three ways. I will print the keys and values in both cases."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "o6VuRgzyANsF",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# defining our stock dictionary\n",
        "d = {'pasta': 40, 'juice': 35, 'salad': 4}\n",
        "\n",
        "# method 1\n",
        "for key in d: # if you loop through d, you automatically get the keys\n",
        "  # print out the key and the item stored at key\n",
        "  print(key, d[key])\n",
        "    \n",
        "# method 2\n",
        "for key in d.keys(): # if you prefer to be explicit, you can use d.keys() to get a list of just keys. this does the same thing as 1\n",
        "  # print out the key and the item stored at key\n",
        "  print(key, d[key])\n",
        "  \n",
        "# method 3\n",
        "for key, value in d.items(): # if you use .items(), you can get keys and values at the same time!\n",
        "  print(key, value)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "--rG3chRQs2g",
        "colab_type": "text"
      },
      "source": [
        "### Looping through just values\n",
        "You may also want to just loop through values. You can do that by using the method `.values()`, as is shown below:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gKyLScRQQIb5",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "for value in d.values():\n",
        "  print(value)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "B68IqHT7Q8-N",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Print all keys in this dictionary (`d`) with a value greater than 30. **You solution should use a loop and only take up three additional lines**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DyjZXIwGQ3aP",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# defining our stock dictionary\n",
        "d = {'pasta': 40, 'juice': 35, 'salad': 4, 'asparagus': 2, 'lemon': 17, 'orange': 54, 'salsa': 49}\n",
        "\n",
        "## write your solution here\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xxlfADILRnuL",
        "colab_type": "text"
      },
      "source": [
        "## Creating a new dictionary from an old one\n",
        "Sometimes, you will want to create a new dictionary that only contains some keys from your old dictionary. For example, if you wanted to create a dictionary with only keys that start with the first half of the alphabet (A-L), you could do this:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tPvNciv2RY64",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# defining our stock dictionary\n",
        "d = {'pasta': 40, 'juice': 35, 'salad': 4, 'asparagus': 2, 'lemon': 17, 'orange': 54, 'salsa': 49}\n",
        "\n",
        "# initializing a new dictionary\n",
        "first_half_dict = {}\n",
        "\n",
        "# loop through items\n",
        "for key, value in d.items():\n",
        "  # check if first letter is in first half of alphabet\n",
        "  if key[0] in 'abcdefghijkl':\n",
        "    # add to new dictionary\n",
        "    first_half_dict[key] = value\n",
        "    \n",
        "print(first_half_dict)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4TsE7QqbScB1",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Create a new dictionary that only includes items where there are less than 20 in stock. We may need to re-order them!\n",
        "\n",
        "**Please use a loop for this exercise!**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qhbmGoDFSVA5",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# defining our stock dictionary\n",
        "d = {'pasta': 40, 'juice': 35, 'salad': 4, 'asparagus': 2, 'lemon': 17, 'orange': 54, 'salsa': 49}\n",
        "\n",
        "new_dict = {}\n",
        "\n",
        "## write your solution here\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "S-tQPsC_SwLp",
        "colab_type": "text"
      },
      "source": [
        "## Counting with a Dictionary\n",
        "Dictionaries are also a useful tool that can be used to count up an arbitrary number of items. We'll derive how it's done below"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RrBRYNU-Sn3d",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# define a list of produce. we want to count the occurrences of everything in the list\n",
        "produce = ['salad', 'asparagus', 'asparagus', 'orange', 'lemon', 'lemon', 'orange', 'asparagus', 'orange', 'lemon', 'orange']\n",
        "\n",
        "# the output should look like this. \n",
        "# remember, dictionaries are unordered, so you should not be concerned if you end up with a different order\n",
        "# {'salad': 1, 'asparagus': 3, 'orange': 4, 'lemon': 3}\n",
        "\n",
        "# define a dictionary to hold produce counts\n",
        "produce_counts = {}\n",
        "\n",
        "# WARNING: this code doesn't work and is here to explain why we need to do certain things!\n",
        "\n",
        "# loop through everything in produce\n",
        "for veggiefruit in produce:\n",
        "  # increase count of a veggiefruit\n",
        "  produce_counts[veggiefruit] += 1\n",
        "  \n",
        "print(produce_counts)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_LPmN2dNUWES",
        "colab_type": "text"
      },
      "source": [
        "In our loop, we try to increase the count of `veggiefruit`. However, it (currently set to `'salad'` in the loop) is not a key in produce_counts, which is why we get a `KeyError`.\n",
        "\n",
        "To fix this problem, we need to add `veggiefruit` to `produce_counts` if it's not already there, like we do here.\n",
        "\n",
        "Remember, we showed before how to check if something is in a dictionary. If you don't remember it, look above!"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xeQqyUkeURP6",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# loop through everything in produce\n",
        "for veggiefruit in produce:\n",
        "  if veggiefruit in produce_counts:\n",
        "    # increase count of a veggiefruit if it is already in produce_counts\n",
        "    produce_counts[veggiefruit] += 1\n",
        "  else:\n",
        "    # add veggiefruit to produce_counts and set it to 1 if it is not there yet\n",
        "    produce_counts[veggiefruit] = 1\n",
        "    \n",
        "print(produce_counts)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5cymXJ3mVqBK",
        "colab_type": "text"
      },
      "source": [
        "This time, we got the desired output"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HD6r46a0WHBK",
        "colab_type": "text"
      },
      "source": [
        "### Exercise\n",
        "Loop through `shoes`, and count how many of each type of shoes we have using a dictionary. Make sure to check your result by counting manually!"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "abHsXD3kVm54",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# defining our shoes dictionary\n",
        "shoes = ['sandals', 'boots', 'sneakers', 'boots', 'heels', 'boots', 'sneakers', 'sneakers', 'boots', 'boots']\n",
        "\n",
        "## write your solution here\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "R16o-j9AWlUU",
        "colab_type": "text"
      },
      "source": [
        "# Putting it All Together\n",
        "Let's go back to the demographics exercise from yesterday. Try to count all of the countries in the dataset using a dictionary. The skeleton for this code is provided. **You should only need to add four lines of code for your solution!**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6T2uS8yEWkwu",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "demographics = lib.load_demographics()\n",
        "\n",
        "country_counts = {}\n",
        "for worker in demographics:\n",
        "  country = worker['country']\n",
        "  ## write your solution here\n",
        "  \n",
        "  ## finish your solution\n",
        "  \n",
        "print(country_counts)"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}
