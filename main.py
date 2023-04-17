#!/usr/bin/env python

import logging
import config
import wisdom
import os

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except:
    __version_info__ == (0,0,0,0,0)

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")

async def fortune(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    allowed_args = ["dbs", "db"]
    args = update.message.text.replace('/fortune', '').strip()
    logger.info(args)
    if args.split(' ')[0] not in allowed_args:
        fortune = wisdom.get_fortune()
        logger.info(fortune)
        await update.message.reply_text(fortune)
    else:
        if args.split(' ')[0] == "dbs":
            dbs = wisdom.dbs()
            dbs = [db.split('/')[-1] for db in dbs]
            await update.message.reply_text(dbs)
        elif args.split(' ')[0] == "db":
            fortune_db = os.path.join(config.REPOPATH, args.split(' ')[1])
            logger.info(fortune_db)
            await update.message.reply_text(wisdom.get_fortune(random=False, db=fortune_db))

def main() -> None:
    application = Application.builder().token(config.TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("fortune", fortune))

    application.run_polling()

if __name__ == "__main__":
    main()