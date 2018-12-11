import random

from pyramid.response import Response

def _handle_request(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames):
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


def _data_view(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames):
    return {"female_names": tuple(female_first_names),
            "male_names": tuple(male_first_names),
            "gender_non_specific_names": tuple(no_gender_first_names),
            "surnames": tuple(surnames)}


def _json_view(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames):
    names_dict = {}
    names_dict["names"] = _handle_request(request,
                                female_first_names,
                                male_first_names,
                                no_gender_first_names,
                                both_first_names,
                                surnames)["names"]


def _text_view(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames):
    names_string = "\n".join(_handle_request(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames)["names"])
    return Response(content_type="text/plain",
                    charset="utf-8",
                    body=names_string)
