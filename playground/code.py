from facebook_scraper import get_posts

for post in get_posts('beaverconfessions', pages=2):
    # print(post.keys())
    print(post['text'])
    print(post['reactions'])
    print(post['reaction_count'])
    print()