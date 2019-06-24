class Expression:
    def eval(self, x_value):
        '''変数 x の値が x_value だった時の式の値を返すメソッド'''
        raise NotImplementedError
    
    def diff(self):
        '''式を変数 x で微分した式に対応する Expression オブジェクト
        を返すメソッド'''
        raise NotImplementedError

class Number(Expression):
    '''変更の必要なし'''
    def __init__(self, number):
        self.number = number
    
    def eval(self, x_value):
        return self.number
    
    def diff(self):
        return Number(0)

class BinaryExpression(Expression):
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2

class Add(BinaryExpression):
    def eval(self,x_value):
        return self.number1.eval(x_value) + self.number2.eval(x_value)

    def diff(self):
        return Add(self.number1.diff(),self.number2.diff())

class Sub(BinaryExpression):
    def eval(self,x_value):
        return self.number1.eval(x_value) - self.number2.eval(x_value)

    def diff(self):
        return Sub(self.number1.diff(),self.number2.diff())

class Mul(BinaryExpression):
    def eval(self,x_value):
        return self.number1.eval(x_value) * self.number2.eval(x_value)

    def diff(self):
        if 'X' in str(type(self.number1)) and 'X' in str(type(self.number2)):
            return Mul(Number(2),self.number1)
        elif 'Number' in str(type(self.number1)) and 'X' in str(type(self.number2)):
            return self.number1
        elif 'X' in str(type(self.number1)) and 'Number' in str(type(self.number2)):
            return self.number1
        else:
            return Number(0)

class Div(BinaryExpression):
    def eval(self,x_value):
        return self.number1.eval(x_value) / self.number2.eval(x_value)
    
    def diff(self):
        item1 = Mul(self.number1.diff(),self.number2)
        item2 = Mul(self.number1,self.number2.diff())
        return Div(Sub(item1,item2),Mul(self.number2,self.number2))
                   
class X(Expression):
    def eval(self, x_value):
        self.x_value = x_value
        return self.x_value

    def diff(self):
        return Number(1)