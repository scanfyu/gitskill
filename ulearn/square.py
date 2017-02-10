import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

# turtle 是一个类；brad 和 angie是实例
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    # 创建 turtle Brad -划一个方形
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    # 创建 turtle angie -划一个圈
    '''
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    '''

    window.exitonclick()

draw_art()