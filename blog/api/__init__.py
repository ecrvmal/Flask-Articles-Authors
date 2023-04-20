from flask_combo_jsonapi import Api
from blog.api.tag import TagList, TagDetail
from combojsonapi.spec import ApiSpecPlugin


def init_api(app):
    api = Api(app)
    api.route(TagList, "tag_list", "/api/tags/", tag="Tag")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/", tag="Tag")
    return api
