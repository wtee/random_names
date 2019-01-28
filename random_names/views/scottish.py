import random

from pyramid.view import view_config

from .base import _data_view, _handle_request, _json_view, _text_view
from random_names.data.scottish_data import female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames

@view_config(route_name="scottish", renderer="../templates/random_names.jinja2")
def html_view(request):
    route = "scottish"
    return_dict = _handle_request(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames)
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
    return _text_view(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames)


@view_config(route_name="scottish_json", renderer="json")
def json_view(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames):
    return _json_view(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames)

@view_config(route_name="scottish_data", renderer="json")
def data_view(request):
    return _data_view(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames)