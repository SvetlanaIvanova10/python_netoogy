# Необходимо реализовать класс Stack со следующими методами:
# isEmpty - проверка стека на пустоту. Метод возвращает True или False.
# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
# size - возвращает количество элементов в стеке.

class Stack():
    def __init__(self,*elements):
        self.elements = list(elements)

    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def push(self, new_element):
        revers_elements = list(self.elements)
        revers_elements.append(new_element)
        self.elements = revers_elements
        return self.elements

    def pop(self):
        self.elements.pop(-1)
        # print(f'Верхний элемент стека удален. Верхний элемент стека: {self.elements[-1]}')
        return self.elements[0:]

    def peek(self):
        # print(f'Верхний элемент стека: {self.elements[-1]}')
        return self.elements[-1]

    def size(self):
        size_elements = len(self.elements)
        # print(f'Количество элементов в стеке: {size_elements}')
        return size_elements

def balans(string):
    brackets_open = ('(', '[', '{', '<')
    brackets_closed = (')', ']', '}', '>')
    stack = Stack()
    for i in string:
        if i in brackets_open:
            stack.push(i)
        if i in brackets_closed:
            if stack.size() == 0:
                return 'Небалансированно'
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack.peek() == open_bracket:
                stack.pop()
            else: return 'Небалансированно'
    return 'Сбалансированно'


if __name__ == '__main__':
    print(balans('(((([{}]))))'))
    print(balans('[([])((([[[]]])))]{()}'))
    print(balans('{{[()]}}'))
    print(balans('}{}'))
    print(balans('{{[(])]}}'))
    print(balans('[[{())}]'))
