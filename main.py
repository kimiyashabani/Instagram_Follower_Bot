from InstaFollower import InstaFollower

similar_account = "pycodebr"
USERNAME = "kimiyashabani@outlook.com"
PASSWORD = "JErU&.)z27dLjJD"
bot = InstaFollower()
bot.login(USERNAME,PASSWORD)
bot.find_followers(similar_account)
bot.follow()

