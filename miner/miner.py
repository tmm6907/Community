import os
from place.models import Place
import requests
import json

zipcodes = [
    # 20001,
    # 20002,
    # 20003,
    # 20004,
    # 20005,
    # 20006,
    # 20007,
    # 20008,
    # 20009,
    # 20010,
    # 20011,
    # 20012,
    # 20015,
    # 20016,
    # 20017,
    # 20018,
    # 20019,
    # 20020,
    # 20024,
    # 20032,
    # 20036,
    # 20037,
    # 20052,
    # 20057,
    # 20064,
    # 20317,
    # 20373,
    # 20390,

    #MD
    20606,
    21001,
    21005,
    21009,
    21520,
    20607,
    21710,
    20762,
    21401,
    21402,
    21403,
    21405,
    20701,
    20608,
    21012,
    20861,
    20609,
    21013,
    21201,
    21202,
    21205,
    21206,
    21209,
    21210,
    21211,
    21212,
    21213,
    21214,
    21215,
    21216,
    21217,
    21218,
    21223,
    21224,
    21229,
    21230,
    21231,
    21239,
    21607,
    20838,
    21521,
    20839,
    21014,
    21015,
    20611,
    21017,
    20705,
    20612,
    21811,
    20814,
    20816,
    20817,
    21610,
    21711,
    21813,
    21522,
    21814,
    20710,
    21523,
    21713,
    20715,
    20716,
    20720,
    20721,
    20841,
    21612,
    20613,
    20722,
    20862,
    20833,
    21225,
    20615,
    21716,
    20616,
    20617,
    21717,
    21718,
    20866,
    20618,
    20818,
    20619,
    20620,
    21613,
    20743,
    21719,
    21228,
    21913,
    21617,
    20621,
    21914,
    20622,
    20623,
    20732,
    21915,
    21619,
    21620,
    20815,
    21622,
    21623,
    20733,
    21028,
    21624,
    20871,
    21029,
    21722,
    20624,
    20735,
    20625,
    21030,
    20740,
    21917,
    20626,
    21044,
    21045,
    21046,
    21918,
    21723,
    21625,
    21524,
    21626,
    21817,
    21627,
    21114,
    21032,
    21628,
    21502,
    21226,
    20872,
    20628,
    21034,
    21035,
    21036,
    21821,
    20751,
    21875,
    21629,
    20855,
    20842,
    20747,
    20629,
    20630,
    21222,
    20754,
    21919,
    21631,
    21601,
    21528,
    21822,
    21037,
    21040,
    21920,
    21075,
    21921,
    21529,
    21042,
    21043,
    21727,
    21221,
    21824,
    21733,
    21047,
    20632,
    21632,
    21048,
    21634,
    21530,
    21050,
    21051,
    20755,
    21052,
    20744,
    21701,
    21702,
    21703,
    21704,
    21053,
    20758,
    21531,
    21532,
    21826,
    20759,
    21734,
    20877,
    20878,
    20879,
    20882,
    21635,
    20765,
    21054,
    20896,
    21930,
    20874,
    20876,
    21056,
    21829,
    21057,
    21060,
    21061,
    20812,
    21737,
    20769,
    21738,
    21071,
    21636,
    21536,
    21638,
    20634,
    20770,
    21639,
    21010,
    21207,
    21740,
    21742,
    21227,
    21074,
    21750,
    21076,
    21077,
    20776,
    21078,
    21830,
    21640,
    20777,
    21641,
    20636,
    20637,
    21031,
    20639,
    21643,
    20781,
    20782,
    20783,
    20784,
    20785,
    21082,
    21754,
    20640,
    21644,
    20645,
    21084,
    21755,
    20794,
    21085,
    21756,
    21645,
    20895,
    21757,
    21087,
    21538,
    21758,
    20646,
    20706,
    20707,
    20708,
    20723,
    20724,
    20650,
    20653,
    21762,
    21835,
    21090,
    21766,
    21539,
    20711,
    21540,
    20657,
    21093,
    21648,
    21102,
    20658,
    21837,
    21838,
    21104,
    21649,
    21105,
    21650,
    21767,
    21647,
    20659,
    21220,
    21769,
    21542,
    21543,
    21108,
    21651,
    21111,
    21770,
    20886,
    21771,
    20712,
    21545,
    21773,
    20662,
    21840,
    21774,
    21776,
    21841,
    20664,
    21653,
    20714,
    21901,
    21236,
    21550,
    21842,
    21113,
    21555,
    20832,
    20736,
    21117,
    21654,
    20745,
    20667,
    21120,
    21234,
    21849,
    21122,
    20670,
    21128,
    21902,
    21130,
    21903,
    21131,
    21208,
    20674,
    21850,
    21851,
    21777,
    20675,
    20837,
    21904,
    20676,
    20677,
    20854,
    21655,
    20678,
    21853,
    21132,
    21856,
    21657,
    21658,
    21133,
    21557,
    21136,
    21659,
    20680,
    21660,
    21911,
    21140,
    20737,
    21661,
    20850,
    20851,
    20852,
    20853,
    21778,
    21779,
    21237,
    21662,
    21780,
    20684,
    20685,
    21663,
    21801,
    21804,
    20860,
    20763,
    20687,
    21664,
    21144,
    21146,
    20764,
    21782,
    21861,
    21665,
    21862,
    20901,
    20902,
    20903,
    20904,
    20905,
    20906,
    20910,
    21783,
    21863,
    20688,
    21152,
    21219,
    20868,
    21560,
    21666,
    21667,
    21864,
    21154,
    21668,
    20746,
    20689,
    21561,
    21784,
    20912,
    20690,
    21787,
    21669,
    20748,
    21788,
    21671,
    21672,
    21204,
    21286,
    20779,
    21673,
    21790,
    21865,
    21866,
    21791,
    21867,
    21156,
    20772,
    20774,
    21155,
    20692,
    21869,
    20601,
    20602,
    20603,
    21793,
    21912,
    20880,
    20693,
    21794,
    20778,
    21562,
    21157,
    21158,
    21871,
    21872,
    21161,
    21162,
    20695,
    21160,
    21874,
    21795,
    21244,
    21675,
    21676,
    21797,
    21798,
    21163,
    21677,
    21678,
    21679,
]

places = [
    'grocery store',
    'primary care',
    'bank',
    'park',
    'mental health service',
    'emergency service',
    'pharmacy',
    'post office',
    'trail',
    'public transportation',
    'fedex',
    'ups',
    'dental care'
]

# Create your views here.
API_KEY = os.environ['PLACES_API_KEY']
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"


def search_nearby_place(place, zipcode):
    query = "{} in {}".format(place, zipcode)
    print(query)
    res = requests.request("GET", url + 'query=' + query + '&key='+API_KEY)
    if res.status_code == '400':
        return False
    else:
        api_places = json.loads(res.text)
        if api_places:
            for location in api_places.get('results'):
                try:
                    location.get('photos')
                    photos = location.get('photos')
                    photo = photos[0]
                    photo = photo["photo_reference"]
                    try:
                        new_place = Place(
                            name=location.get('name'),
                            formatted_address=location.get('formatted_address'),
                            phone_number=location.get('formatted_phone_number'),
                            zip_code=zipcode,
                            url=location.get('url'),
                            website=location.get('website'),
                            photos=photo,
                            rating=location.get('rating'),
                            category=place,
                        )
                        new_place.save()
                    except:
                        continue
                except:
                    continue
        else:
            return False
