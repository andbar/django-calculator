from django.shortcuts import render, render_to_response


def check_input(symbol, num_one, num_two):
    if symbol == "/" and float(num_two) == 0.0:
        context = {"message": "Can't divide by zero! Try again."}
    else:
        try:
            result = do_math(symbol, num_one, num_two)
            context = {"message": "{} {} {} = {}".format(num_one, symbol, num_two, result), "result": str(result)}
        except:
            context = {"message": "That's not a number! Try again."}
    return context


def do_math(symbol, num_one, num_two):
    if symbol == "+":
        return float(num_one) + float(num_two)
    elif symbol == "-":
        return float(num_one) - float(num_two)
    elif symbol == "*":
        return float(num_one) * float(num_two)
    elif symbol == "/":
        return float(num_one) / float(num_two)


def index_view(request):
    operat = request.GET.get("operator")
    first_number = request.GET.get("first_num")
    second_number = request.GET.get("second_num")
    if operat:
        context = check_input(operat, first_number, second_number)
    else:
        context = {}
    return render_to_response(template_name='calculator.html', context=context)
