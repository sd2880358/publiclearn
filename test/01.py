def SayHello(name):
    print('I want to say hello with you, {0}'.format(name))
    print('hello,{0} '.format(name))
    print('done','*'*20)

if __name__ == '__main__':
    print('*'*20)
    name = input ('please input your name:  ')
    print(SayHello(name = name ))
    print('*'*20)

