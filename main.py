from InstaFollower import InstaFollower

similar_account = "pycodebr"
USERNAME = "Your email comes here"
PASSWORD = "You password comes here"
bot = InstaFollower()
bot.login(USERNAME,PASSWORD)
bot.find_followers(similar_account)
bot.follow()

