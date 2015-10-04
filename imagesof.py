import time
import praw
import OAuth2Util
import re


def search_for_places(r, o):
    submission_stream = praw.helpers.submission_stream(r, 'all')
    print("searching for posts...")
    for submission in submission_stream:
        o.refresh()
        title = submission.title
#1800s
        if re.search("\\b18[00-99]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1800s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe1800s')
#1900s
        if re.search("\\b190[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1900s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe1900s')
#1910s
        if re.search("\\b191[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1910s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe1910s')
#1920s
        if re.search("\\b192[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1920s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe1920s')
#1930s
        if re.search("\\b193[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1930s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe1930s')
#1940s
        if re.search("\\b194[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1940s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe1940s')

#1950s
        if re.search("\\b195[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1950s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe1950s')
#1960s
        if re.search("\\b196[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1960s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe1960s')
#1970s
        if re.search("\\b197[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1970s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe1970s')
#1980s
        if re.search("\\b198[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1980s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe1980s')
#1990s
        if re.search("\\b199[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe1990s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe1990s')
#2000s
        if re.search("\\b200[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe2000s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe2000s')
#2010s
        if re.search("\\b201[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe2010s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe2010s')
#2020s
        if re.search("\\b202[0-9]\\b", title, flags=re.IGNORECASE) != None:
            if re.search("(\\bbadkeyword\\b)", title, flags=re.IGNORECASE) != None:
                continue
            if str(submission.author).lower() == 'rpbot' or str(submission.author).lower() == 'amici_ursi' or str(submission.author).lower() == 'noeatnosleep':
                continue
            if str(submission.subreddit).lower() == 'imagesofthe2020s':
                continue
            if submission.over_18:  # skip if nsfw
                continue
            if 'imgur' not in submission.url and 'deviantart' not in submission.url:
                continue
            make_post(r, submission, 'imagesofthe2020s')


def make_post(r, originalsubmission, subreddit):
    title = "\"{}\" by {} in {}".format(originalsubmission.title, originalsubmission.author,
                                              originalsubmission.subreddit)
    comment = '[Original post]({}) in /r/{}'.format(originalsubmission.permalink,
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


def main():
    print("Logging in...")
    r = praw.Reddit('ImagesOf v2.05 /u/amici_ursi')
    o = OAuth2Util.OAuth2Util(r, print_log=True)

    while True:
        try:
            search_for_places(r, o)
        except praw.errors.HTTPException:
            print("Reddit is down. Sleeping...")
            time.sleep(360)

if __name__ == '__main__':
    main()