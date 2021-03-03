import random
import os
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'vanlyapp'
insta_password = os.environ[f'{insta_username}_psw']

dont_likes = ['sex', 'nude', 'naked', 'beef', 'pork', 'seafood',
              'egg', 'chicken', 'cheese', 'sausage', 'lobster',
              'fisch', 'schwein', 'lamm', 'rind', 'kuh', 'meeresfrüchte',
              'schaf', 'ziege', 'hummer', 'yoghurt', 'joghurt', 'dairy',
              'meal', 'food', 'eat', 'pancake', 'cake', 'dessert',
              'protein', 'essen', 'mahl', 'breakfast', 'lunch',
              'dinner', 'turkey', 'truthahn', 'plate', 'bacon',
              'sushi', 'burger', 'salmon', 'shrimp', 'steak',
              'schnitzel', 'goat', 'oxtail', 'mayo', 'fur', 'leather',
              'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy',
              'breakfast', 'dinner', 'lunch']

friends = ['livio.colleluori', 'salty.sealion', 'caityrock', 'lanereisig', '__agartha_',
           'spicy.muffin', 'emma.thenomad', 'alecbrower', 'derek_montes', 'gigihasart']

like_tag_list = ['vanlife', 'vanlifecommunity', 'vanlifemeetup', 'vandiaries', 'vwvan', 'vanlifestyle', 'roadtrip', 'adventure', 'homeonwheels', 'vanlifeculture', 'optoutside',  'vanlifesociety', 'vanlifeexplorers', 'vanlifers', 'campervanlife',
                 'vanliving', 'vanlifeideas', 'vanlifeproject', 'homeiswhereyouparkit', 'busconversion', 'vanbuild', 'vanlifemovement', 'vanlifediaries', 'vanlifesociety', 'vancrush', 'projectvanlife', 'vanlifeideas', 'ontheroad', 'livingsmall']


accounts = ['vanlifediaries','j_bonde', 'mitch_cox', 'nasrvanlife', 'rochelleallen', 'vanlifeisawesome', 'vanlife.living', 'vanlife.culture', 'vanlifecamper', 'vanlifedistrict',  'vanlife.journal', 'vanlifevirals', 'travywild',
            'tommycampervans', 'vandoitco', 'flarespace',  'vanliferules', 'vanlife.living', 'thevanlifeapp', 'van_craft']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    # settings
    # session.set_relationship_bounds(enabled=True,
    #                               max_followers=40000)

    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)

    session.set_user_interact(amount=25, randomize=True, percentage=15)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=25)

    # activity
    session.like_by_tags(random.sample(like_tag_list, 15),
                         amount=random.randint(20, 60), interact=True)

    session.unfollow_users(amount=random.randint(70, 210),
                           instapy_followed_enabled=(True, "all"), style="FIFO",
                           unfollow_after=90 * 60 * 60, sleep_delay=501)

    # """ Joining Engagement Pods...
    # """
    # photo_comments = ['Nice shot! @{}',
    #                   'I love your profile! @{}',
    #                   'Wonderful :thumbsup:',
    #                   'Just incredible :open_mouth:',
    #                   'What camera did you use @{}?',
    #                   'Love your posts @{}',
    #                   'Looks awesome @{}',
    #                   'Getting inspired by you @{}',
    #                   ':raised_hands: Yes!']

    # session.set_do_comment(enabled=False, percentage=95)
    # session.set_comments(photo_comments, media='Photo')
    # session.join_pods(topic='travel')
