length = len(formatted_name)

def format_name(f_name, l_name):
    """Выбирается первое и последнее имя, плсле чего
    возвращается текст с регистром в каждом слова"""
    if f_name == "" or l_name == "":
        return "Error"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?"), input("What is your last name?")))

format_name()