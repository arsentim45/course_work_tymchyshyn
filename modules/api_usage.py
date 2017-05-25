from instagram.client import InstagramAPI

access_token =  9cfaf61e97e7408082a76bd777133e7f
client_secret = ab35b87e649e49aaacb8e9397ff24981

media_id = input()

list1 = api.media_likes(media_id)

class ApiModel(object):

    @classmethod
    def object_from_dictionary(cls, entry):
        # make dict keys all strings
        if entry is None:
            return ""
        entry_str_dict = dict([(str(key), value) for key, value in entry.items()])
        return cls(**entry_str_dict)

    def __repr__(self):
        return str(self)
        # if six.PY2:
        #     return six.text_type(self).encode('utf8')
        # else:
        #     return self.encode('utf8')

    def __str__(self):
        if six.PY3:
            return self.__unicode__()
        else:
            return unicode(self).encode('utf-8')

class Media(ApiModel):
    if 'user_has_liked' in entry:
        new_media.user_has_liked = entry['user_has_liked']
    new_media.like_count = entry['likes']['count']
    new_media.likes = []
    if 'data' in entry['likes']:
        for like in entry['likes']['data']:
            new_media.likes.append(User.object_from_dictionary(like))