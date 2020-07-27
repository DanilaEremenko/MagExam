import sys
import re


def main():
    if len(sys.argv) != 2:
        raise Exception('Only path to input file should be passed')

    people_dict = {}
    item_dict = {}
    full_sum = 0
    with open(sys.argv[1]) as input_file_fp:
        for line in input_file_fp.read().split(';'):
            if line != '':
                ###########################################################
                # -----nice trap with spaces for 'одноразовая посуда' -----
                ###########################################################
                line = re.sub(', +', ',', line)
                line = re.sub(' +,', ',', line)

                name, shop_item, price = line.replace('\n', '').split(',')
                if not price.isnumeric():
                    raise Exception('Is not numeric price for %s:%s' % (name, shop_item))
                else:
                    name = name.lower()
                    shop_item = shop_item.lower()

                    if name not in people_dict:
                        people_dict[name] = int(price)
                    else:
                        people_dict[name] += int(price)

                    if shop_item not in item_dict:
                        item_dict[shop_item] = int(price)
                    else:
                        item_dict[shop_item] += int(price)

                    full_sum += int(price)

    while True:
        input_key = input("Type your request:").lower()

        ##################################
        if input_key == '\exit':
            break
        elif input_key in people_dict.keys():
            print('%d' % (people_dict[input_key]))

        ##################################
        elif input_key in item_dict.keys():
            print('%d' % (item_dict[input_key]))

        ##################################
        elif input_key == 'сумма':
            print(str(full_sum))
        else:
            raise Exception('Bad input data')


if __name__ == '__main__':
    main()
