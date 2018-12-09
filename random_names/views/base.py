import random

def handle_request(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames):
    gender_options = ("any gender", "female", "male", "gender non-specific")

    if 'number' not in request.GET:
        number = 1
    else:
        number = int(request.GET["number"])
        if number > 100:
            number = 100
        elif number < 1:
            number = 1

    numbers = range(1,101)
    return_numbers = [number] + [n for n in numbers if n != number]

    if 'gender' not in request.GET:
        firsts = random.sample(both_first_names, number)
        return_options = gender_options
    else:
        return_options = [request.GET['gender']] + [g for g in gender_options if g != request.GET['gender']]
    
        if request.GET['gender'] == 'gender non-specific':
            firsts = random.sample(no_gender_first_names, number)
        elif request.GET['gender'] == 'female':
            firsts = random.sample(female_first_names, number)
        elif request.GET['gender'] == 'male':
            firsts = random.sample(male_first_names, number)
        elif request.GET['gender'] == 'any gender':
            firsts = random.sample(both_first_names, number)
        else:
            firsts = random.sample(both_first_names, number)
    
    lasts  = random.sample(surnames, number)

    names = [" ".join([first, last]) for first, last in zip(firsts, lasts)]

    return {"names": names, "options": return_options, "numbers": return_numbers}