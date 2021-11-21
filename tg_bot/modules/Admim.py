from tg_bot.modules.helper_funcs.decorators import kigcallback
from telegram import (
    ParseMode,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext
from tg_bot.modules.language import gs

def fmt_md_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        gs(update.effective_chat.id, "md_help"),
        parse_mode=ParseMode.HTML,
    )


def fmt_filling_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        gs(update.effective_chat.id, "filling_help"),
        parse_mode=ParseMode.HTML,
    )



@kigcallback(pattern=r"fmt_help_")
def fmt_help(update: Update, context: CallbackContext):
    query = update.callback_query
    bot = context.bot
    help_info = query.data.split("fmt_help_")[1]
    if help_info == "ban":
        help_text = gs(update.effective_chat.id, "bans_help")
    elif help_info == "warn":
        help_text = gs(update.effective_chat.id, "warns_help") 
    elif help_info == "mute":
        help_text = gs(update.effective_chat.id, "mute_help") 
    elif help_info == "lock":
        help_text = gs(update.effective_chat.id, "locks_help") 
    query.message.edit_text(
        text=help_text,
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Back", callback_data=f"help_module({__mod_name__.lower()})"),
            InlineKeyboardButton(text='Report Error', url='https://t.me/YorkTownEagleUnion')]]
        ),
    )
    bot.answer_callback_query(query.id)

__mod_name__ = 'SammyLwda'

def get_help(chat):
    return [gs(chat, "formt_help_bse"),
    [
        InlineKeyboardButton(text="BAN", callback_data="fmt_help_ban"),
        InlineKeyboardButton(text="WARN", callback_data="fmt_help_warn")
    ], 
    [
        InlineKeyboardButton(text="MUTE", callback_data="fmt_help_mute"),
        InlineKeyboardButton(text="LOCK", callback_data="fmt_help_lock")
    ]
]
