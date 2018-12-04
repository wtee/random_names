def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('american', '/american.html')
    config.add_route('american_text', '/american.txt')
    config.add_route('american_json', '/american.json')
    config.add_route('american_data', '/american/data.json')
