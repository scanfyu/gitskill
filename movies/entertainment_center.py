#-*- coding: UTF-8 -*- 

import media

toy_story = media.Movie("firefighter",
                        "how a firefighter becomes strong",
                        "http://baike.baidu.com/pic/%E7%81%AB%E5%BD%B1%E5%BF%8D%E8%80%85/8702/0/d000baa1cd11728bdff895dacafcc3cec2fd2c74?fr=lemma&ct=single",
                        "http://list.youku.com/show/id_zcc001f06962411de83b1.html")

# print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://imgsa.baidu.com/baike/c0%3Dbaike150%2C5%2C5%2C150%2C50/sign=fe876963750e0cf3b4fa46a96b2f997a/faf2b2119313b07ea45594790bd7912396dd8cd3.jpg",
                     "http://v.youku.com/v_show/id_XODMwMjI2NTQ4.html?from=s1.8-3-1.1")

print(avatar.storyline)

avatar.show_trailer()