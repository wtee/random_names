from pyramid.view import view_config
from pyramid.response import Response

from .base import handle_request
from .american_data import female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames

@view_config(route_name="american", renderer="../templates/random_names.jinja2")
def html_view(request):
    route = "american"
    return_dict = handle_request(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames)
    return_dict.update({ "title": "American names",
                            "description": f"First names are from the\
                                            <a href=\"https://www.census.gov/topics/population/genealogy/data/1990_census/1990_census_namefiles.html\">1990 U.S. Census</a>.\
                                            Gender divisions reflect those from the original data. Gender\
                                            non-specific names appear in both the female and male lists\
                                            Last names are from the\
                                            <a href=\"https://www.census.gov/topics/population/genealogy/data/2010_surnames.html\">2010 U.S. Census</a>.\
                                            Both sets of data are in the public domain.\
                                            <a href=\"{ request.route_url('american_data') }\">Download a full copy of the data.</a>",
                                            "route": route,})

    return return_dict


@view_config(route_name="american_text")
def text_view(request):
    names_string = "\n".join(handle_request(request, female_first_names, male_first_names, no_gender_first_names, both_first_names, surnames))
    return Response(content_type="text/plain",
                    charset="utf-8",
                    body=names_string)


@view_config(route_name="american_json", renderer="json")
def json_view(request):
    names_dict = {}
    names_dict["names"] = handle_request(request,
                                female_first_names,
                                male_first_names,
                                no_gender_first_names,
                                both_first_names,
                                surnames)["names"]

    return names_dict

@view_config(route_name="american_data", renderer="json")
def data_view(request):
    return {"female_names": tuple(female_first_names),
            "male_names": tuple(male_first_names),
            "gender_non_specific_names": tuple(no_gender_first_names),
            "surnames": tuple(surnames)}