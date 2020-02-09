"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

Note: Got some help from https://stackoverflow.com/questions/8982163/how-do-i-tell-python-to-convert-integers-into-words

"""
tens = {30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
twenty = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                  'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
                  'eighteen', 'nineteen', 'twenty']


def int_to_eng(input_int):
    if input_int <= 20:
        return twenty[input_int]
    elif input_int < 100 and input_int % 10 == 0:
        return tens[input_int]
    elif input_int < 100:
        return int_to_eng(int(input_int - (input_int % 10))) + int_to_eng(int(input_int % 10))
    elif input_int < 1000 and input_int % 100 == 0:
        return int_to_eng(int(input_int / 100)) + 'hundred'
    elif input_int < 1000:
        return int_to_eng(int(input_int / 100)) + 'hundredand' + int_to_eng(input_int % 100)
    elif input_int == 1000:
        return 'onethousand'


def test():
    assert len(int_to_eng(342)) == 23
    assert len(int_to_eng(115)) == 20
    assert len(int_to_eng(100)) == 10


def main():
    chars = 0
    for i in range(1, 1001):
        chars += len(int_to_eng(i))
    print(chars)


test()
main()
