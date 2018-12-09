import random

from pyramid.view import view_config
from pyramid.response import Response

from .base import handle_request
from .scottish_data import female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames

@view_config(route_name="scottish", renderer="../templates/random_names.jinja2")
def html_view(request):
    route = "scottish"
    return_dict = handle_request(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames)
    return_dict.update({ "title": "Scottish names",
                            "description": f"First names are from the Scotland's 2017, 2007, 1997, 1987, and 1977\
                                            <a href=\"https://www.nrscotland.gov.uk/statistics-and-data/statistics/statistics-by-theme/vital-events/names/babies-first-names\">Full list of babies' first names</a>.\
                                            Gender divisions reflect those from the original data. Gender\
                                            non-specific names appear in both the female and male lists\
                                            Last names are from Scotland's 2017\
                                            <a href=\"https://www.nrscotland.gov.uk/statistics-and-data/statistics/statistics-by-theme/vital-events/names/most-common-surnames\">List of most common surnames</a>.\
                                            Both sets of data are the creation of the Scottish Government and under Crown Copyright, released under the terms of the\
                                            <a href=\"http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/\">Open Government Licence, v. 3</a>.\
                                            <a href=\"{ request.route_url('scottish_data') }\">Download a full copy of the data.</a>",
                                            "route": route,})

    return return_dict


@view_config(route_name="scottish_text")
def text_view(request):
    names_string = "\n".join(handle_request(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames))
    return Response(content_type="text/plain",
                    charset="utf-8",
                    body=names_string)


@view_config(route_name="scottish_json", renderer="json")
def json_view(request):
    names_dict = {}
    names_dict["names"] = handle_request(request,
                                female_first_names,
                                male_first_names,
                                no_gender_first_names,
                                both_first_names,
                                surnames)["names"]

    return names_dict

@view_config(route_name="scottish_data", renderer="json")
def data_view(request):
    return {"female_names": tuple(female_first_names),
            "male_names": tuple(male_first_names),
            "gender_non_specific_names": tuple(no_gender_first_names),
            "surnames": tuple(surnames)}