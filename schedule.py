
# BATCH with cron

# from routes.shorturl.controllers import deleteOldShortLinks
# from database import SQLALCHEMY_DATABASE_URI
# from fastapi_utils.session import FastAPISessionMaker
# from apscheduler.schedulers.background import BackgroundScheduler

# sessionmaker = FastAPISessionMaker(SQLALCHEMY_DATABASE_URI)
# scheduler = BackgroundScheduler()

# def deleteOldShortLinksBatch():
#     print("executed :: deleteOldShortLinks")
#     with sessionmaker.context_session() as db:
#         minuteOld = 60 * 24 * 7 * 2    # 2 weeks old
#         deleteOldShortLinks(minuteOld, db)

# scheduler.add_job(deleteOldShortLinksBatch, 'cron', hour=23, minute=30)

# scheduler.start()