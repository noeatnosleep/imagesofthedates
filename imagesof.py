import time
import praw
import os
import re
import Subreddits
import Domains


r = praw.Reddit('ImagesOf v2.2 /u/amici_ursi, /u/captainmeta4, /u/noeatnosleep')

print("Getting user blacklist")
userblacklist_wiki = r.get_wiki_page("ImagesOfNetwork","userblacklist")
userblacklist = set([name.strip().lower()[3:] for name in userblacklist_wiki.content_md.split("\n") if name.strip() != ""])


def search_for_places(r):
    submission_stream = praw.helpers.submission_stream(r, 'all')
    print("searching for posts...")
    for submission in submission_stream:
        title = submission.title
#1800s
        if re.search("\\b18[0-9][0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\b18[0-9][0-9].?(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩)|(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩).?18[0-9][0-9]\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.domain).lower().endswith(Domains.domains) == False:
                continue
            if str(submission.author).lower() in userblacklist:
                continue
            if str(submission.subreddit).lower() in Subreddits.subreddits:
                continue
            if str(submission.author).lower() == 'blacklisteduser':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1800s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            make_post(r, submission, 'imagesofthe1800s')
#1900s
        if re.search("\\b190[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\b190[0-9].?(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩)|(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩).?190[0-9]\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.domain).lower().endswith(Domains.domains) == False:
                continue
            if str(submission.author).lower() in userblacklist:
                continue
            if str(submission.subreddit).lower() in Subreddits.subreddits:
                continue
            if str(submission.author).lower() == 'blacklisteduser':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1900s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            make_post(r, submission, 'imagesofthe1900s')
#1910s
        if re.search("\\b191[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\b191[0-9].?(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩)|(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩).?191[0-9]\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.domain).lower().endswith(Domains.domains) == False:
                continue
            if str(submission.author).lower() in userblacklist:
                continue
            if str(submission.subreddit).lower() in Subreddits.subreddits:
                continue
            if str(submission.author).lower() == 'blacklisteduser':
                continue
            if str(submission.subreddit).lower() in ('imagesofthe1910s', '1911fans'):
                continue
            if submission.over_18:  # skip if nsfw
                continue
            make_post(r, submission, 'imagesofthe1910s')
#1920s
        if re.search("\\b192[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\b192[0-9].?(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩)|(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩).?192[0-9]\\b)", title, flags=re.IGNORECASE) != None: #don't post if a variation of "1920 x" or "x 1920"
                continue
            if str(submission.domain).lower().endswith(Domains.domains) == False:
                continue
            if str(submission.author).lower() in userblacklist:
                continue
            if str(submission.subreddit).lower() in Subreddits.subreddits:
                continue
            if str(submission.author).lower() == 'blacklisteduser':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1920s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            make_post(r, submission, 'imagesofthe1920s')
#1930s
        if re.search("\\b193[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\b193[0-9].?(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩)|(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩).?193[0-9]\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.domain).lower().endswith(Domains.domains) == False:
                continue
            if str(submission.author).lower() in userblacklist:
                continue
            if str(submission.subreddit).lower() in Subreddits.subreddits:
                continue
            if str(submission.author).lower() == 'blacklisteduser':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1930s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            make_post(r, submission, 'imagesofthe1930s')
#1940s
        if re.search("\\b194[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\b194[0-9].?(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩)|(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩).?194[0-9]\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.domain).lower().endswith(Domains.domains) == False:
                continue
            if str(submission.author).lower() in userblacklist:
                continue
            if str(submission.subreddit).lower() in Subreddits.subreddits:
                continue
            if str(submission.author).lower() == 'blacklisteduser':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1940s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            make_post(r, submission, 'imagesofthe1940s')
#1950s
        if re.search("\\b195[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\b195[0-9].?(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩)|(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩).?195[0-9]\\b)", title, flags=re.IGNORECASE) != None:
                continue
 
            if str(submission.domain).lower().endswith(Domains.domains) == False:
                continue
            if str(submission.author).lower() in userblacklist:
                continue
            if str(submission.subreddit).lower() in Subreddits.subreddits:
                continue
            if str(submission.author).lower() == 'blacklisteduser':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1950s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            make_post(r, submission, 'imagesofthe1950s')
#1960s
        if re.search("\\b196[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\b196[0-9].?(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩)|(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩).?196[0-9]\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.domain).lower().endswith(Domains.domains) == False:
                continue
            if str(submission.author).lower() in userblacklist:
                continue
            if str(submission.subreddit).lower() in Subreddits.subreddits:
                continue
            if str(submission.author).lower() == 'blacklisteduser':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1960s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            make_post(r, submission, 'imagesofthe1960s')
#1970s
        if re.search("\\b197[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\b197[0-9].?(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩)|(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩).?197[0-9]\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.domain).lower().endswith(Domains.domains) == False:
                continue
            if str(submission.author).lower() in userblacklist:
                continue
            if str(submission.subreddit).lower() in Subreddits.subreddits:
                continue
            if str(submission.author).lower() == 'blacklisteduser':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1970s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            make_post(r, submission, 'imagesofthe1970s')
#1980s
        if re.search("\\b198[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\b198[0-9].?(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩)|(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩).?198[0-9]\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.domain).lower().endswith(Domains.domains) == False:
                continue
            if str(submission.author).lower() in userblacklist:
                continue
            if str(submission.subreddit).lower() in Subreddits.subreddits:
                continue
            if str(submission.author).lower() == 'blacklisteduser':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1980s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            make_post(r, submission, 'imagesofthe1980s')
#1990s
        if re.search("\\b199[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\b199[0-9].?(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩)|(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩).?199[0-9]\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.domain).lower().endswith(Domains.domains) == False:
                continue
            if str(submission.author).lower() in userblacklist:
                continue
            if str(submission.subreddit).lower() in Subreddits.subreddits:
                continue
            if str(submission.author).lower() == 'blacklisteduser':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1990s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            make_post(r, submission, 'imagesofthe1990s')
#2000s
        if re.search("\\b200[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\b200[0-9].?(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩)|(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩).?200[0-9]\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.domain).lower().endswith(Domains.domains) == False:
                continue
            if str(submission.author).lower() in userblacklist:
                continue
            if str(submission.subreddit).lower() in Subreddits.subreddits:
                continue
            if str(submission.author).lower() == 'blacklisteduser':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe2000s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            make_post(r, submission, 'imagesofthe2000s')
#2010s
        if re.search("\\b201[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\b201[0-9].?(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩)|(x|\*|-|✗|✘|×|╳|☓|✕|✖|⨉|⨯|🞩).?201[0-9]\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.domain).lower().endswith(Domains.domains) == False:
                continue
            if str(submission.author).lower() in userblacklist:
                continue
            if str(submission.subreddit).lower() in Subreddits.subreddits:
                continue
            if str(submission.author).lower() == 'blacklisteduser':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe2010s' or str(submission.subreddit).lower() == 'cutekorean':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            make_post(r, submission, 'imagesofthe2010s')


def make_post(r, originalsubmission, subreddit):
    title = 'originalsubmission.title'
    comment = '[Original post]({}) by /u/{} in /r/{} '.format(originalsubmission.permalink,
                                                    originalsubmission.author,
                                                    originalsubmission.subreddit)
    print("Making post in {}...".format(subreddit))
    while True:
        try:
            xpost = r.submit(subreddit, title, url=originalsubmission.url, captcha=None, send_replies=True)
            xpost.add_comment(comment)
            break
        except praw.errors.AlreadySubmitted as e:
            print("Already submitted. Skipping.")
            break
        except praw.errors.RateLimitExceeded as e:
            print(("ERROR: Rate limit exceeded. Sleeping for " +
                   "{} seconds".format(e.sleep_time)))
            time.sleep(e.sleep_time)
        except praw.errors.APIException as e:
            print("API error. Skipping.")
            break
        
def praw_oauth_login(r):
    
    print('authorizing...')
    
    #Load keys from heroku config vars
    client_id = os.environ.get("client_id")
    client_secret = os.environ.get("client_secret")
    redirect_uri = "http://127.0.0.1:65010/authorize_callback"
    refresh_token=os.environ.get("refresh_token")
    
    #Set the oauth app info and get authorization
    r.set_oauth_app_info(client_id, client_secret, redirect_uri)
    r.refresh_access_information(refresh_token)
    
    print('...done')


def main():
    print("Logging in...")
    
    praw_oauth_login(r)

    while True:
        try:
            search_for_places(r)
        except praw.errors.HTTPException:
            print("Reddit is down. Sleeping...")
            time.sleep(360)

if __name__ == '__main__':
    main()
