from DoublyLists import Lists


def main():
    list = Lists()
    list.push(6)
    list.push(3)
    list.push(3)
    list.push(3)
    list.push(3)
    list.insert_after(list.head.next,55)
    list.append(100)
    list.print_list()

if __name__ == '__main__':
    main()
